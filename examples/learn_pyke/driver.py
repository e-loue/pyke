# driver.py

import sys
from pyke import knowledge_engine, krb_traceback

engine = knowledge_engine.engine(__file__)

def run():
    engine.reset()
    try:
        engine.activate('pattern_matching')
        engine.prove_1_goal('pattern_matching.knows_pattern_matching()')
    except StandardError:
        krb_traceback.print_exc()
        sys.exit(1)

