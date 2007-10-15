# special.py

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
