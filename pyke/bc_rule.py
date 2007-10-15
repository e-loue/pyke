# bc_rule.py

from __future__ import with_statement, absolute_import, division
import functools
from pyke import fc_rule

class bc_rule(fc_rule.rule):
    ''' This represents a single backward-chaining rule.  Most of it's
        behavior is inherited.
    '''
    def __init__(self, name, rule_base, goal_name, bc_fn, plan_fn,
		 goal_arg_patterns, plan_vars, patterns):
	super(bc_rule, self).__init__(name, rule_base, patterns)
	self.goal_name = goal_name
	self.bc_fn = bc_fn
	self.plan_fn = plan_fn
	self.goal_arg_pats = goal_arg_patterns
	self.plan_vars = plan_vars
	rule_base.add_bc_rule(self)
    def goal_arg_patterns(self):
	return self.goal_arg_pats
    def make_plan(self, context, final):
	return functools.partial(self.plan_fn,
				 dict((var_name, context.lookup_data(var_name,
								     final))
				      for var_name in self.plan_vars))

def test():
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
