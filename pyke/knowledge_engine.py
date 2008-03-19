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
import re

from pyke import (condensedPrint, contexts, pattern,
                  fact_base, rule_base, special)

class CanNotProve(StandardError):
    pass

Name_test = re.compile(r'[a-zA-Z_][a-zA-Z0-9_]*$')
Bad_name_char = re.compile('[^a-zA-Z0-9_]')

class engine(object):
    _Variables = tuple(contexts.variable('ans_%d' % i) for i in range(100))
    
    def __init__(self, paths = ('.',),
                 gen_dir = '.', gen_root_dir = 'compiled_krb',
                 load_fc = True, load_bc = True):
        if not Name_test.match(gen_root_dir):
            raise ValueError(
                "engine.__init__: gen_root_dir (%s) must be a legal python "
                "identifier" % (gen_root_dir,))
        self.knowledge_bases = {}
        self.rule_bases = {}
        special.create_for(self)
        if paths != '*test*':
            if isinstance(paths, types.ModuleType):
                # secret hook for the compiler to initialize itself (so the
                # compiled python module can be in an egg).
                paths.populate(self)
            else:
                if isinstance(paths, types.StringTypes): paths = (paths,)
                compile_list = _get_compile_list(paths, gen_dir, gen_root_dir)
                if compile_list:
                    from pyke import krb_compiler
                    krb_compiler.compile(gen_dir, gen_root_dir, compile_list)
                    _check_list(compile_list, gen_dir, gen_root_dir)
                _load_paths(self, paths, gen_dir, gen_root_dir,
                            load_fc, load_bc, compile_list)
        for kb in self.knowledge_bases.itervalues(): kb.init2()
        for rb in self.rule_bases.itervalues(): rb.init2()
    def reset(self):
        for rb in self.rule_bases.itervalues(): rb.reset()
        for kb in self.knowledge_bases.itervalues(): kb.reset()
    def get_kb(self, kb_name, _new_class = None):
        ans = self.knowledge_bases.get(kb_name)
        if ans is None:
            if _new_class: ans = _new_class(self, kb_name)
            else: raise KeyError("knowledge_base %s not found" % kb_name)
        return ans
    def get_rb(self, rb_name):
        ans = self.rule_bases.get(rb_name)
        if ans is None: raise KeyError("rule_base %s not found" % rb_name)
        return ans
    def get_create(self, rb_name, parent = None, exclude_list = ()):
        ans = self.rule_bases.get(rb_name)
        if ans is None:
            ans = rule_base.rule_base(self, rb_name, parent, exclude_list)
        elif ans.parent != parent or ans.exclude_set != frozenset(exclude_list):
            raise AssertionError("duplicate rule_base: %s" % rb_name)
        return ans

    def add_universal_fact(self, kb_name, fact_name, args):
        if isinstance(args, types.StringTypes):
            raise TypeError("engine.add_universal_fact: "
                            "illegal args type, %s" % type(args))
        args = tuple(args)
        return self.get_kb(kb_name, fact_base.fact_base) \
                   .add_universal_fact(fact_name, args)
    def add_case_specific_fact(self, kb_name, fact_name, args):
        if isinstance(args, types.StringTypes):
            raise TypeError("engine.add_case_specific_fact: "
                            "illegal args type, %s" % type(args))
        args = tuple(args)
        return self.get_kb(kb_name, fact_base.fact_base) \
                   .add_case_specific_fact(fact_name, args)
    def assert_(self, kb_name, entity_name, args):
        if isinstance(args, types.StringTypes):
            raise TypeError("engine.assert_: "
                            "illegal args type, %s" % type(args))
        args = tuple(args)
        return self.get_kb(kb_name, fact_base.fact_base) \
                   .assert_(entity_name, args)

    def activate(self, *rb_names):
        for rb_name in rb_names: self.get_rb(rb_name).activate()

    def lookup(self, kb_name, entity_name, pat_context, patterns):
        return self.get_kb(kb_name).lookup(pat_context, pat_context,
                                           entity_name, patterns)

    def prove(self, kb_name, entity_name, pat_context, patterns):
        return self.get_kb(kb_name).prove(pat_context, pat_context,
                                          entity_name, patterns)
    def prove_n(self, kb_name, entity_name, fixed_args, num_returns):
        ''' Generates: a tuple of len == num_returns, and a plan (or None).
        '''
        context = contexts.simple_context()
        vars = self._Variables[:num_returns]
        try:
            for plan in self.prove(kb_name, entity_name, context,
                                   tuple(pattern.pattern_literal(arg)
                                         for arg in fixed_args) + vars):
                final = {}
                ans = tuple(context.lookup_data(var.name, final = final)
                            for var in vars)
                if plan: plan = plan.create_plan(final)
                yield ans, plan
        finally:
            context.done()
    def prove_1(self, kb_name, entity_name, fixed_args, num_returns):
        ''' Returns a tuple of len == num_returns, and a plan (or None).
        '''
        try:
            # All we need is the first one!
            return self.prove_n(kb_name, entity_name, fixed_args, num_returns) \
                       .next()
        except StopIteration:
            raise CanNotProve("Can not prove %s.%s%s" %
                               (kb_name, entity_name,
                                 condensedPrint.cprint(
                                   fixed_args + self._Variables[:num_returns])))
    def print_stats(self, f = sys.stdout):
        for kb in sorted(self.knowledge_bases.values(), key=lambda kb: kb.name):
            kb.print_stats(f)
    def trace(self, rb_name, rule_name):
        self.get_rb(rb_name).trace(rule_name)
    def untrace(self, rb_name, rule_name):
        self.get_rb(rb_name).untrace(rule_name)

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

def _load_paths(engine, paths, gen_dir, gen_root_dir, load_fc, load_bc,
                compile_list):
    if ('' if gen_dir == '.' else os.path.abspath(gen_dir)) not in sys.path:
        sys.path.append(os.path.abspath(gen_dir))
    for path in paths:
        for dirpath, dirnames, filenames in os.walk(path, onerror=_raise_exc):
            for filename in filenames:
                if filename.endswith('.krb'):
                    _load_file(engine, os.path.join(dirpath, filename),
                               gen_dir, gen_root_dir, load_fc, load_bc,
                               compile_list)

def _load_file(engine, filename, gen_dir, gen_root_dir, load_fc, load_bc,
               compile_list):
    base, package_list = _get_base_path(filename, gen_dir, gen_root_dir)
    base_modulename = os.path.basename(base)
    def load_module(type, do_import=True):
        try:
            os.stat(base + type + '.py')
            module_path = package_list + [base_modulename + type]
            full_module_name = '.'.join(module_path)
            #print "loading:", full_module_name
            if full_module_name in sys.modules:
                #print "already imported"
                module = sys.modules[full_module_name]
                if filename in compile_list:
                    module = reload(module)
                    #print module
            elif do_import:
                #print "needs import"
                module = _import(module_path)
            if do_import: module.populate(engine)
        except OSError:
            pass
    if load_fc: load_module('_fc')
    if load_bc:
        load_module('_plans', False)
        load_module('_bc')

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

def _check_list(compile_list, gen_dir, gen_root_dir):
    for filename in compile_list:
        if _needs_compiling(filename, gen_dir, gen_root_dir):
            raise AssertionError("%s didn't compile correctly" % filename)

def test():
    import doctest
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
