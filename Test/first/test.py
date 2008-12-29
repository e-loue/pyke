# test.py

import os.path
from Test import pyketest

Engine = knowledge_engine.engine(os.path.dirname(__file__),
                                 'Test.first.compiled_krb')

class fc_tests(pyketest.fc_tests):
    engine = Engine
