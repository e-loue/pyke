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

from __future__ import with_statement, absolute_import, division
from pyke import pattern, contexts, condensedPrint

Knowledge_bases = {}
Variables = tuple(contexts.variable('ans_%d' % i) for i in range(10))

class CanNotProve(StandardError):
    pass

def get(kb_name):
    ans = Knowledge_bases.get(kb_name)
    if ans is None: raise KeyError("knowledge_base: %s not found" % kb_name)
    return ans

def assert_(kb_name, entity_name, args):
    return get(kb_name).assert_(entity_name, args)

def lookup(kb_name, entity_name, pat_context, patterns):
    return get(kb_name).lookup(pat_context, pat_context, entity_name, patterns)

def prove(kb_name, entity_name, pat_context, patterns):
    return get(kb_name).prove(pat_context, pat_context, entity_name, patterns)

def prove_n(kb_name, entity_name, fixed_args, num_returns):
    context = contexts.simple_context()
    vars = Variables[:num_returns]
    try:
        prove(kb_name, entity_name, context,
              tuple(pattern.pattern_literal(arg)
                    for arg in fixed_args) + vars) \
         .next()
    except StopIteration:
        raise CanNotProve("Can not prove %s.%s%s" %
                              (kb_name, entity_name,
                               condensedPrint.cprint(fixed_args + vars)))
    ans = tuple(context.lookup_data(var.name) for var in vars)
    context.done()
    return ans

class knowledge_base(object):
    ''' This object is a master repository for knowledge entities of different
	names.  These knowledge entities could be facts or rules.  The
	cumulative information maintained in a knowledge_base represents all
	knowledge within a specific domain.
	
	In the syntax: "name1.name2(arg_pattern...)", the knowledge_base name
	is "name1".
    '''
    def __init__(self, name, entity_list_type = None, register = True):
	self.name = name
	if register:
	    if name in Knowledge_bases:
		raise AssertionError("knowledge_base %s already exists" % name)
	    Knowledge_bases[name] = self
	self.entity_lists = {}		# {name: entity_list}
	self.entity_list_type = entity_list_type
	self.initialized = False	# used by self.init2
    def init2(self):
	''' overridden by subclasses. '''
	pass
    def reset(self):
	for entity in self.entity_lists.itervalues(): entity.reset()
    def __repr__(self): return "<%s %s>" % (self.__class__.__name__, self.name)
    def get_entity_list(self, entity_name):
	ans = self.entity_lists.get(entity_name)
	if ans is None:
	    if self.entity_list_type:
		ans = self.entity_lists[entity_name] \
		    = self.entity_list_type(entity_name)
	    else:
		raise KeyError("%s not found in knowledge_base %s" %
			       (entity_name, self.name))
	return ans
    def lookup(self, bindings, pat_context, entity_name, patterns):
	entity = self.entity_lists.get(entity_name)
	if entity is None: return ()
	return entity.lookup(bindings, pat_context, patterns)
    def prove(self, bindings, pat_context, entity_name, patterns):
	entity = self.entity_lists.get(entity_name)
	if entity is None: return ()
	return entity.prove(bindings, pat_context, patterns)
    def add_fc_rule_ref(self, entity_name, fc_rule, foreach_index):
	self.entity_lists[entity_name].add_fc_rule_ref(fc_rule, foreach_index)

class knowledge_entity_list(object):
    ''' This object keeps track of all of the knowledge entities sharing the
	same name.  For example, these knowledge entities could be all the
	facts of the same name or all of the rules of the same name.
	Generally, all of the entities in this list may come to bear on
	looking up or proving a single fact or goal.

	In the syntax: "name1.name2(arg_pattern...)", the knowledge entity
	name is "name2".
    '''
    def __init__(self, name):
	self.name = name
    def __repr__(self): return "<%s %s>" % (self.__class__.__name__, self.name)
    def reset(self):
        pass
    def prove(self, bindings, pat_context, patterns):
	return self.lookup(bindings, pat_context, patterns)
    def add_fc_rule_ref(self, fc_rule, foreach_index):
	pass

def test():
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
