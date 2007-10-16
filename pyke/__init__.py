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

from __future__ import with_statement, absolute_import, division

# Must include 'special' here to get it to load and be available to the rules.
from pyke import (knowledge_base, rule_base, fact_base, pattern, contexts,
                  condensedPrint, special)

class CanNotProve(StandardError):
    pass

Variables = tuple(contexts.variable('ans_%d' % i) for i in range(10))

get_kb = knowledge_base.get
get_rb = rule_base.get
init = rule_base.init
reset = rule_base.reset

def add_universal_fact(kb_name, fact_name, args):
    return get_kb(kb_name, fact_base.fact_base) \
               .add_universal_fact(fact_name, args)

def add_case_specific_fact(kb_name, fact_name, args):
    return get_kb(kb_name, fact_base.fact_base) \
               .add_case_specific_fact(fact_name, args)

def activate(*rb_names):
    for rb_name in rb_names: get_rb(rb_name).activate()

def assert_(kb_name, entity_name, args):
    return get_kb(kb_name, fact_base.fact_base).assert_(entity_name, args)

def lookup(kb_name, entity_name, pat_context, patterns):
    return get_kb(kb_name).lookup(pat_context, pat_context,
                                  entity_name, patterns)

def prove(kb_name, entity_name, pat_context, patterns):
    return get_kb(kb_name).prove(pat_context, pat_context,
                                 entity_name, patterns)

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

def test():
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
