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
    This example shows how people are related.  The primary data (facts) that
    are used to figure everything out are in family.py.

    There are three independent rule bases that all do the same thing.  The
    fc_example rule base only uses forward-chaining rules.  The bc_example
    rule base only uses backward-chaining rules.  And the example rule base
    uses all three (though, there isn't really a need for plans, so the plans
    are pretty contrived).

    One the pyke engine is created, all the rule bases loaded and all the
    primary data established as universal facts; there are three functions
    that can be used to run each of the three rule bases: fc_test, bc_test,
    and test.
'''

from __future__ import with_statement
import contextlib
import sys

import pyke
from pyke import krb_traceback

# Compile and load .krb files in '.' directory (recursively).
engine = pyke.engine('.')

# This loads the family universal facts.
import family
family.init(engine)

def fc_test(name = 'bruce'):
    '''
        This function runs the forward-chaining example (fc_example.krb).
    '''
    engine.reset()      # Allows us to run tests multiple times.

    engine.activate('fc_example')  # Runs all applicable forward-chaining rules.

    print "doing proof"
    for (person2, relationship), plan \
     in engine.prove_n('family', 'how_related', (name,), 2):
        print "%s, %s are %s" % (name, person2, relationship)
    print
    print "done"
    engine.print_stats()

def bc_test(name = 'bruce'):
    engine.reset()      # Allows us to run tests multiple times.

    engine.activate('bc_example')

    print "doing proof"
    try:
        for (person2, relationship), plan \
         in engine.prove_n('bc_example', 'how_related', (name,), 2):
            print "%s, %s are %s" % (name, person2, relationship)
    except StandardError:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)
    print
    print "done"
    engine.print_stats()

def bc2_test(name = 'bruce'):
    engine.reset()      # Allows us to run tests multiple times.

    engine.activate('bc2_example')

    print "doing proof"
    try:
        for (person2, relationship), plan \
         in engine.prove_n('bc2_example', 'how_related', (name,), 2):
            print "%s, %s are %s" % (name, person2, relationship)
    except StandardError:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)
    print
    print "done"
    engine.print_stats()

def test(name = 'bruce'):
    engine.reset()      # Allows us to run tests multiple times.

    # Also runs all applicable forward-chaining rules.
    engine.activate('example')

    print "doing proof"
    try:
        # In this case, the relationship is returned when you run the plan.
        for (person2,), plan \
         in engine.prove_n('example', 'how_related', (name,), 1):
            print "%s, %s are %s" % (name, person2, plan())
    except StandardError:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)
    print
    print "done"
    engine.print_stats()

