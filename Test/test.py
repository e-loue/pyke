# test.py

from __future__ import with_statement
import sys
import types
from pyke import knowledge_engine
from pyke import krb_traceback

def init(*paths):
    global Engine
    Engine = knowledge_engine.engine(*paths)

def add_fact(fb, name, *args):
    Engine.add_universal_fact(fb, name, args)

def tmp_fact(fb, name, *args):
    Engine.add_case_specific_fact(fb, name, args)

def fc_test(*rb_names):
    Engine.reset()
    try:
        for rb_name in rb_names:
            Engine.activate(rb_name)
    except:
        krb_traceback.print_exc()
        sys.exit(1)

def bc_test(rb_names, goal, num_return, args = (), rb_name = None,
            plan_args = None, plan_kws = None):
    Engine.reset()
    try:
        if isinstance(rb_names, types.StringTypes): rb_names = (rb_names,)
        for rb_name in rb_names:
            Engine.activate(rb_name)
        if rb_name is None: rb_name = rb_names[0]
        with Engine.prove_n(rb_name, goal, args, num_return) as gen:
            for ret_args, plan in gen:
                first = True
                for ret_arg in ret_args:
                    if first: first = False
                    else: print ",",
                    print ret_arg,
                print
                if plan_args is None and plan_kws is None:
                    assert plan is None, "unexpected plan"
                else:
                    assert plan is not None, "expected plan"
                    print "plan:"
                    if plan_args is None: ans = plan(**plan_kws)
                    elif plan_kws is None: ans = plan(*plan_args)
                    else: ans = plan(*plan_args, **plan_vars)
                    if ans is not None: print ans
    except:
        krb_traceback.print_exc()
        sys.exit(1)

