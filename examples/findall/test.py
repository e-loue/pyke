# test.py

import sys
from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine()

def init(engine):
    def child_of(child, father, mother):
        engine.add_universal_fact('family', 'child_of', (child, father, mother))
    child_of('egon', 'anton', 'hilde')
    child_of('ralf', 'anton', 'hilde')
    child_of('hilde', 'stefan', 'brigitte')
    child_of('diethelm', 'stefan', 'brigitte')
    child_of('harald', 'diethelm', 'gitte')
    child_of('claudia', 'diethelm', 'gitte')
    
init(engine)

def test():
    engine.reset()
    try:
        engine.activate('fc_findall')
    except:
        krb_traceback.print_exc()
        sys.exit(1)

def bc_test():
    engine.reset()
    try:
        engine.activate('bc_findall')
        for (child, cousins), plan \
         in engine.prove_n('bc_findall', 'cousins_of', (), 2):
            print "%s has %s as cousins" % (child, cousins)
    except:
        krb_traceback.print_exc()
        sys.exit(1)

