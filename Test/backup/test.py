# test.py

import os.path
from pyke import knowledge_engine

def test():
    engine = knowledge_engine.engine(os.path.dirname(__file__),
                                     'Test.backup.compiled_krb')
    engine.activate('backup')
    (ans,), plan = engine.prove_1('backup', 'top', (), 1)
    print ans
