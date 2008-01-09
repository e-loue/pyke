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

import sys
import types
import os
import os.path
import imp
import re

from pyke import contexts

class CanNotProve(StandardError):
    pass

Knowledge_bases = {}
Rule_bases = {}

_Variables = tuple(contexts.variable('ans_%d' % i) for i in range(100))
_Load_done = False

def get_kb(kb_name, new_class = None):
    ans = Knowledge_bases.get(kb_name)
    if ans is None:
        if new_class: ans = new_class(kb_name)
        else: raise KeyError("knowledge_base: %s not found" % kb_name)
    return ans

def get_rb(rb_name):
    ans = Rule_bases.get(rb_name)
    if ans is None: raise KeyError("rule_base: %s not found" % rb_name)
    return ans

def init():
    for kb in Knowledge_bases.itervalues(): kb.init2()
    for rb in Rule_bases.itervalues(): rb.init2()

def reset():
    for rb in Rule_bases.itervalues(): rb.reset()
    for kb in Knowledge_bases.itervalues(): kb.reset()

def load(paths = ('.',), gen_dir = '.', gen_root_dir = 'compiled_krb',
         load_fc = True, load_bc = True):
    global _Load_done
    if _Load_done: raise AssertionError("pyke.load may only be called once")
    _Load_done = True
    if not Name_test.match(gen_root_dir):
        raise ValueError("pyke.load: "
                         "gen_root_dir (%s) must be a legal python identifier" %
                             (gen_root_dir,))
    if isinstance(paths, types.StringTypes): paths = (paths,)
    compile_list = _get_compile_list(paths, gen_dir, gen_root_dir)
    if compile_list:
        status = os.system("%s -m pyke.compiler %s %s %s" % 
                           (sys.executable, gen_dir, gen_root_dir,
                            ' '.join(compile_list)))
        if status != 0:
            raise SyntaxError("Errors encountered trying to compile")
        _check_list(compile_list, gen_dir, gen_root_dir)
    _load_paths(paths, gen_dir, gen_root_dir, load_fc, load_bc)
    init()

def _raise_exc(exc): raise exc

def _make_package_dirs(base_dir, package_path):
    ''' Creates directories in package_path, relative to base_dir, and makes
        sure that each one has an __init__.py file in it.

        Package_path is a sequence of path components.

        Returns the full path (base_dir/package_path)
    '''
    if len(package_path) > 1: _make_package_dirs(base_dir, package_path[:-1])
    full_package_path = os.path.join(base_dir, os.path.join(*package_path))
    if not os.path.exists(full_package_path): os.mkdir(full_package_path)
    init_file_path = os.path.join(full_package_path, '__init__.py')
    if not os.path.exists(init_file_path): open(init_file_path, 'w').close()
    return full_package_path

Name_test = re.compile(r'[a-zA-Z_][a-zA-Z0-9_]*$')
Bad_name_char = re.compile('[^a-zA-Z0-9_]')

def _doctor_names(path):
    ''' Convert all path components into legal path names.
        Return converted result.
    '''
    def fix_component(c):
        if c[0] in '0123456789': c = '_' + c
        return Bad_name_char.sub('_', c)
    if not path: return []
    return [fix_component(component) for component in path.split(os.path.sep)]

def _get_base_path(filename, gen_dir, gen_root_dir, makedirs = False):
    if makedirs and not os.path.exists(gen_dir): os.makedirs(gen_dir)
    fn_dirname, fn_name = os.path.split(filename)
    fndrive, fnpath = os.path.splitdrive(os.path.abspath(fn_dirname))
    # convert "c:\a\b\c" to "\c_drive\a\b\c"
    if fndrive:
        fn_boguspath = '%s%s_drive%s' % (os.path.sep, fndrive, fnpath)
    else:
        fn_boguspath = fnpath
    #print "fn_boguspath:", fn_boguspath
    gendrive, genpath = os.path.splitdrive(os.path.abspath(gen_dir))
    if gendrive:
        gen_boguspath = '%s%s_drive%s' % (os.path.sep, gendrive, genpath)
    else:
        gen_boguspath = genpath
    #print "gen_boguspath:", gen_boguspath
    # find commonprefix to last common path component
    # unfortunately, os.path.commonprefix(['a/ba/c', 'a/bb/d']) gives 'a/b'!
    commonprefix = os.path.commonprefix([fn_boguspath, gen_boguspath])
    assert commonprefix and commonprefix[0] == os.path.sep
    #print "commonprefix:", commonprefix
    if commonprefix == fn_boguspath:
        skip_len = len(commonprefix)
    elif commonprefix == gen_boguspath: 
        skip_len = len(commonprefix) + 1
    else:
        skip_len = commonprefix.rindex(os.path.sep) + 1
    fn_unique_tail = fn_boguspath[skip_len:]
    #print "fn_unique_tail:", fn_unique_tail
    assert not fn_unique_tail or fn_unique_tail[0] != os.path.sep
    package_list = [gen_root_dir] + _doctor_names(fn_unique_tail)
    if makedirs:
        path = _make_package_dirs(gen_dir, package_list)
    else:
        path = os.path.join(gen_dir, *package_list)
    return os.path.join(path, fn_name[:-4]), package_list

def _needs_compiling(filename, gen_dir, gen_root_dir):
    source_mtime = os.stat(filename).st_mtime
    base, ignore = _get_base_path(filename, gen_dir, gen_root_dir)
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

def _get_compile_list(paths, gen_dir, gen_root_dir):
    ans = []
    for path in paths:
        for dirpath, dirnames, filenames in os.walk(path, onerror=_raise_exc):
            for filename in filenames:
                if filename.endswith('.krb') and \
                   _needs_compiling(os.path.join(dirpath, filename),
                                    gen_dir, gen_root_dir):
                    ans.append(os.path.join(dirpath, filename))
    return ans

def _check_list(compile_list, gen_dir, gen_root_dir):
    for filename in compile_list:
        if _needs_compiling(filename, gen_dir, gen_root_dir):
            raise AssertionError("%s didn't compile correctly" % filename)

def _load_paths(paths, gen_dir, gen_root_dir, load_fc, load_bc):
    if ('' if gen_dir == '.' else os.path.abspath(gen_dir)) not in sys.path:
        sys.path.append(os.path.abspath(gen_dir))
    for path in paths:
        for dirpath, dirnames, filenames in os.walk(path, onerror=_raise_exc):
            for filename in filenames:
                if filename.endswith('.krb'):
                    _load_file(os.path.join(dirpath, filename),
                               gen_dir, gen_root_dir, load_fc, load_bc)

def _load_file(filename, gen_dir, gen_root_dir, load_fc, load_bc):
    base, package_list = _get_base_path(filename, gen_dir, gen_root_dir)
    base_modulename = os.path.basename(base)
    if load_fc:
        try:
            os.stat(base + '_fc.py')
            _import(package_list + [base_modulename + '_fc'])
        except OSError:
            pass
    if load_bc:
        try:
            os.stat(base + '_bc.py')
            _import(package_list + [base_modulename + '_bc'])
        except OSError:
            pass

""" ******* for testing:
def trace_import(*args, **kws):
    if args[0].endswith('_plans'):
        sys.stderr.write("import: ")
        if kws: sys.stderr.write("kws.keys(): %s " % (str(kws.keys()),))
        for arg in args:
            if isinstance(arg, dict):
                if '__name__' in arg:
                    sys.stderr.write('%s[%d] ' % (arg['__name__'], len(arg)))
                else:
                    sys.stderr.write(str(len(arg)) + ' ')
            else:
                sys.stderr.write(str(arg) + ' ')
        sys.stderr.write('\n')
    return old_import(*args)

import __builtin__
old_import = __builtin__.__import__
#print "__builtin__:", __builtin__, "old_import:", old_import
__builtin__.__import__ = trace_import
********* end testing """

def _import(modulepath):
    ''' modulepath does not include .py
    '''
    #print "_import:", modulepath
    mod = __import__('.'.join(modulepath))
    for comp in modulepath[1:]:
        mod = getattr(mod, comp)
    return mod

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
                               condensedPrint.cprint(fixed_args + 
                                                     _Variables[:num_returns])))


# This has to come after Knowledge_bases and Rule_bases are initialized for
# initialization code in special.
#
# Must include 'special' here to get it to load and be available to the rules.
#
from pyke import (fact_base, pattern, condensedPrint, special)


def test():
    import doctest
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
