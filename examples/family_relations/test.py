# test.py

from __future__ import with_statement
import cPickle as pickle
import copy_reg
import contextlib
import functools

import family
#import example
import example_bc
from pyke import knowledge_base, rule_base, contexts, pattern, special

rule_base.init()

family = knowledge_base.get('family')
example = rule_base.get('example')

patterns = (pattern.pattern_literal('bruce'), contexts.variable('who'))

# To be able to pickle plans.  (Not needed to unpickle).
copy_reg.pickle(functools.partial,
		lambda p: (functools.partial, (p.func,) + p.args))

def test():
    global plan
    rule_base.reset()

    context = contexts.simple_context()

    #print "family: universal_facts:"
    #family.dump_universal_facts()
    #print

    #print "family: case_specific_facts:"
    #family.dump_specific_facts()
    #print

    example.activate()

    #print "family: universal_facts:"
    #family.dump_universal_facts()
    #print

    #print "family: case_specific_facts:"
    #family.dump_specific_facts()
    #print

    #print "get_rule_lists_for test:"
    #for ans in example.gen_rule_lists_for('how_related'):
    #    print "how_related:", ans
    #print

    test_pickle = False
    print "doing proof"
    # prove(bindings, pat_context, goal_name, patterns)
    for ans in example.prove(context, context, 'how_related', patterns):
	#print "prove:", ans
        print [pat.as_data(context) for pat in patterns]
	#print "making plan"
	plan = ans.create_plan()
	#print "plan:", plan
	if test_pickle:
	    print "pickling plan"
	    with contextlib.closing(file('plan_pickle', 'w')) as f:
		pickle.dump(plan, f)
	#print "executing plan"
	print "plan ->", plan()
    print

    print "done"

