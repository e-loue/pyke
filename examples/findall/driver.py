# driver.py

from __future__ import with_statement
import sys
from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)

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
        with engine.prove_goal('bc_findall.cousins_of($child, $cousins)') \
          as gen:
            for vars, plan in gen:
                print "%s has %s as cousins" % (vars['child'], vars['cousins'])
    except:
        krb_traceback.print_exc()
        sys.exit(1)

