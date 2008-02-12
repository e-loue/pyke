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

from pyke import knowledge_base, rule_base

# claim_goal, fact, prove_all, gather_all

class special_knowledge_base(knowledge_base.knowledge_base):
    def __init__(self, engine):
	super(special_knowledge_base, self).__init__(engine, 'special')
    def add_fn(self, fn):
	if fn.name in self.entity_lists:
	    raise KeyError("%s.%s already exists" % (self.name, fn.name))
	self.entity_lists[fn.name] = fn

class special_fn(knowledge_base.knowledge_entity_list):
    def __init__(self, special_base, name):
	super(special_fn, self).__init__(name)
	special_base.add_fn(self)
    def lookup(self, bindings, pat_context, patterns):
	raise SyntaxError("special.%s may not be used in forward chaining "
			  "rules" % self.name)
    def prove(self, bindings, pat_context, patterns):
	raise SyntaxError("special.%s may not be used in backward chaining "
			  "rules" % self.name)

class claim_goal(special_fn):
    def __init__(self, special_base):
	super(claim_goal, self).__init__(special_base, 'claim_goal')
    def prove(self, bindings, pat_context, patterns):
	yield
	raise rule_base.StopProof

def create_for(engine):
    special_base = special_knowledge_base(engine)
    claim_goal(special_base)

def test():
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
