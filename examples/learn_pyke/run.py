# run.py

import sys
from pyke import knowledge_engine, krb_traceback

engine = knowledge_engine.engine()

def run():
    engine.reset()
    try:
        engine.activate("pattern_matching")
        engine.prove_1("pattern_matching", "knows_pattern_matching")
    except StandardError:
        krb_traceback.print_exc()
        sys.exit(1)

