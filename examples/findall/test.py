# test.py

from __future__ import with_statement
import sys
import os.path
from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(os.path.dirname(__file__),
                                 'examples.findall.compiled_krb')

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
        with engine.prove_n('bc_findall', 'cousins_of', (), 2) as gen:
            for (child, cousins), plan in gen:
                print "%s has %s as cousins" % (child, cousins)
    except:
        krb_traceback.print_exc()
        sys.exit(1)

