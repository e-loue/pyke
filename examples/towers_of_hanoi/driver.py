# driver.py

from __future__ import with_statement
import sys
from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)

def test(num_disks):
    engine.reset()
    try:
        engine.activate('towers_of_hanoi')
  
        with engine.prove_goal('towers_of_hanoi.solve($num_disks, $moves)',
                               num_disks=num_disks) \
          as gen:
            for i, (vars, no_plan) in enumerate(gen):
                print "got %d:" % (i + 1), vars['moves']
    except:
        krb_traceback.print_exc()
        sys.exit(1)

