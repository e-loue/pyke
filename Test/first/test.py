# test.py

from Test import pyketest

Engine = pyketest.mk_engine()

class fc_tests(pyketest.fc_tests):
    engine = Engine
