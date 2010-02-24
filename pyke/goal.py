# goal.py

r'''goal.compile is what you're looking for here!

EXAMPLE USAGE:

    from pyke import goal

    bruce_related_to = \
      goal.compile('bc_example.how_related(bruce, %who, @ans)')

    def main():
        with bruce_related_to(my_engine, who='thomas') as gen:
            for vars_dict, plan in gen:
                print vars_dict['ans']
'''

import itertools
from pyke import contexts
from pyke import krb_compiler

def compile(goal_str):
    return prover(*krb_compiler.compile_goal(goal_str))

class prover(object):
    def __init__(self, rb_name, goal_name, patterns, python_vars, pattern_vars):
        #print "prover", rb_name, goal_name, patterns, python_vars, pattern_vars
        self.rb_name = rb_name
        self.goal_name = goal_name
        self.patterns = patterns
        self.python_vars = python_vars
        self.pattern_vars = pattern_vars

    def prove(self, engine, **args):
        assert len(args) == len(self.python_vars), \
               "incorrect number of arguments to goal: expected %d, got %d" % \
                 (len(self.python_args), len(args))
        context = contexts.simple_context()
        for var in self.python_vars:
            context.bind(var, context, args[var])
        return producer(engine, self.rb_name, self.goal_name, self.patterns,
                        context, self.pattern_vars)

class producer(object):
    def __init__(self, engine, rb_name, goal_name, patterns, context,
                       pattern_vars):
        self.engine = engine
        self.rb_name = rb_name
        self.goal_name = goal_name
        self.patterns = patterns
        self.context = context
        self.pattern_vars = pattern_vars

    def __enter__(self):
        self.context_manager = self.engine.prove(self.rb_name, self.goal_name,
                                                 self.context, self.patterns)
        it = iter(self.context_manager.__enter__())
        return itertools.imap(self.doctor_answer, it)

    def __exit__(self, type, value, tb):
        return self.context_manager.__exit__(type, value, tb)

    def doctor_answer(self, prototype_plan):
        return dict((name, self.context.lookup_data(name))
                    for name in self.pattern_vars), \
               prototype_plan and prototype_plan.create_plan()

