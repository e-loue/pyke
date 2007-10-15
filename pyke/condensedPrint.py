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

import sys
import types
import re

def cprint(obj, maxlen = 80, maxdepth = 4, maxlines = 20):
    items = cprint2(obj, maxdepth)
    #sys.stderr.write("cprint items: %s\n" % str(items))
    return format(items, maxlen, maxlen, maxlines)[0]

def format_len(x):
    """
	>>> format_len('abc')
	3
	>>> format_len(('(', ('(', 'def', ')'), 'yz', ')'))
	11
    """
    if not isinstance(x, (list, tuple)): return len(x)
    if len(x) > 3: sep_len = 2 * (len(x) - 3)
    else: sep_len = 0
    return reduce(lambda total, next: total + format_len(next), x, 0) + sep_len

def format(x, lenleft, maxlen, maxlines, indent = 0):
    r"""
	>>> format('"hello mom this is a long str"', 7, 80, 9)
	('"he..."', 0)
	>>> format(('(', 'a', 'b', 'c', ')'), 80, 80, 9)
	('(a, b, c)', 0)
	>>> format(('(', 'a', 'b', 'c', ')'), 8, 80, 9)
	('(a,\n  b,\n  c)', 2)
    """
    if not isinstance(x, (list, tuple)):
	if len(x) <= lenleft: return x, 0
	if lenleft >= 5: return x[:lenleft-4] + '...' + x[-1], 0
	return '&', 0
    if len(x) == 0: return '', 0
    if format_len(x) <= lenleft:
	return x[0] + \
	       ', '.join(format(y, lenleft, maxlen, maxlines)[0]
		           for y in x[1:-1]) + \
	       x[-1], 0
    indent += 2
    ans = x[0]
    lines_taken = 0
    if len(x) > 2:
	first, taken = \
	    format(x[1], lenleft - len(ans), maxlen, maxlines, indent + 2)
	ans += first
	lines_taken += taken
	for y in x[2:-1]:
	    if lines_taken >= maxlines:
		ans += ', ...'
		break
	    line, taken = \
		format(y, maxlen - indent, maxlen, maxlines - lines_taken,
		       indent)
	    ans += ',\n' + indent * ' ' + line
	    lines_taken += taken + 1
    return ans + x[-1], lines_taken

def cprint2(obj, maxdepth):
    if isinstance(obj, types.TupleType):
	return printSeq('(', ')', obj, maxdepth)
    if isinstance(obj, types.ListType):
	return printSeq('[', ']', obj, maxdepth)
    if isinstance(obj, types.DictType):
	return printDict(obj, maxdepth)
    if isinstance(obj, types.StringTypes):
	return printStr(obj)
    try:
	return str(obj)
    except StandardError, e:
	exc_type, exc_value, exc_traceback = sys.exc_info()
	import traceback
	if isinstance(obj, types.InstanceType): obj_type = obj.__class__
	else: obj_type = type(obj)
	return "While trying to cprint a %s, got: %s" % (obj_type, traceback.format_exception_only(exc_type, exc_value))

str_chk = re.compile('[a-zA-Z_][a-zA-Z0-9_]*$')

def printStr(str):
    """
	>>> printStr('hello_34_A')
	'hello_34_A'
	>>> printStr('hello 34_A')
	"'hello 34_A'"
    """
    if str_chk.match(str): return str
    return repr(str)

def printSeq(startChar, endChar, seq, maxdepth):
    """
	>>> printSeq('(', ')', (1, 2, 3), 4)
	['(', '1', '2', '3', ')']
	>>> printSeq('(', ')', (), 4)
	['(', ')']
    """
    if maxdepth < 1: return '&'
    maxdepth -= 1
    return [startChar] + [cprint2(x, maxdepth) for x in seq] + [endChar]

def item(key, value, maxdepth, separator):
    """
	>>> item('hello', 'bob', 3, '=')
	'hello=bob'
	>>> item(('hello', 'there'), 'bob', 3, '=')
	['(', 'hello', 'there', ')=bob']
	>>> item('hello', ('extra', 'bob'), 3, '=')
	['hello=(', 'extra', 'bob', ')']
	>>> item(('hello', 'there'), ('extra', 'bob'), 3, '=')
	['(', 'hello', 'there', ')=(', 'extra', 'bob', ')']
    """
    keyans = cprint2(key, maxdepth)
    valans = cprint2(value, maxdepth)
    if isinstance(keyans, list):
	keyans[-1] += separator
	if isinstance(valans, list):
	    keyans[-1] += valans[0]
	    keyans.extend(valans[1:])
	else:
	    keyans[-1] += valans
	return keyans
    if isinstance(valans, list):
	valans[0] = keyans + separator + valans[0]
	return valans
    return keyans + separator + valans

def printDict(dict, maxdepth,
		    startChar = '{', endChar = '}', separator = ': '):
    """
	>>> printDict({1:2, 3:4, 5:(6,7)}, 5)
	['{', '1: 2', '3: 4', ['5: (', '6', '7', ')'], '}']
	>>> printDict({}, 5)
	['{', '}']
    """
    if maxdepth < 1: return '&'
    maxdepth -= 1
    keys = dict.keys()
    keys.sort()
    return [startChar] + \
	   [item(key, dict[key], maxdepth, separator) for key in keys] + \
	   [endChar]

def test():
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()

