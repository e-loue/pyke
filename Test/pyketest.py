# pyketest.py

from __future__ import with_statement
import types
import unittest
from pyke import knowledge_engine
from pyke import krb_traceback

def mk_engine(*paths):
    if isinstance(self.paths, types.StringTypes):
        self.paths = (self.paths,)
    return knowledge_engine.engine(*paths)

class pyketest(unittest.TestCase):
    # Need to set: engine
    tmp_facts = ()      # sequence of (fb_name, fact_name, fact_arg...)
    rb_names_to_activate = ('test',)
    def activate(self):
        for tmp_fact in self.tmp_facts:
            fb = tmp_fact[0]
            name = tmp_fact[1]
            args = tmp_fact[2:]
            self.tmp_fact(fb, name, *args)
        if hasattr(self, 'add_tmp_facts'): self.add_tmp_facts()
        self.engine.activate(*self.rb_names_to_activate)
    def add_fact(fb, name, *args):
        self.engine.add_universal_fact(fb, name, args)
    def tmp_fact(fb, name, *args):
        self.engine.add_case_specific_fact(fb, name, args)
    def tearDown(self):
        self.engine.reset()

class fc_tests(pyketest):
    def runTest(self):
        self.activate()

class bc_tests(pyketest):
    rb_name = None      # defaults to self.rb_names_to_activate[0]
    # Need to set: goal, num_return
    plan_args = None
    plan_kws = None
    def __init__(self, methodName = 'runTest'):
        super(bc_tests, self).__init__(methodName)
        if self.rb_name is None: self.rb_name = self.rb_names_to_activate[0]
    def setUp(self):
        try:
            self.activate()
        except:
            krb_traceback.print_exc()
            raise
    def bc_test(self, *args):
        ans = []
        with self.engine.prove_n(self.rb_name, self.goal, args,
                                 self.num_return) as gen:
            for ret_args, plan in gen:
                if plan_args is None and plan_kws is None:
                    self.assert_(plan is None, "unexpected plan")
                    ans.append(ret_args)
                else:
                    self.assert_(plan is not None, "expected plan")
                    if plan_args is None: plan_ans = plan(**plan_kws)
                    elif plan_kws is None: plan_ans = plan(*plan_args)
                    else: plan_ans = plan(*plan_args, **plan_vars)
                    ans.append((ret_args, plan_ans))
        return ans

