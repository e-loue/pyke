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
import contextlib
import os.path
import re
import sys

# FIX: Take this out:
use_test = False

# If set, doesn't delete output files on error.
no_nuke = True

import pyke

if use_test:
    from pyke.compiler import compiler_test_bc
else:
    from pyke.compiler import compiler_bc
from pyke.compiler import krbparser

#from pyke import contexts
#contexts.debug = ('patterns_out1', 'patterns_out',)

pyke.init()

Ast_names = frozenset((
    'file',
    'parent',
    'fc_rule',
    'fc_predicate',
    'assert',
    'python_assertion',
    'python_eq',
    'python_in',
    'python_check',
    'counting',
    'bc_rule',
    'goal',
    'bc_predicate',
    'symbol',
    'pattern_var',
    'as',
    'plan_spec',
    'pattern_data',
    'pattern_tuple',
  # 'anonymous_var',
))

def dump(ast, f = sys.stderr, need_nl = False, indent = 0):
    if not isinstance(ast, tuple) or len(ast) == 0:
        f.write(repr(ast))
        return False
    if ast[0] in Ast_names:
        indent += 2
        if need_nl:
            f.write("\n")
            f.write(' ' * indent) 
        f.write('(%s' % ast[0])
        for arg in ast[1:]:
            f.write(', ')
            dump(arg, f, True, indent)
        f.write(')')
        return True
    f.write('(')
    did_nl = dump(ast[0], f, False, indent)
    for arg in ast[1:]:
        f.write(', ')
        did_nl |= dump(arg, f, did_nl, indent)
    f.write(')')
    return did_nl

Name_test = re.compile(r'[a-zA-Z_][a-zA-Z0-9_]*$')

def compile(filename):
    rb_name = os.path.basename(filename)
    if not rb_name.endswith('.krb'):
        raise ValueError("compile: filename, %s, must end with .krb" % filename)
    rb_name = rb_name[:-4]
    if not Name_test.match(rb_name):
        raise ValueError("compile: %s illegal as python identifier" % rb_name)
    base_path = filename[:-4]
    bc_path = base_path + '_bc.py'
    plan_path = base_path + '.py'
    try:
        ast = krbparser.parse(filename)
        sys.stderr.write("got ast\n")
        # dump(ast)
        # sys.stderr.write('\n\n')
        pyke.reset()
        if use_test:
            pyke.activate('compiler_test')
            (plan_lines, bc_lines), plan = \
                pyke.prove_1('compiler_test', 'compile', (rb_name, ast), 2)
        else:
            pyke.activate('compiler')
            (plan_lines, bc_lines), plan = \
                pyke.prove_1('compiler', 'compile', (rb_name, ast), 2)
        sys.stderr.write("writing bc_lines\n")
        write_file(bc_lines, bc_path)
        sys.stderr.write("writing plan_lines\n")
        #sys.stderr.write("plan_lines:\n")
        #for line in plan_lines:
        #    sys.stderr.write("  " + repr(line) + "\n")
        write_file(plan_lines, plan_path)
        sys.stderr.write("done!\n")
    except:
        if os.path.lexists(bc_path) and not no_nuke: os.remove(bc_path)
        if os.path.lexists(plan_path) and not no_nuke: os.remove(plan_path)
        raise

def write_file(lines, filename):
    with contextlib.closing(file(filename, 'w')) as f:
        indents = [0]
        write_file2(lines, f, indents)

def write_file2(lines, f, indents):
    for line in lines:
        if line == 'POPINDENT':
            assert len(indents) > 1
            del indents[-1]
        elif isinstance(line, tuple):
            if len(line) == 2 and line[0] == 'INDENT':
                indents.append(indents[-1] + line[1])
            else:
                write_file2(line, f, indents)
        else:
            f.write(' ' * indents[-1] + line + '\n')

def test():
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
