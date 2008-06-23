# run.py

from pyke import knowledge_engine

engine = knowledge_engine.engine()

def run():
    engine.reset()
    engine.activate("pattern_matching")
    engine.prove_1("pattern_matching", "knows_pattern_matching")

