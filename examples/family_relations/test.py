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

from __future__ import with_statement
import cPickle as pickle
import copy_reg
import contextlib
import functools

# This causes the family universal facts to be loaded as a byproduct of the
# import.
import family

#import example
import example_bc
import pyke

pyke.init()

# To be able to pickle plans.  (Not needed to unpickle).
copy_reg.pickle(functools.partial,
		lambda p: (functools.partial, (p.func,) + p.args))

def test():
    global plan
    pyke.reset()

    #family = pyke.get_kb('family')

    #print "family: universal_facts:"
    #family.dump_universal_facts()
    #print

    #print "family: case_specific_facts:"
    #family.dump_specific_facts()
    #print

    pyke.activate('example')

    #print "family: universal_facts:"
    #family.dump_universal_facts()
    #print

    #print "family: case_specific_facts:"
    #family.dump_specific_facts()
    #print

    test_pickle = False
    print "doing proof"
    for (ans,), plan in pyke.prove_n('example', 'how_related', ('bruce',), 1):
	#print "prove:", ans
        print "bruce,", ans
	#print "plan:", plan
	if test_pickle:
	    print "pickling plan"
	    with contextlib.closing(file('plan_pickle', 'w')) as f:
		pickle.dump(plan, f)
	#print "executing plan"
	print "plan ->", plan()
    print

    print "done"

