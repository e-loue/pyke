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

'''
    Forward chaining rules (fc_rule) are one of two types of rules in a
    rule_base (the other being backward chaining rules -- bc_rule).

    All forward chaining is done automatically as each rule_base is
    activated.  This is done in two steps:

        1.  All fc_rules are registered with the fact_lists referenced in
            their 'foreach' clause by calling fc_rule.register_rule() on
            each fc_rule (including the parent rule_base's fc_rules).

            This will cause the fact_list to invoke fc_rule.new_fact each time
            a new fact for that fact_list (by that name) is asserted (by the
            same or another fc_rule).

        2.  The fc_rule.run() function is called on each fc_rule (including
            the parent rule_base's fc_rules).

    The forward chaining rule is compiled into a python function which does
    the actual inferencing work for both the 'run' case and the 'new_fact'
    case, depending on the arguments passed to it.  Each fc_rule object
    remembers its associated compiled python function.

    The fc_rule object tracks the progress of the forward chaining for that
    rule.  If the rule has not been run yet, it ignores new_facts since it
    will see the new fact when it is later run.

'''

from pyke import contexts

import itertools

class rule(object):
    ''' Common to both fc_rules and bc_rules. '''
    def __init__(self, name, rule_base, patterns):
        self.name = name
        self.rule_base = rule_base
        self.patterns = patterns
    def __repr__(self):
        return "<%s %s>" % (self.__class__.__name__, self.name)
    def pattern(self, pattern_index):
        return self.patterns[pattern_index]

class fc_rule(rule):
    def __init__(self, name, rule_base, rule_fn, foreach_facts, patterns):
        super(fc_rule, self).__init__(name, rule_base, patterns)
        rule_base.add_fc_rule(self)
        self.rule_fn = rule_fn
        self.foreach_facts = foreach_facts # (kb_name, fact_name, arg_pats)...
        self.ran = False
    def register_rule(self):
        for i, (kb_name, fact_name, arg_patterns) \
         in enumerate(self.foreach_facts):
            self.rule_base.engine.get_kb(kb_name) \
                .add_fc_rule_ref(fact_name, self, i)
    def reset(self):
        self.ran = False
    def run(self):
        self.ran = True
        self.rule_fn(self)
    def new_fact(self, fact_args, n):
        if self.ran:
            arg_patterns = self.foreach_facts[n][2]
            if len(fact_args) == len(arg_patterns):
                context = contexts.simple_context()
                if all(itertools.imap(lambda pat, arg:
                                          pat.match_data(context, context, arg),
                                      arg_patterns,
                                      fact_args)):
                    self.rule_base.num_fc_rules_rerun += 1
                    self.rule_fn(self, context, n)
                context.done()
    def foreach_patterns(self, foreach_index):
        return self.foreach_facts[foreach_index][2]

def test():
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
