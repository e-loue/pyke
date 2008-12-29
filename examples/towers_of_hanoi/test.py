# test.py

from __future__ import with_statement
import sys
import os.path
from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(os.path.dirname(__file__),
                                 'examples.towers_of_hanoi.compiled_krb')

def test(num_disks):
    engine.reset()
    try:
        engine.activate('towers_of_hanoi')
  
        with engine.prove_n('towers_of_hanoi', 'solve', (num_disks,), 1) as gen:
            for i, ((moves,), no_plan) in enumerate(gen):
                print "got %d:" % (i + 1), moves
    except:
        krb_traceback.print_exc()
        sys.exit(1)

