# test.py

from pyke import knowledge_engine

def test():
    engine = knowledge_engine.engine()
    engine.activate('backup')
    (ans,), plan = engine.prove_1('backup', 'top', (), 1)
    print ans
