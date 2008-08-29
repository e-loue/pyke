# test.py

import sys
from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine()

def fc_test():
    engine.reset()
    try:
        engine.activate('fc_notany')
    except:
        krb_traceback.print_exc()
        sys.exit(1)

def bc_test():
    engine.reset()
    try:
        engine.activate('bc_notany')

        #for (sibling1, sibling2, gender1, gender2 ), plan \
        # in engine.prove_n('bc_notany', 'siblings', (), 4):
        #    print "siblings:", sibling1, sibling2
  
        for (child,), plan \
         in engine.prove_n('bc_notany', 'child_with_no_aunt', (), 1):
            print child, "has no aunt"

        for (child,), plan \
         in engine.prove_n('bc_notany', 'child_with_no_uncle', (), 1):
            print child, "has no uncle"
    except:
        krb_traceback.print_exc()
        sys.exit(1)

