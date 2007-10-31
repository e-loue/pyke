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
import types
import os
import os.path
import imp

# Must include 'special' here to get it to load and be available to the rules.
from pyke import (knowledge_base, rule_base, fact_base, pattern, contexts,
                  condensedPrint, special)

class CanNotProve(StandardError):
    pass

get_kb = knowledge_base.get
get_rb = rule_base.get
init = rule_base.init
reset = rule_base.reset

_Load_done = False

def load(paths = ('.',), load_fc = True, load_bc = True):
    global _Load_done
    assert not _Load_done, "pyke.load may only be called once"
    _Load_done = True
    if isinstance(paths, types.StringTypes): paths = (paths,)
    compile_list = _get_compile_list(paths)
    if compile_list:
        status = os.system("python -m pyke.compiler %s" % 
                           ' '.join(compile_list))
        if status != 0:
            raise SyntaxError("Errors encountered trying to compile")
        _check_list(compile_list)
    _load_path(paths, load_fc, load_bc)
    init()

def _raise_exc(exc): raise exc

def _needs_compiling(filename):
    source_mtime = os.stat(filename).st_mtime
    base = filename[:-4]
    try:
        ok = os.stat(base + '_fc.py').st_mtime > source_mtime
    except OSError:
        ok = None
    if ok is None or ok:
        try:
            ok = os.stat(base + '_bc.py').st_mtime > source_mtime
        except OSError:
            if ok is None: ok = False
    return not ok

def _get_compile_list(paths):
    ans = []
    for path in paths:
        for dirpath, dirnames, filenames in os.walk(path, onerror=_raise_exc):
            for filename in filenames:
                if filename.endswith('.krb') and \
                   _needs_compiling(os.path.join(dirpath, filename)):
                    ans.append(os.path.join(dirpath, filename))
    return ans

def _check_list(compile_list):
    for filename in compile_list:
        if _needs_compiling(filename):
            raise AssertionError("%s didn't compile correctly" % filename)

def _load_path(paths, load_fc, load_bc):
    for path in paths:
        for dirpath, dirnames, filenames in os.walk(path, onerror=_raise_exc):
            for filename in filenames:
                if filename.endswith('.krb'):
                    _load_file(os.path.join(dirpath, filename),
                               load_fc, load_bc)

def _load_file(filename, load_fc, load_bc):
    base = filename[:-4]
    if load_fc:
        try:
            os.stat(base + '_fc.py')
            _import(base + '_fc')
        except OSError:
            pass
    if load_bc:
        try:
            os.stat(base + '_bc.py')
            _import(base + '_bc')
        except OSError:
            pass

def _import(modulepath):
    ''' modulepath does not include .py
    '''
    name = os.path.basename(modulepath)
    path = os.path.dirname(modulepath)
    #print "modulepath", modulepath, "name", name, "path", path
    file, pathname, description = imp.find_module(name, [path])
    try:
        imp.load_module(name, file, pathname, description)
    finally:
        if file is not None: file.close()

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

_Variables = tuple(contexts.variable('ans_%d' % i) for i in range(100))

def prove_n(kb_name, entity_name, fixed_args, num_returns):
    ''' Generates: a tuple of len == num_returns, and a plan (or None).
    '''
    context = contexts.simple_context()
    vars = _Variables[:num_returns]
    try:
        for plan in prove(kb_name, entity_name, context,
                          tuple(pattern.pattern_literal(arg)
                                for arg in fixed_args) + vars):
            ans = tuple(context.lookup_data(var.name) for var in vars)
            if plan: plan = plan.create_plan()
            yield ans, plan
    finally:
        context.done()

def prove_1(kb_name, entity_name, fixed_args, num_returns):
    ''' Returns a tuple of len == num_returns, and a plan (or None).
    '''
    try:
        # All we need is the first one!
        return prove_n(kb_name, entity_name, fixed_args, num_returns).next()
    except StopIteration:
        raise CanNotProve("Can not prove %s.%s%s" %
                              (kb_name, entity_name,
                               condensedPrint.cprint(fixed_args + vars)))

def test():
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
