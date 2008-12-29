# run.py

import sys
import os.path
from pyke import knowledge_engine, krb_traceback

engine = knowledge_engine.engine(os.path.dirname(__file__),
                                 'examples.learn_pyke.compiled_krb')

def run():
    engine.reset()
    try:
        engine.activate("pattern_matching")
        engine.prove_1("pattern_matching", "knows_pattern_matching")
    except StandardError:
        krb_traceback.print_exc()
        sys.exit(1)

