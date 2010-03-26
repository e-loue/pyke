# goal.py

r'''goal.compile is what you're looking for here!

EXAMPLE USAGE:

    from pyke import goal

    bruce_related_to = \
      goal.compile('bc_example.how_related(bruce, $who, $ans)')

    def main():
        with bruce_related_to(my_engine, who='thomas') as gen:
            for vars, plan in gen:
                print vars['ans']
'''

from __future__ import with_statement

import itertools
from pyke import contexts, knowledge_engine, krb_compiler

def compile(goal_str):
    return prover(goal_str, *krb_compiler.compile_goal(goal_str))

class prover(object):
    def __init__(self, goal_str, rb_name, goal_name, patterns, pattern_vars):
        #print "prover", rb_name, goal_name, patterns, pattern_vars
        self.goal_str = goal_str
        self.rb_name = rb_name
        self.goal_name = goal_name
        self.patterns = patterns
        self.pattern_vars = pattern_vars

    def prove(self, engine, **args):
        context = contexts.simple_context()
        for var, value in args.iteritems():
            context.bind(var, context, value)
        return producer(engine, self.rb_name, self.goal_name, self.patterns,
                        context, self.pattern_vars)

    def prove_1(self, engine, **args):
        global knowledge_engine
        try:
            # All we need is the first one!
            with self.prove(engine, **args) as it:
                return iter(it).next()
        except StopIteration:
            raise knowledge_engine.CanNotProve("Can not prove " + self.goal_str)


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

