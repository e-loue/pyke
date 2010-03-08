# test.py

from pyke import knowledge_engine

Engine = None

def test(kb, ke, arg):
    global Engine
    if Engine is None:
        Engine = knowledge_engine.engine(__file__)
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
    vars, no_plan = Engine.prove_1_goal('facts.fact3($ans)')
    assert vars['ans'] == 'hi\nthere'
