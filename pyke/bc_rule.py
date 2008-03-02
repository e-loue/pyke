# $Id$
# coding=utf-8
# 
# Copyright © 2007 Bruce Frederiksen
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import functools
from pyke import fc_rule, immutable_dict

class bc_rule(fc_rule.rule):
    ''' This represents a single backward-chaining rule.  Most of its
        behavior is inherited.
    '''
    def __init__(self, name, rule_base, goal_name, bc_fn, plan_fn,
		 goal_arg_patterns, plan_vars, patterns):
	super(bc_rule, self).__init__(name, rule_base, patterns)
	self.goal_name = goal_name
        self.orig_bc_fn = bc_fn
        self.bc_fn = bc_fn
	self.plan_fn = plan_fn
	self.goal_arg_pats = goal_arg_patterns
	self.plan_vars = plan_vars
	rule_base.add_bc_rule(self)
    def goal_arg_patterns(self):
	return self.goal_arg_pats
    def make_plan(self, context, final):
	return functools.partial(self.plan_fn,
                   immutable_dict.immutable_dict(
                       (var_name, context.lookup_data(var_name, final=final))
                       for var_name in self.plan_vars))
    def trace(self):
        self.bc_fn = self.surrogate
    def surrogate(self, rule, arg_patterns, arg_context):
        print "%s.%s%s" % (rule.rule_base.root_name, rule.name,
                           tuple(arg.as_data(arg_context, True)
                                 for arg in arg_patterns))
        for prototype_plan in self.orig_bc_fn(rule, arg_patterns, arg_context):
            print "%s.%s succeeded with %s" % \
                  (rule.rule_base.root_name, rule.name,
                   tuple(arg.as_data(arg_context, True)
                         for arg in arg_patterns))
            yield prototype_plan
        print "%s.%s failed" % (rule.rule_base.root_name, rule.name)
    def untrace(self):
        self.bc_fn = self.orig_bc_fn

def test():
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
