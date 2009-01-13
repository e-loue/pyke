# $Id$
# coding=utf-8
# 
# Copyright © 2007-2008 Bruce Frederiksen
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
    This example shows how people are related.  The primary data (facts) that
    are used to figure everything out are in family.kfb.

    There are four independent rule bases that all do the same thing.  The
    fc_example rule base only uses forward-chaining rules.  The bc_example
    rule base only uses backward-chaining rules.  The bc2_example rule base
    also only uses backward-chaining rules, but with a few optimizations that
    make it run 100 times faster than bc_example.  And the example rule base
    uses all three (though it's a poor use of plans).

    Once the pyke engine is created, all the rule bases loaded and all the
    primary data established as universal facts; there are five functions
    that can be used to run each of the three rule bases: fc_test, bc_test,
    bc2_test, test and general.
'''

from __future__ import with_statement
import contextlib
import sys
import time

from pyke import knowledge_engine, krb_traceback

# Compile and load .krb files in same directory that I'm in (recursively).
engine = knowledge_engine.engine('examples.family_relations')

def fc_test(person1 = 'bruce'):
    '''
        This function runs the forward-chaining example (fc_example.krb).
    '''
    engine.reset()      # Allows us to run tests multiple times.

    start_time = time.time()
    engine.activate('fc_example')  # Runs all applicable forward-chaining rules.
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time

    print "doing proof"
    with engine.prove_n('family', 'how_related', (person1,), 2) as gen:
        for (person2, relationship), plan in gen:
            print "%s, %s are %s" % (person1, person2, relationship)
    prove_time = time.time() - fc_end_time
    print
    print "done"
    engine.print_stats()
    print "fc time %.2f, %.0f asserts/sec" % \
          (fc_time, engine.get_kb('family').get_stats()[2] / fc_time)

def bc_test(person1 = 'bruce'):
    engine.reset()      # Allows us to run tests multiple times.

    start_time = time.time()
    engine.activate('bc_example')
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time

    print "doing proof"
    try:
        with engine.prove_n('bc_example', 'how_related', (person1,), 2) as gen:
            for (person2, relationship), plan in gen:
                print "%s, %s are %s" % (person1, person2, relationship)
    except StandardError:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)
    prove_time = time.time() - fc_end_time
    print
    print "done"
    engine.print_stats()
    print "bc time %.2f, %.0f goals/sec" % \
          (prove_time, engine.get_kb('bc_example').num_prove_calls / prove_time)

def bc2_test(person1 = 'bruce'):
    engine.reset()      # Allows us to run tests multiple times.

    start_time = time.time()
    engine.activate('bc2_example')
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time

    print "doing proof"
    try:
        with engine.prove_n('bc2_example', 'how_related', (person1,), 2) as gen:
            for (person2, relationship), plan in gen:
                print "%s, %s are %s" % (person1, person2, relationship)
    except StandardError:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)
    prove_time = time.time() - fc_end_time
    print
    print "done"
    engine.print_stats()
    print "bc time %.2f, %.0f goals/sec" % \
          (prove_time,
           engine.get_kb('bc2_example').num_prove_calls / prove_time)

def test(person1 = 'bruce'):
    engine.reset()      # Allows us to run tests multiple times.

    # Also runs all applicable forward-chaining rules.
    start_time = time.time()
    engine.activate('example')
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time

    print "doing proof"
    try:
        # In this case, the relationship is returned when you run the plan.
        with engine.prove_n('example', 'how_related', (person1,), 1) as gen:
            for (person2,), plan in gen:
                print "%s, %s are %s" % (person1, person2, plan())
    except StandardError:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)
    prove_time = time.time() - fc_end_time
    print
    print "done"
    engine.print_stats()
    print "fc time %.2f, %.0f asserts/sec" % \
          (fc_time, engine.get_kb('family').get_stats()[2] / fc_time)
    print "bc time %.2f, %.0f goals/sec" % \
          (prove_time, engine.get_kb('example').num_prove_calls / prove_time)
    print "total time %.2f" % (fc_time + prove_time)

# Need some extra goodies for general()...
from pyke import contexts, pattern

def general(person1 = None, person2 = None, relationship = None):

    engine.reset()      # Allows us to run tests multiple times.

    start_time = time.time()
    engine.activate('bc2_example')      # same rule base as bc2_test()
    fc_end_time = time.time()
    fc_time = fc_end_time - start_time

    print "doing proof"
    top_context = contexts.simple_context()
    if person1: arg1 = pattern.pattern_literal(person1)
    else: arg1 = contexts.variable('person1')
    if person2: arg2 = pattern.pattern_literal(person2)
    else: arg2 = contexts.variable('person2')
    if relationship: arg3 = make_pattern(relationship)
    else: arg3 = contexts.variable('relationship')
    try:
        with engine.prove('bc2_example', 'how_related', top_context,
                          (arg1, arg2, arg3)) \
          as gen:
            for prototype_plan in gen:
                print "%s, %s are %s" % (arg1.as_data(top_context),
                                         arg2.as_data(top_context),
                                         arg3.as_data(top_context))
    except StandardError:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)
    prove_time = time.time() - fc_end_time
    print
    print "done"
    engine.print_stats()
    print "bc time %.2f, %.0f goals/sec" % \
          (prove_time,
           engine.get_kb('bc2_example').num_prove_calls / prove_time)

import types

def make_pattern(x):
    if isinstance(x, types.StringTypes):
        if x[0] == '$': return contexts.variable(x[1:])
        return pattern.pattern_literal(x)
    if isinstance(x, (tuple, list)):
        return pattern.pattern_tuple(tuple(make_pattern(element)
                                             for element in x))
    return pattern.pattern_literal(x)
