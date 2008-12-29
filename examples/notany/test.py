# test.py

from __future__ import with_statement
import sys
import os.path
from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(os.path.dirname(__file__),
                                 'examples.notany.compiled_krb')

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

        #with engine.prove_n('bc_notany', 'siblings', (), 4) as gen1:
        #    for (sibling1, sibling2, gender1, gender2 ), plan in gen1:
        #        print "siblings:", sibling1, sibling2
  
        with engine.prove_n('bc_notany', 'child_with_no_aunt', (), 1) as gen2:
            for (child,), plan in gen2:
                print child, "has no aunt"

        with engine.prove_n('bc_notany', 'child_with_no_uncle', (), 1) as gen3:
            for (child,), plan in gen3:
                print child, "has no uncle"
    except:
        krb_traceback.print_exc()
        sys.exit(1)

