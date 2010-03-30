# driver.py

from pyke import knowledge_engine

def run():
    engine = knowledge_engine.engine(__file__)
    engine.activate('backup')
    vars, plan = engine.prove_1_goal('backup.top($ans)')
    print vars['ans']
