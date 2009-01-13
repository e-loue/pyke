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

from __future__ import with_statement
import os, os.path
import sys

import pyke
from pyke import knowledge_engine

from pyke.krb_compiler import compiler_bc
from pyke.krb_compiler import krbparser

#from pyke import contexts
#contexts.debug = ('patterns_out1', 'patterns_out',)

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

def to_relative(from_path, to_path):
    '''
        >>> to_relative('/a/b/c', '/a/b/d/e')
        '../d/e'
        >>> to_relative('/a/b/c', '/b/d/e')
        '/b/d/e'
        >>> to_relative('/a/b/c', '/a/b/c/e')
        'e'
    '''
    from_path = os.path.abspath(from_path)
    to_path = os.path.abspath(to_path)
    prefix = ''
    while os.path.join(from_path, to_path[len(from_path) + 1:]) != to_path:
        new_from_path = os.path.dirname(from_path)
        if new_from_path == from_path: return to_path
        from_path = new_from_path
        prefix = os.path.join(prefix, '..')
    return os.path.join(prefix, to_path[len(from_path) + 1:])

def compile_krb(rb_name, generated_root_pkg, generated_root_dir, filename):
    engine = knowledge_engine.engine(('*direct*', compiler_bc))
    try:
        fc_name = rb_name + '_fc.py'
        bc_name = rb_name + '_bc.py'
        plan_name = rb_name + '_plans.py'
        fc_path = os.path.join(generated_root_dir, fc_name)
        bc_path = os.path.join(generated_root_dir, bc_name)
        plan_path = os.path.join(generated_root_dir, plan_name)
        ast = krbparser.parse(krbparser, filename)
        #sys.stderr.write("got ast\n")
        # dump(ast)
        # sys.stderr.write('\n\n')
        engine.reset()
        engine.activate('compiler')
        (fc_lines, bc_lines, plan_lines), plan = \
            engine.prove_1('compiler', 'compile',
                           (generated_root_pkg, rb_name, ast), 3)
        krb_filename = to_relative(generated_root_dir, filename)
        ans = []
        if fc_lines:
            sys.stderr.write("writing [%s]/%s\n" %
                               (generated_root_pkg, os.path.basename(fc_path)))
            write_file(fc_lines +
                       ("",
                        "Krb_filename = %r" % krb_filename,),
                       fc_path)
            ans.append(fc_name)
        elif os.path.lexists(fc_path): os.remove(fc_path)
        if bc_lines:
            sys.stderr.write("writing [%s]/%s\n" %
                               (generated_root_pkg, os.path.basename(bc_path)))
            write_file(bc_lines +
                       ("",
                        "Krb_filename = %r" % krb_filename,),
                       bc_path)
            ans.append(bc_name)
        elif os.path.lexists(bc_path): os.remove(bc_path)
        if plan_lines:
            sys.stderr.write("writing [%s]/%s\n" %
                               (generated_root_pkg,
                                os.path.basename(plan_path)))
            #sys.stderr.write("plan_lines:\n")
            #for line in plan_lines:
            #    sys.stderr.write("  " + repr(line) + "\n")
            write_file(plan_lines +
                       ("",
                        "Krb_filename = %r" % krb_filename,),
                       plan_path)
            ans.insert(len(ans) - 1, plan_name)  # want this loaded before _bc
        elif os.path.lexists(plan_path): os.remove(plan_path)
        #sys.stderr.write("done!\n")
        return ans
    except:
        if os.path.lexists(fc_path): os.remove(fc_path)
        if os.path.lexists(bc_path): os.remove(bc_path)
        if os.path.lexists(plan_path): os.remove(plan_path)
        raise

def compile_kfb(filename):
    global kfbparser
    try:
        kfbparser
    except NameError:
        from pyke.krb_compiler import kfbparser
    return kfbparser.parse(kfbparser, filename)

def compile_kqb(filename):
    global kqb_parser
    try:
        kqb_parser
    except NameError:
        from pyke.krb_compiler import kqb_parser
    return kqb_parser.parse_kqb(filename)

def write_file(lines, filename):
    with open(filename, 'w') as f:
        indents = [0]
        lineno_map = []
        write_file2(lines, f, indents, lineno_map, 0)
        if lineno_map:
            f.write("Krb_lineno_map = (\n")
            for map_entry in lineno_map:
                f.write("    %s,\n" % str(map_entry))
            f.write(")\n")

def write_file2(lines, f, indents, lineno_map, lineno, starting_lineno = None):
    for line in lines:
        if line == 'POPINDENT':
            assert len(indents) > 1
            del indents[-1]
        elif isinstance(line, tuple):
            if len(line) == 2 and line[0] == 'INDENT':
                indents.append(indents[-1] + line[1])
            elif len(line) == 2 and line[0] == 'STARTING_LINENO':
                assert starting_lineno is None, \
                       "missing ENDING_LINENO for STARTING_LINENO %d" % \
                           starting_lineno[1]
                starting_lineno = line[1], lineno + 1
            elif len(line) == 2 and line[0] == 'ENDING_LINENO':
                assert starting_lineno is not None, \
                       "missing STARTING_LINENO for ENDING_LINENO %d" % \
                           line[1]
                lineno_map.append(((starting_lineno[1], lineno),
                                   (starting_lineno[0], line[1])))
                starting_lineno = None
            else:
                lineno, starting_lineno = \
                    write_file2(line, f, indents, lineno_map, lineno,
                                starting_lineno)
        else:
            f.write(' ' * indents[-1] + line + '\n')
            lineno += 1
    return lineno, starting_lineno


def test():
    import doctest
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
