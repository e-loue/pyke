# test.py

import sys
from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine()

def init(engine):
    def child_of(child, father, mother):
        engine.add_universal_fact('family', 'child_of', (child, father, mother))
    child_of('arthur2', 'arthur1', 'bertha_o')
    child_of('helen', 'arthur1', 'bertha_o')
    child_of('roberta', 'arthur1', 'bertha_o')

    child_of('gladis', 'john', 'bertha_c')
    child_of('sarah_r', 'john', 'bertha_c')
    child_of('alice', 'marshall1', 'bertha_c')
    child_of('edmond', 'marshall1', 'bertha_c')

init(engine)

def test():
    engine.reset()
    try:
        engine.activate('fc_forall')
    except:
        krb_traceback.print_exc()
        sys.exit(1)

