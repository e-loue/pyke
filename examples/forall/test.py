# test.py

import sys
from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine()

def fc_test():
    engine.reset()
    try:
        engine.activate('fc_forall')
    except:
        krb_traceback.print_exc()
        sys.exit(1)

def bc_test():
    engine.reset()
    try:
        engine.activate('bc_forall')
        for (child,), plan \
         in engine.prove_n('bc_forall', 'no_step_siblings', (), 1):
            print child
    except:
        krb_traceback.print_exc()
        sys.exit(1)

