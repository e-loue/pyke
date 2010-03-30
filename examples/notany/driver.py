# driver.py

from __future__ import with_statement
import sys
from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)

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

        #with engine.prove_goal(
        #       'bc_notany.siblings($sibling1, $sibling2, $_, $_)') \
        #  as gen1:
        #    for vars, plan in gen1:
        #        print "siblings:", vars['sibling1'], vars['sibling2']
  
        with engine.prove_goal('bc_notany.child_with_no_aunt($child)') as gen2:
            for vars, plan in gen2:
                print vars['child'], "has no aunt"

        with engine.prove_goal('bc_notany.child_with_no_uncle($child)') as gen3:
            for vars, plan in gen3:
                print vars['child'], "has no uncle"
    except:
        krb_traceback.print_exc()
        sys.exit(1)

