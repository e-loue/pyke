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

from pyke import tmp_itertools as itertools
from pyke import knowledge_base

class StopProof(Exception): pass

class stopIterator(object):
    def __init__(self, rule_base, iterator):
        self.rule_base = rule_base
        self.iterator = iter(iterator)
    def __iter__(self): return self
    def next(self):
        if self.iterator:
            try:
                return self.iterator.next()
            except StopProof:
                self.iterator = None
                self.rule_base.num_bc_rule_failures += 1
        raise StopIteration

class rule_base(knowledge_base.knowledge_base):
    def __init__(self, engine, name, parent = None, exclude_list = ()):
        super(rule_base, self).__init__(engine, name, rule_list, False)
        if name in engine.rule_bases:
            raise AssertionError("rule_base %s already exists" % name)
        if name in engine.knowledge_bases:
            raise AssertionError("name clash between rule_base '%s' and "
                                 "fact_base '%s'" % (name, name))
        engine.rule_bases[name] = self
        self.fc_rules = []
        self.parent = parent
        self.exclude_set = frozenset(exclude_list)
        self.rules = {}         # {name: rule}
    def add_fc_rule(self, fc_rule):
        if fc_rule.name in self.rules:
            raise AssertionError("%s rule_base: duplicate rule name: %s" %
                                 (self.name, fc_rule.name))
        self.rules[fc_rule.name] = fc_rule
        self.fc_rules.append(fc_rule)
    def add_bc_rule(self, bc_rule):
        if bc_rule.name in self.rules:
            raise AssertionError("%s rule_base: duplicate rule name: %s" %
                                 (self.name, bc_rule.name))
        self.rules[bc_rule.name] = bc_rule
        self.get_entity_list(bc_rule.goal_name).add_bc_rule(bc_rule)
    def init2(self):
        if not self.initialized:
            self.initialized = True
            if self.parent:
                parent = self.engine.rule_bases.get(self.parent)
                if parent is None:
                    raise KeyError("rule_base %s: parent %s not found" % \
                                   (self.name, self.parent))
                self.parent = parent
                self.parent.init2()
                self.root_name = self.parent.root_name
            else:
                self.root_name = self.name
            self.reset()
    def derived_from(self, rb):
        parent = self.parent
        while parent:
            if parent == rb: return True
            parent = parent.parent
        return False
    def register_fc_rules(self, stop_at_rb):
        rb = self
        while rb is not stop_at_rb:
            for fc_rule in rb.fc_rules: fc_rule.register_rule()
            if not rb.parent: break
            rb = rb.parent
    def run_fc_rules(self, stop_at_rb):
        rb = self
        while rb is not stop_at_rb:
            for fc_rule in rb.fc_rules: fc_rule.run()
            if not rb.parent: break
            rb = rb.parent
    def activate(self):
        current_rb = self.engine.knowledge_bases.get(self.root_name)
        if current_rb:
            assert self.derived_from(current_rb), \
                   "%s.activate(): not derived from current rule_base, %s" % \
                   (self.name, current_rb.name)
        self.engine.knowledge_bases[self.root_name] = self
        self.register_fc_rules(current_rb)
        self.run_fc_rules(current_rb)
    def reset(self):
        if self.root_name in self.engine.knowledge_bases:
            del self.engine.knowledge_bases[self.root_name]
        for fc_rule in self.fc_rules: fc_rule.reset()
        self.num_fc_rules_triggered = 0
        self.num_fc_rules_rerun = 0
        self.num_prove_calls = 0
        self.num_bc_rules_matched = 0
        self.num_bc_rule_successes = 0
        self.num_bc_rule_failures = 0
    def gen_rule_lists_for(self, goal_name):
        rule_base = self
        while True:
            rl = rule_base.entity_lists.get(goal_name)
            if rl: yield rl
            if rule_base.parent and goal_name not in rule_base.exclude_set:
                rule_base = rule_base.parent
            else:
                break
    def prove(self, bindings, pat_context, goal_name, patterns):
        self.num_prove_calls += 1
        return stopIterator(self,
                   itertools.chain(
                       rl.prove(bindings, pat_context, patterns)
                       for rl in self.gen_rule_lists_for(goal_name)))
    def print_stats(self, f):
        f.write("%s: %d fc_rules, %d triggered, %d rerun\n" %
                (self.name, len(self.fc_rules), self.num_fc_rules_triggered,
                 self.num_fc_rules_rerun))
        num_bc_rules = sum(rule_list.num_bc_rules()
                             for rule_list in self.entity_lists.itervalues())
        f.write("%s: %d bc_rules, %d goals, %d rules matched\n" %
                (self.name, num_bc_rules, self.num_prove_calls,
                 self.num_bc_rules_matched))
        f.write("%s  %d successes, %d failures\n" %
                (' ' * len(self.name), self.num_bc_rule_successes,
                 self.num_bc_rule_failures))
        if self.parent: self.parent.print_stats(f)
    def trace(self, rule_name):
        for rule_list in self.entity_lists.itervalues():
            if rule_list.trace(rule_name): return
        raise KeyError("trace: rule %s not found" % rule_name)
    def untrace(self, rule_name):
        for rule_list in self.entity_lists.itervalues():
            if rule_list.untrace(rule_name): return
        raise KeyError("untrace: rule %s not found" % rule_name)

class rule_list(knowledge_base.knowledge_entity_list):
    def __init__(self, name):
        self.name = name
        self.bc_rules = []
    def add_bc_rule(self, bc_rule):
        self.bc_rules.append(bc_rule)
    def prove(self, bindings, pat_context, patterns):
        """ Binds patterns to successive facts, yielding None for each
            successful match.  Undoes bindings upon continuation, so that no
            bindings remain at StopIteration.
        """
        return itertools.chain(bc_rule.bc_fn(bc_rule, patterns, pat_context)
                               for bc_rule in self.bc_rules)
    def num_bc_rules(self):
        return len(self.bc_rules)
    def trace(self, rule_name):
        for bc_rule in self.bc_rules:
            if bc_rule.name == rule_name:
                bc_rule.trace()
                return True
        return False
    def untrace(self, rule_name):
        for bc_rule in self.bc_rules:
            if bc_rule.name == rule_name:
                bc_rule.untrace()
                return True
        return False

def test():
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
