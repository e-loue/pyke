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
import sys
import types
import os
import os.path
import re
import contextlib

if sys.version_info[0] < 3:
    import itertools
    class chain(object):
        old_chain = itertools.chain
        def __new__(cls, *args):
            return cls.old_chain(*args)
        @staticmethod
        def from_iterable(i):
            for iterable in i:
                for x in iterable: yield x
    itertools.chain = chain

import pyke
from pyke import (condensedPrint, contexts, pattern,
                  fact_base, rule_base, special)

class CanNotProve(StandardError):
    pass

Name_test = re.compile(r'[a-zA-Z_][a-zA-Z0-9_]*$')
Bad_name_char = re.compile('[^a-zA-Z0-9_]')

class engine(object):
    _Variables = tuple(contexts.variable('ans_%d' % i) for i in range(100))
    
    def __init__(self, paths = ('.',),
                 gen_root_location = '.', gen_root_pkg = 'compiled_krb',
                 load_fc = True, load_bc = True, load_fb = True,
                 load_qb = True):
        if not Name_test.match(gen_root_pkg):
            raise ValueError(
                "engine.__init__: gen_root_pkg (%s) must be a legal python "
                "identifier" % (gen_root_pkg,))
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
                compile_list = _get_compile_list(paths, gen_root_location,
                                                 gen_root_pkg)
                if compile_list:
                    from pyke import krb_compiler
                    krb_compiler.compile(gen_root_location, gen_root_pkg,
                                         compile_list)
                    _check_list(compile_list, gen_root_location, gen_root_pkg)
                compile_list2 = _load_paths(self, paths, gen_root_location,
                                            gen_root_pkg,
                                            load_fc, load_bc, load_fb, load_qb,
                                            compile_list)
                if compile_list2:
                    from pyke import krb_compiler
                    krb_compiler.compile(gen_root_location, gen_root_pkg,
                                         compile_list2)
                    _check_list(compile_list2, gen_root_location, gen_root_pkg)
                    for full_filename in compile_list2:
                        if not _load_file(self, full_filename,
                                          gen_root_location, gen_root_pkg,
                                          load_fc, load_bc, load_fb, load_qb,
                                          compile_list2):
                            raise AssertionError("version recompile failed")
        for kb in self.knowledge_bases.itervalues(): kb.init2()
        for rb in self.rule_bases.itervalues(): rb.init2()
    def get_ask_module(self):
        if not hasattr(self, 'ask_module'):
            from pyke import ask_tty
            self.ask_module = ask_tty
        return self.ask_module
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
    def get_ke(self, kb_name, entity_name):
        return self.get_kb(kb_name).get_entity_list(entity_name)

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
    def prove_n(self, kb_name, entity_name, fixed_args = (), num_returns = 0):
        ''' Returns a context manager for a generator of:
                a tuple of len == num_returns, and a plan (or None).
        '''
        if isinstance(fixed_args, types.StringTypes):
            raise TypeError("engine.prove_n: fixed_args must not be a string, "
                            "did you forget a , (%(arg)s) => (%(arg)s,)?" %
                            {'arg': repr(fixed_args)})
        def gen():
            context = contexts.simple_context()
            vars = self._Variables[:num_returns]
            try:
                with self.prove(kb_name, entity_name, context,
                                tuple(pattern.pattern_literal(arg)
                                      for arg in fixed_args) + vars) \
                  as it:
                    for plan in it:
                        final = {}
                        ans = tuple(context.lookup_data(var.name, final = final)
                                    for var in vars)
                        if plan: plan = plan.create_plan(final)
                        yield ans, plan
            finally:
                context.done()
        return contextlib.closing(gen())
    def prove_1(self, kb_name, entity_name, fixed_args = (), num_returns = 0):
        ''' Returns a tuple of len == num_returns, and a plan (or None).
        '''
        try:
            # All we need is the first one!
            with self.prove_n(kb_name, entity_name, fixed_args, num_returns) \
              as it:
                return iter(it).next()
        except StopIteration:
            raise CanNotProve("Can not prove %s.%s%s" %
                               (kb_name, entity_name,
                                 condensedPrint.cprint(
                                   fixed_args + self._Variables[:num_returns])))
    def print_stats(self, f = sys.stdout):
        for kb \
         in sorted(self.knowledge_bases.itervalues(), key=lambda kb: kb.name):
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
    ''' Convert all path components into legal python identifiers.
        Return converted result as a list of the legal identifiers.

        >>> _doctor_names('a/b/c')
        ['a', 'b', 'c']
        >>> _doctor_names('44/4.2/hi-mom.txt')
        ['_44', '_4_2', 'hi_mom_txt']
    '''
    def fix_component(c):
        if c[0] in '0123456789': c = '_' + c
        return Bad_name_char.sub('_', c)
    if not path: return []
    return [fix_component(component) for component in path.split(os.path.sep)]

def _get_base_path(filename, gen_root_location, gen_root_pkg, makedirs = False):
    r'''
        Figures out the base path for the compiled files of a source filename.

        Also returns a list of packages starting at gen_root_pkg to the
        package containing the compiled files.

        This is an example for the default gen_root_location, gen_root_pkg
        arguments:

        >>> sourcefile = 'sourcedir/a/b/c.krb'
        >>> base_path, package_list = \
        ...     _get_base_path(sourcefile, '.', 'compiled_krb')
        >>> base_path
        './compiled_krb/sourcedir/a/b/c'
        >>> package_list
        ['compiled_krb', 'sourcedir', 'a', 'b']

        Here's an example where the sources and compiled files are both in
        the same subdirectory (common_subdir):

        >>> common_subdir = 'x/y/z'
        >>> filename = common_subdir + '/' + sourcefile
        >>> base_path, package_list = \
        ...     _get_base_path(filename,
        ...                    common_subdir + '/test/root',
        ...                    'compiled_krb')
        >>> base_path
        'x/y/z/test/root/compiled_krb/sourcedir/a/b/c'
        >>> package_list
        ['compiled_krb', 'sourcedir', 'a', 'b']

        And finally an example where the sources and compiled files are in
        different directories starting in ../..:

        >>> import os, os.path
        >>> base2, sub2 = os.path.split(os.getcwd())
        >>> base1, sub1 = os.path.split(base2)
        >>> base_path, package_list = \
        ...     _get_base_path(sourcefile,
        ...                    '../../test_root',
        ...                    'compiled_krb')
        >>> expected_path = os.path.join('../../test_root/compiled_krb',
        ...                              _doctor_names(sub1)[0],
        ...                              _doctor_names(sub2)[0],
        ...                              'sourcedir/a/b/c')
        >>> base_path == expected_path
        True
        >>> package_list == ['compiled_krb',
        ...                  _doctor_names(sub1)[0], _doctor_names(sub2)[0],
        ...                  'sourcedir', 'a', 'b']
        True
    '''
    if makedirs and not os.path.exists(gen_root_location):
        os.makedirs(gen_root_location)
    fn_dirname, fn_basename = os.path.split(filename)
    fndrive, fnpath = os.path.splitdrive(os.path.abspath(fn_dirname))
    # convert "c:\a\b\c" to "\c_drive\a\b\c"
    if fndrive:
        fn_boguspath = '%s%s_drive%s' % (os.path.sep, fndrive, fnpath)
    else:
        fn_boguspath = fnpath
    #print "fn_boguspath:", fn_boguspath
    gendrive, genpath = os.path.splitdrive(os.path.abspath(gen_root_location))
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
    package_list = [gen_root_pkg] + _doctor_names(fn_unique_tail)
    if makedirs:
        path = _make_package_dirs(gen_root_location, package_list)
    else:
        path = os.path.join(gen_root_location, *package_list)
    return os.path.join(path, fn_basename[:-4]), package_list

def _needs_compiling(filename, gen_root_location, gen_root_pkg):
    r'''
        Returns True if 'filename' needs to be recompiled.

        This means that the compiled file exists and its modification time is
        later than modification time of 'filename'.

        It does not check the pyke.version cooked into the compiled file.
        That is done by _load_file.
    '''
    source_mtime = os.path.getmtime(filename)
    base, ignore = _get_base_path(filename, gen_root_location, gen_root_pkg)
    if filename.endswith('.krb'):
        try:
            ok = os.path.getmtime(base + '_fc.py') > source_mtime
        except OSError:
            ok = None
        if ok is None or ok:
            try:
                ok = os.path.getmtime(base + '_bc.py') > source_mtime
            except OSError:
                if ok is None: ok = False
    elif filename.endswith('.kfb'):
        try:
            ok = os.path.getmtime(base + '.fbc') > source_mtime
        except OSError:
            ok = False
    elif filename.endswith('.kqb'):
        try:
            ok = os.path.getmtime(base + '.qbc') > source_mtime
        except OSError:
            ok = False
    return not ok

def _get_compile_list(paths, gen_root_location, gen_root_pkg):
    ans = []
    for path in paths:
        for dirpath, dirnames, filenames in os.walk(path, onerror=_raise_exc):
            for filename in filenames:
                if len(filename) > 4 \
                   and filename[-4:] in ('.krb', '.kfb', '.kqb') \
                   and _needs_compiling(os.path.join(dirpath, filename),
                                        gen_root_location, gen_root_pkg):
                    ans.append(os.path.join(dirpath, filename))
    return ans

def _load_paths(engine, paths, gen_root_location, gen_root_pkg,
                load_fc, load_bc, load_fb, load_qb, compile_list):
    r'''
        Loads the compiled versions of all source files in 'paths'.

        Returns a list of source files that are missing or have old pyke
        versions in them.  These must be re-compiled and re-loaded.
    '''
    if gen_root_location == '.':
        if '' not in sys.path \
           and os.path.abspath(gen_root_location) not in sys.path:
            sys.path.insert(0, '')
    else:
        if os.path.abspath(gen_root_location) not in sys.path:
            sys.path.insert(0, os.path.abspath(gen_root_location))
    ans = []
    for path in paths:
        for dirpath, dirnames, filenames in os.walk(path, onerror=_raise_exc):
            for filename in filenames:
                if len(filename) > 4 \
                   and filename[-4:] in ('.krb', '.kfb', '.kqb'):
                    full_filename = os.path.join(dirpath, filename)
                    if not _load_file(engine, full_filename,
                                      gen_root_location, gen_root_pkg,
                                      load_fc, load_bc, load_fb, load_qb,
                                      compile_list):
                        ans.append(full_filename)
    #print "_load_paths =>", ans
    return ans

def _load_file(engine, filename, gen_root_location, gen_root_pkg,
               load_fc, load_bc, load_fb, load_qb, compile_list):
    base, package_list = \
        _get_base_path(filename, gen_root_location, gen_root_pkg)
    base_modulename = os.path.basename(base)
    def load_module(type, do_import=True):
        try:
            os.stat(base + type + '.py')
        except OSError:
            return True
        module_path = package_list + [base_modulename + type]
        full_module_name = '.'.join(module_path)
        #print >> sys.stderr, "loading:", full_module_name
        module = None
        if full_module_name in sys.modules:
            #print "already imported"
            module = sys.modules[full_module_name]
            if filename in compile_list:
                module = reload(module)
                #print module
        elif do_import:
            #print "needs import"
            module = _import(module_path)
        if module is not None and \
           (not hasattr(module, 'version') or module.version != pyke.version):
            #print "load_module(%s, %s) => False" % (filename, type)
            return False
        if module is not None and \
           module.Krb_source_filename != filename:
            raise AssertionError("duplicate knowledge base names, from files: "
                                 "%s and %s" %
                                 (module.Krb_source_filename, filename))
        if do_import: module.populate(engine)
        #print "load_module(%s, %s) => True" % (filename, type)
        return True
    if load_fc and filename.endswith('.krb'):
        if not load_module('_fc'): return False
    if load_bc and filename.endswith('.krb'):
        if not load_module('_plans', False): return False
        if not load_module('_bc'): return False
    if load_fb and filename.endswith('.kfb'):
        return _load_pickle(base + '.fbc', filename, engine)
    if load_qb and filename.endswith('.kqb'):
        return _load_pickle(base + '.qbc', filename, engine)
    return True

def _load_pickle(filename, source_filename, engine):
    global pickle
    try:
        pickle      # test to see whether this has already been loaded
    except NameError:
        import cPickle as pickle
    try:
        f = open(filename, 'rb')
    except IOError:
        return False
    try:
        version = pickle.load(f)
        if version != pyke.version: return False
        pickled_source_filename = pickle.load(f)
        if pickled_source_filename != source_filename:
            raise AssertionError("duplicate knowledge base names, from files: "
                                 "%s and %s" %
                                 (pickled_source_filename, source_filename))
        pickle.load(f).register(engine)
    finally:
        f.close()
    return True

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

def _check_list(compile_list, gen_root_location, gen_root_pkg):
    for filename in compile_list:
        if _needs_compiling(filename, gen_root_location, gen_root_pkg):
            raise AssertionError("%s didn't compile correctly" % filename)

def test():
    import doctest
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
