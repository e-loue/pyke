# test.py

from pyke import knowledge_engine

Engine = knowledge_engine.engine('Test.CanNotProve')

def test(kb, ke, arg):
    Engine.reset()
    Engine.activate('rules')
    try:
        Engine.prove_1(kb, ke, (arg,), 0)
    except knowledge_engine.CanNotProve:
        return
    raise AssertionError("test: expected CanNotProve exception")

def dotests():
    test('facts', 'fact1', 2)
    test('facts', 'fact2', 2)
    test('rules', 'rule1', 2)
    test('rules', 'rule2', 2)
    Engine.reset()
    Engine.activate('rules')
    (arg,), no_plan = Engine.prove_1('facts', 'fact3', (), 1)
    assert arg == 'hi\nthere'
