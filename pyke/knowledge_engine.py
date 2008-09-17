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
    
    def __init__(self, paths = ('.',), generated_root_dir = 'compiled_krb',
                 load_fc = True, load_bc = True, load_fb = True,
                 load_qb = True):
        gen_root_location, root_package = os.path.split(generated_root_dir)
        if not Name_test.match(root_package):
            raise ValueError(
                "engine.__init__: generated_root_dir (%s) must end with a "
                "legal python identifier" % (generated_root_dir,))
        self.knowledge_bases = {}
        self.rule_bases = {}
        special.create_for(self)
        if paths != '*test*':
            if isinstance(paths, types.ModuleType):
                # secret hook for the compiler to initialize itself (so the
                # compiled python module can be in an egg).
                paths.populate(self)
            else:
                # Make sure gen_root_location is on sys.path.
                if gen_root_location == '.' or gen_root_location == '':
                    if '' not in sys.path \
                       and os.path.abspath(gen_root_location) not in sys.path:
                        sys.path.insert(0, '')
                else:
                    if os.path.abspath(gen_root_location) not in sys.path:
                        sys.path.insert(0, os.path.abspath(gen_root_location))

                if isinstance(paths, types.StringTypes): paths = (paths,)

                # Generate list of files that need to be recompiled.
                compile_list = _get_compile_list(paths, generated_root_dir)

                # Compile files.
                if compile_list:
                    from pyke import krb_compiler
                    krb_compiler.compile(generated_root_dir, compile_list)
                    _check_list(compile_list, generated_root_dir)

                # Load files.  This may produce another list of files that
                # need to be recompiled due to different embedded pyke version
                # numbers.
                compile_list2 = _load_paths(self, paths, generated_root_dir,
                                            root_package,
                                            load_fc, load_bc, load_fb, load_qb,
                                            compile_list)

                # Compile and load files.
                if compile_list2:
                    from pyke import krb_compiler
                    krb_compiler.compile(generated_root_dir, compile_list2)
                    _check_list(compile_list2, generated_root_dir)
                    for full_filename in compile_list2:
                        if not _load_file(self, full_filename,
                                          generated_root_dir, root_package,
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

def _needs_compiling(filename, generated_root_dir):
    r'''
        Returns True if 'filename' needs to be recompiled.

        This means that the compiled file exists and its modification time is
        later than modification time of 'filename'.

        It does not check the pyke.version cooked into the compiled file.
        That is done by _load_file.
    '''
    source_mtime = os.path.getmtime(filename)
    base = os.path.join(generated_root_dir, os.path.basename(filename)[:-4])
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

def _get_compile_list(paths, generated_root_dir):
    ans = []
    for path in paths:
        for dirpath, dirnames, filenames in os.walk(path, onerror=_raise_exc):
            for filename in filenames:
                if len(filename) > 4 \
                   and filename[-4:] in ('.krb', '.kfb', '.kqb') \
                   and _needs_compiling(os.path.join(dirpath, filename),
                                        generated_root_dir):
                    ans.append(os.path.join(dirpath, filename))
    return ans

def _load_paths(engine, paths, generated_root_dir, root_package,
                load_fc, load_bc, load_fb, load_qb, compile_list):
    r'''
        Loads the compiled versions of all source files in 'paths'.

        Returns a list of source files that are missing or have old pyke
        versions in them.  These must be re-compiled and re-loaded.
    '''
    ans = []
    for path in paths:
        for dirpath, dirnames, filenames in os.walk(path, onerror=_raise_exc):
            for filename in filenames:
                if len(filename) > 4 \
                   and filename[-4:] in ('.krb', '.kfb', '.kqb'):
                    full_filename = os.path.join(dirpath, filename)
                    if not _load_file(engine, full_filename,
                                      generated_root_dir, root_package,
                                      load_fc, load_bc, load_fb, load_qb,
                                      compile_list):
                        ans.append(full_filename)
    #print "_load_paths =>", ans
    return ans

def _load_file(engine, filename, generated_root_dir, root_package,
               load_fc, load_bc, load_fb, load_qb, compile_list):
    base_modulename = os.path.basename(filename)[:-4]
    base = os.path.join(generated_root_dir, base_modulename)
    def load_module(type, do_import=True):
        try:
            os.stat(base + type + '.py')
        except OSError:
            return True
        module_path = (root_package, base_modulename + type)
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

def _check_list(compile_list, generated_root_dir):
    for filename in compile_list:
        if _needs_compiling(filename, generated_root_dir):
            raise AssertionError("%s didn't compile correctly" % filename)

def test():
    import doctest
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
