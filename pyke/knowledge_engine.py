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
import os, os.path
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
from pyke import contexts

debug = False

Sys_path = tuple(os.getcwd() if p == ''
                             else os.path.normpath(os.path.abspath(p))
                 for p in sys.path)

class CanNotProve(StandardError):
    pass

class engine(object):
    _Variables = tuple(contexts.variable('ans_%d' % i) for i in range(100))

    def __init__(self, *search_paths, **kws):
        r'''All search_paths are relative to reference_path.

        Each search_path may be:

            path        -- a path relative to reference_path to search for
                           source files, placing the compiled knowledge bases
                           in '.compiled_krb'.
            module      -- the module's __file__ is taken as the path.
            (None|path|module, target_package)
                        -- use target_package rather than '.compiled_krb'.
                           This is a package name in Python dotted name
                           notation relative to path.  Use None to use the
                           compiled knowledge bases in the target_package
                           without scanning for source files.

        kws can be: load_fc, load_bc, load_fb and load_qb.  They are all
        boolean valued and default to True.
        '''

        # import this stuff here to avoid import cycles...
        global condensedPrint, pattern, fact_base, goal, rule_base, special, \
               target_pkg
        from pyke import (condensedPrint, pattern, fact_base, goal, rule_base,
                          special, target_pkg)

        for keyword in kws.iterkeys():
            if keyword not in ('load_fc', 'load_bc', 'load_fb', 'load_qb'):
                raise TypeError("engine.__init__() got an unexpected keyword "
                                "argument %r" %
                                  keyword)
        self.knowledge_bases = {}
        self.rule_bases = {}
        special.create_for(self)

        if len(search_paths) == 1 and isinstance(search_paths[0], tuple) and \
           search_paths[0][0] == '*direct*' and \
           isinstance(search_paths[0][1], types.ModuleType):
            # secret hook for the compiler to initialize itself (so the
            # compiled python module can be in an egg).
            search_paths[0][1].populate(self)
        else:
            target_pkgs = {}  # {target_package_name: target_pkg}
            for path in search_paths:
                self._create_target_pkg(path, target_pkgs)
            for target_package in target_pkgs.itervalues():
                if debug:
                    print >>sys.stderr, "target_package:", target_package
                target_package.compile(self)
                target_package.write()
                target_package.load(self, **kws)
        for kb in self.knowledge_bases.itervalues(): kb.init2()
        for rb in self.rule_bases.itervalues(): rb.init2()

    def _create_target_pkg(self, path, target_pkgs):
        # Does target_pkg.add_source_package.

        if debug: print >> sys.stderr, "engine._create_target_pkg:", path

        # First, figure out source_package_name, source_package_dir
        #               and target_package_name:
        target_package_name = '.compiled_krb'   # default
        if isinstance(path, (tuple, list)):
            path, target_package_name = path
        if isinstance(path, types.ModuleType):
            path = path.__file__
        if not isinstance(path, (types.StringTypes, types.NoneType)):
            raise ValueError("illegal path argument: string expected, got " + \
                               str(type(path)))

        if debug:
            print >> sys.stderr, "_create_target_pkg path:", \
                                 repr(path)
            print >> sys.stderr, "_create_target_pkg target_package_name:", \
                                 repr(target_package_name)

        # Handle the case where there are no source files (for a distributed
        # app that wants to hide its knowledge bases):
        if path is None:
            assert target_package_name[0] != '.', \
                   "engine: relative target, %s, illegal " \
                   "with no source package" % \
                       target_package_name
            if target_package_name not in target_pkgs:
                # This import must succeed!
                tp = _get_target_pkg(target_package_name + 
                                       '.compiled_pyke_files')
                if tp is None:
                    raise AssertionError("%s: compiled with different version "
                                             "of Pyke" %
                                           target_package_name)
                tp.reset(check_sources=False)
                target_pkgs[target_package_name] = tp
            return

        path = os.path.normpath(os.path.abspath(path))

        path_to_package, source_package_name, remainder_path, zip_file_flag = \
          _pythonify_path(path)

        if debug:
            print >> sys.stderr, "_create_target_pkg path to " \
                                   "_pythonify_path:", \
                                 repr(path)
            print >> sys.stderr, "    path_to_package:", repr(path_to_package)
            print >> sys.stderr, "    source_package_name:", \
                                 repr(source_package_name)
            print >> sys.stderr, "    remainder_path:", repr(remainder_path)
            print >> sys.stderr, "    zip_file_flag:", zip_file_flag

        target_filename = None

        # Convert relative target_package_name (if specified) to absolute form:
        if target_package_name[0] == '.':
            num_dots = \
                len(target_package_name) - len(target_package_name.lstrip('.'))
            if debug:
                print >> sys.stderr, "_create_target_pkg num_dots:", num_dots
            if num_dots == 1:
                base_package = source_package_name
            else:
                base_package = \
                    '.'.join(source_package_name.split('.')[:-(num_dots - 1)])
            if base_package:
                target_package_name = \
                    base_package + '.' + target_package_name[num_dots:]
            else:
                target_package_name = target_package_name[num_dots:]

            target_filename = \
              os.path.join(path_to_package,
                           os.path.join(*target_package_name.split('.')),
                           'compiled_pyke_files.py')

            if debug:
                print >> sys.stderr, "_create_target_pkg " \
                                       "absolute target_package_name:", \
                                     target_package_name

        if target_package_name in target_pkgs:
            tp = target_pkgs[target_package_name]
        else:
            target_name = target_package_name + '.compiled_pyke_files'
            if debug:
                print >> sys.stderr, "_create_target_pkg target_name:", \
                                     target_name
            tp = None
            try:
                # See if compiled_pyke_files already exists.
                tp = _get_target_pkg(target_name)
            except ImportError:
                pass
            if tp is None:
                if debug:
                    print >> sys.stderr, "_create_target_pkg: no target module"
                tp = target_pkg.target_pkg(target_name, target_filename)
            tp.reset()
            target_pkgs[target_package_name] = tp

        source_package_dir = \
          os.path.join(path_to_package,
                       os.path.join(*source_package_name.split('.')))
        if not os.path.isdir(source_package_dir):
            source_package_dir = os.path.dirname(source_package_dir)
            remainder_path = os.path.dirname(remainder_path)
        tp.add_source_package(source_package_name, remainder_path,
                              source_package_dir)

    def get_ask_module(self):
        if not hasattr(self, 'ask_module'):
            from pyke import ask_tty
            self.ask_module = ask_tty
        return self.ask_module

    def reset(self):
        r'''Erases all case-specific facts and deactivates all rule bases.
        '''
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
        r'''Universal facts are not deleted by engine.reset.
        '''
        if isinstance(args, types.StringTypes):
            raise TypeError("engine.add_universal_fact: "
                            "illegal args type, %s" % type(args))
        args = tuple(args)
        return self.get_kb(kb_name, fact_base.fact_base) \
                   .add_universal_fact(fact_name, args)

    def add_case_specific_fact(self, kb_name, fact_name, args):
        r'''Case specific facts are deleted by engine.reset.
        '''
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
        r'''Activate rule bases.

        This runs all forward-chaining rules in the activated rule bases, so
        add your facts before doing this!
        '''
        for rb_name in rb_names: self.get_rb(rb_name).activate()

    def lookup(self, kb_name, entity_name, pat_context, patterns):
        return self.get_kb(kb_name).lookup(pat_context, pat_context,
                                           entity_name, patterns)

    def prove_goal(self, goal_str, **args):
        r'''Proves goal_str with logic variables set to args.

        This returns a context manager that you use in a with statement:

            Ugly setup to use the family_relations example.  You can ignore
            this... :-(

            >>> source_dir = os.path.dirname(os.path.dirname(__file__))
            >>> family_relations_dir = \
            ...   os.path.join(source_dir, 'examples/family_relations')
            >>> sys.path.insert(0, family_relations_dir)
            >>> from pyke import knowledge_engine
            >>> my_engine = knowledge_engine.engine(family_relations_dir)

            >>> my_engine.activate('bc_example')

            OK, here's the example!

            >>> with my_engine.prove_goal(
            ...        'family.how_related($person1, $person2, $how_related)',
            ...        person1='bruce') as it:
            ...     for vars, plan in it:
            ...         print "bruce is related to", vars['person2'], "as", \
            ...               vars['how_related']

        vars is a dictionary of all of the logic variables in the goal
        (without the '$') and their values.  The plan is a callable python
        function.

        If you only want the first answer, see engine.prove_1_goal.
        '''
        return goal.compile(goal_str).prove(self, **args)

    def prove_1_goal(self, goal_str, **args):
        r'''Proves goal_str with logic variables set to args.

        Returns the vars and plan for the first solution found.  Raises
        knowledge_engine.CanNotProve if no solutions are found.

            Ugly setup to use the family_relations example.  You can ignore
            this... :-(

            >>> source_dir = os.path.dirname(os.path.dirname(__file__))
            >>> family_relations_dir = \
            ...   os.path.join(source_dir, 'examples/family_relations')
            >>> sys.path.insert(0, family_relations_dir)
            >>> from pyke import knowledge_engine
            >>> my_engine = knowledge_engine.engine(family_relations_dir)

            >>> my_engine.activate('bc_example')

            OK, here's the example!

            >>> vars, plan = \
            ...   my_engine.prove_1_goal(
            ...     'bc_example.how_related($person1, $person2, $how_related)',
            ...     person1='bruce',
            ...     person2='m_thomas')
            >>> print "bruce is related to m_thomas as", vars['how_related']
            bruce is related to m_thomas as ('father', 'son')

        If you want more than one answer, see engine.prove_goal.
        '''
        return goal.compile(goal_str).prove_1(self, **args)

    def prove(self, kb_name, entity_name, pat_context, patterns):
        r'''Deprecated.  Use engine.prove_goal.
        '''
        return self.get_kb(kb_name).prove(pat_context, pat_context,
                                          entity_name, patterns)

    def prove_n(self, kb_name, entity_name, fixed_args = (), num_returns = 0):
        '''Returns a context manager for a generator of:
               a tuple of len == num_returns, and a plan (or None).

        Deprecated.  Use engine.prove_goal.
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
        r'''Returns a tuple of len == num_returns, and a plan (or None).

        Deprecated.  Use engine.prove_1_goal.
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

def _get_target_pkg(target_name):
    if debug: print >> sys.stderr, "_get_target_pkg", target_name
    module = target_pkg.import_(target_name)
    path = module.__file__
    if debug: print >> sys.stderr, "_get_target_pkg __file__ is", path
    if path.endswith(('.pyc', '.pyo')): path = path[:-1]
    compiled_path = path + ('o' if sys.flags.optimize else 'c')
    if debug:
        print >> sys.stderr, "source path is", path
        if os.path.exists(path):
            print >> sys.stderr, "source path exists"
            print >> sys.stderr, "source path mtime", os.path.getmtime(path)
        else:
            print >> sys.stderr, "source path does not exist"
        print >> sys.stderr, "compiled path is", compiled_path
        if os.path.exists(compiled_path):
            print >> sys.stderr, "compiled path exists"
            print >> sys.stderr, "compiled path mtime", \
                                 os.path.getmtime(compiled_path)
        else:
            print >> sys.stderr, "compiled path does not exist"
    if not os.path.exists(compiled_path) or \
          os.path.exists(path) and \
          os.path.getmtime(path) > os.path.getmtime(compiled_path):
        if debug:
            print >> sys.stderr, "_get_target_pkg doing reload for", target_name
        module = reload(module)
    if getattr(module, 'target_pkg_version', None) != pyke.target_pkg_version:
        if debug:
            print >> sys.stderr, "_get_target_pkg doing invalid version for", \
                                 target_name
        return None
    return getattr(module, 'get_target_pkg')()

def _pythonify_path(path):
    r'''Returns path_to_package, package_name, remainder_path, zip_file_flag.

    If zip_file_flag is set, remainder_path is ''.
    '''
    path = os.path.normpath(os.path.abspath(path))
    if path.endswith(('.py', '.pyc', '.pyo')):
        path = os.path.dirname(path)
    package_name = ''
    remainder_path = ''
    remainder_package_name = ''
    ans = '', '', path, False
    while path:
        if in_sys_path(path):
            if len(remainder_path) < len(ans[2]) or \
               len(remainder_path) == len(ans[2]) and \
                 len(package_name) > len(ans[1]):
                if os.path.isdir(path):
                    ans = path, package_name, remainder_path, False
                else:
                    ans = path, remainder_package_name, '', True
        parent_path, dir = os.path.split(path)
        if parent_path == '' or parent_path == path:
            break
        if _is_package_dir(path):
            if package_name:
                package_name = dir + '.' + package_name
            else:
                package_name = dir
        else:
            package_path = os.path.join(*package_name.split('.'))
            package_name = ''
            if remainder_path:
                remainder_path = os.path.join(dir, package_path, remainder_path)
            else:
                remainder_path = os.path.join(dir, package_path)
        if remainder_package_name:
            remainder_package_name = dir + '.' + remainder_package_name
        else:
            remainder_package_name = dir
        path = parent_path
    return ans

def _is_package_dir(path):
    if not os.path.isdir(path): return False
    return os.path.exists(os.path.join(path, '__init__.py')) or \
           os.path.exists(os.path.join(path, '__init__.pyc')) or \
           os.path.exists(os.path.join(path, '__init__.pyo'))

def in_sys_path(path):
    r'''Assumes path is a normalized abspath.
    '''
    return path in Sys_path

