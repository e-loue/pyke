# $Id$
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

# cut, fact, prove_all, gather_all

class special_knowledge_base(knowledge_base.knowledge_base):
    def __init__(self):
	super(special_knowledge_base, self).__init__('special')
    def add_fn(self, fn):
	if fn.name in self.entity_lists:
	    raise KeyError("%s.%s already exists" % (self.name, fn.name))
	self.entity_lists[fn.name] = fn

Special = special_knowledge_base()

class special_fn(knowledge_base.knowledge_entity_list):
    def __init__(self, name):
	super(special_fn, self).__init__(name)
	Special.add_fn(self)
    def lookup(self, bindings, pat_context, patterns):
	raise SyntaxError("special.%s may not be used in forward chaining "
			  "rules" % self.name)
    def prove(self, bindings, pat_context, patterns):
	raise SyntaxError("special.%s may not be used in backward chaining "
			  "rules" % self.name)

class cut(special_fn):
    def __init__(self):
	super(cut, self).__init__('cut')
    def prove(self, bindings, pat_context, patterns):
	yield
	raise rule_base.StopProof

cut()
