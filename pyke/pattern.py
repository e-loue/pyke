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

import types
import itertools

class pattern(object):
    def __ne__(self, b): return not (self == b)
    def simple_match_pattern(self, bindings, my_context, pattern_b, b_context):
	return self.match_pattern(bindings, my_context, pattern_b, b_context)
    def lookup(self, context, allow_variable_in_ans = False):
	return self

class pattern_literal(pattern):
    def __init__(self, literal):
	self.literal = literal
    def __hash__(self): return hash(self.literal)
    def __eq__(self, b):
        if isinstance(b, pattern_literal): return self.literal == b.literal
        return self.literal == b
    def match_data(self, bindings, my_context, data):
	return self.literal == data
    def match_pattern(self, bindings, my_context, pattern_b, b_context):
	if isinstance(pattern_b, pattern_literal):
	    return self.literal == pattern_b.literal
	return pattern_b.match_data(bindings, b_context, self.literal)
    def as_data(self, my_context, final = None):
	return self.literal
    def is_data(self, my_context):
	return True

class pattern_tuple(pattern):
    def __init__(self, elements, rest_var = None):
	self.elements = tuple(elements)
	self.rest_var = rest_var
    def __hash__(self):
        hash(self.elements) ^ hash(self.rest_var)
    def __eq__(self, b):
        return isinstance(b, pattern_tuple) and \
               self.elements == b.elements and self.rest_var == b.rest_var
    def match_data(self, bindings, my_context, data):
	try:
	    data = tuple(data)
	except TypeError:
	    return False
	if len(self.elements) > len(data) or \
	   self.rest_var is None and len(self.elements) < len(data):
	    return False
	for x, y in itertools.izip(self.elements, data):
	    if not x.match_data(bindings, my_context, y): return False
	if self.rest_var is not None:
            return self.rest_var.match_data(bindings, my_context,
                                            tuple(data[len(self.elements):]))
	return True
    def simple_match_pattern(self, bindings, my_context, pattern_b, b_context):
	return self, my_context
    def match_pattern(self, bindings, my_context, pattern_b, b_context):
	simple_ans = pattern_b.simple_match_pattern(bindings, b_context,
						    self, my_context)
	if isinstance(simple_ans, bool): return simple_ans
	pattern_b, b_context = simple_ans
	if not isinstance(pattern_b, pattern):
	    return self.match_data(bindings, my_context, pattern_b)
	assert isinstance(pattern_b, pattern_tuple), "Internal logic error"

	my_len = len(self.elements)
	b_len = len(pattern_b.elements)
	if pattern_b.rest_var is None and my_len > b_len or \
	   self.rest_var is None and my_len < b_len:
	    return False
	for x, y in itertools.izip(self.elements, pattern_b.elements):
	    if not x.match_pattern(bindings, my_context, y, b_context):
		return False
	if my_len <= b_len and self.rest_var is not None:
            # This is where the two rest_vars are bound together if my_len ==
            # b_len.
	    tail_val, tail_context = pattern_b._tail(my_len, b_context)
	    if tail_context is None:
		if not self.rest_var.match_data(bindings, my_context, tail_val):
		    return False
	    else:
		if not self.rest_var.match_pattern(bindings, my_context,
						   tail_val, tail_context):
		    return False
	elif pattern_b.rest_var is not None:
	    tail_val, tail_context = self._tail(b_len, my_context)
	    if tail_context is None:
		if not pattern_b.rest_var.match_data(bindings, b_context,
						     tail_val):
		    return False
	    else:
		if not pattern_b.rest_var.match_pattern(bindings, b_context,
							tail_val, tail_context):
		    return False
	return True
    def as_data(self, my_context, final = None):
	ans = tuple(x.as_data(my_context, final) for x in self.elements)
	if self.rest_var is None:
	    return ans
	else:
	    return ans + my_context.lookup_data(self.rest_var.name, final)
    def _tail(self, n, my_context):
	""" Return a copy of myself with the first n elements removed.
	"""
	if n == len(self.elements):
	    if self.rest_var is None: return (), None
	    return self.rest_var, my_context
	rest_elements = self.elements[n:]
	if self.rest_var is None and \
	   all(itertools.imap(lambda x: isinstance(x, pattern_literal),
			      rest_elements)):
	    return tuple(x.literal for x in rest_elements), None
	return pattern_tuple(self.elements[n:], self.rest_var), my_context
    def is_data(self, my_context):
	arg_test = all(itertools.imap(lambda arg_pat:
                                          arg_pat.is_data(my_context),
                                      self.elements))
	if not arg_test or self.rest_var is None: return arg_test
	return self.rest_var.is_data(my_context)

def test():
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
