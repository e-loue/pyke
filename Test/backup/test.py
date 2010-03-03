# test.py

from pyke import knowledge_engine

def test():
    engine = knowledge_engine.engine(__file__)
    engine.activate('backup')
    (ans,), plan = engine.prove_1('backup', 'top', (), 1)
    print ans
