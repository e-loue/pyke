# test.py

import sys
from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine()

def fc_test():
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

