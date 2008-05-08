# test.py

import sys
from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine()

def init(engine):
    def add_fact(predicate, child, father, mother):
        engine.add_universal_fact('family', predicate, (child, father, mother))

    add_fact('son_of', 'egon', 'anton', 'brigitte')
    add_fact('son_of', 'ralf', 'anton', 'brigitte')
    add_fact('son_of', 'anton', 'johann', 'maria')
    add_fact('daugther_of', 'elisabeth', 'johann', 'maria')    
    add_fact('daugther_of', 'karin', 'karl', 'margit')
    add_fact('daugther_of', 'sabine', 'karl', 'margit')

init(engine)

'''
def test():
    engine.reset()
    try:
        engine.activate('fc_notnay')
    except:
        krb_traceback.print_exc()
        sys.exit(1)
'''

def bc_test():
    engine.reset()
    try:
        engine.activate('bc_notany')

        #for (sibling1, sibling2, gender1, gender2 ), plan \
        # in engine.prove_n('bc_notany', 'siblings', (), 4):
        #    print "siblings:", sibling1, sibling2

        for (sibling, gender1, gender2 ), plan \
         in engine.prove_n('bc_notany', 'siblings', ('anton'), 3):
            print "siblings:", 'anton', sibling
           
        for (child,), plan \
         in engine.prove_n('bc_notany', 'child_with_no_aunt', (), 1):
            print child, "has no aunt"

        for (child,), plan \
         in engine.prove_n('bc_notany', 'child_with_no_uncle', (), 1):
            print child, "has no uncle"
    except:
        krb_traceback.print_exc()
        sys.exit(1)

