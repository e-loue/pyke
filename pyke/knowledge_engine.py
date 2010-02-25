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
from pyke import (condensedPrint, contexts, pattern,
                  fact_base, goal, rule_base, special, target_pkg)

debug = False

class CanNotProve(StandardError):
    pass

class engine(object):
    _Variables = tuple(contexts.variable('ans_%d' % i) for i in range(100))

    def __init__(self, *paths, **kws):
        '''
            kws can be: load_fc, load_bc, load_fb and load_qb.
            They all default to True.
        '''
        for keyword in kws.iterkeys():
            if keyword not in ('load_fc', 'load_bc', 'load_fb', 'load_qb'):
                raise TypeError("engine.__init__() got an unexpected keyword "
                                "argument %r" %
                                  keyword)
        self.knowledge_bases = {}
        self.rule_bases = {}
        special.create_for(self)

        if len(paths) == 1 and isinstance(paths[0], tuple) and \
           paths[0][0] == '*direct*' and \
           isinstance(paths[0][1], types.ModuleType):
            # secret hook for the compiler to initialize itself (so the
            # compiled python module can be in an egg).
            paths[0][1].populate(self)
        else:
            target_pkgs = {}  # {target_package_name: target_pkg}
            for path in paths: self._init_path(path, target_pkgs)
            for target_package in target_pkgs.itervalues():
                if debug:
                    print >>sys.stderr, "target_package:", target_package
                target_package.compile(self)
                target_package.write()
                target_package.load(self, **kws)
        for kb in self.knowledge_bases.itervalues(): kb.init2()
        for rb in self.rule_bases.itervalues(): rb.init2()

    def _init_path(self, path, target_pkgs):
        if debug: print >> sys.stderr, "engine._init_path:", path
        # Does target_pkg.add_source_package.
        source_package_name = None
        target_package_name = '.compiled_krb'
        if isinstance(path, (tuple, list)):
            path, target_package_name = path
        if isinstance(path, types.StringTypes):
            source_package_name = path
        elif isinstance(path, types.ModuleType):
            if path.__file__.endswith(('__init__.py', '__init__.pyc',
                                       '__init__.pyo')):
                source_package_name = path.__name__
            else:
                source_package_name = path.__name__.rsplit('.', 1)[0]
        if debug:
            print >> sys.stderr, "_init_path source_package_name:", \
                                 source_package_name
            print >> sys.stderr, "_init_path target_package_name:", \
                                 target_package_name
        if source_package_name is None:
            assert target_package_name[0] != '.', \
                   "engine: relative target, %s, illegal " \
                   "with no source package" % \
                       target_package_name
            if target_package_name not in target_pkgs:
                # This import must succeed!
                tp = _get_target_pkg(target_package_name + 
                                       '.compiled_pyke_files')
                tp.reset()
                target_pkgs[target_package_name] = tp
            return
        if debug:
            print >> sys.stderr, "_init_path source_package_name:", \
                                 source_package_name
        if target_package_name[0] == '.':
            num_dots = \
                len(target_package_name) - len(target_package_name.lstrip('.'))
            if debug: print >> sys.stderr, "_init_path num_dots:", num_dots
            if num_dots == 1:
                base_package = source_package_name
            else:
                base_package = \
                    '.'.join(source_package_name.split('.')[:-(num_dots - 1)])
            target_package_name = \
                base_package + '.' + target_package_name[num_dots:]
        if debug:
            print >> sys.stderr, "_init_path target_package_name:", \
                                 target_package_name
        if target_package_name in target_pkgs:
            tp = target_pkgs[target_package_name]
        else:
            target_name = target_package_name + '.compiled_pyke_files'
            if debug:
                print >> sys.stderr, "_init_path target_name:", target_name
            try:
                # See if compiled_pyke_files already exists.
                tp = _get_target_pkg(target_name)
            except ImportError:
                if debug: print >> sys.stderr, "_init_path: no target module"
                # Create a new target_pkg object.
                try:
                    # See if the target_package exists.
                    target_package_dir = \
                        os.path.dirname(target_pkg.import_(target_package_name)
                                                  .__file__)
                except ImportError:
                    if debug:
                        print >> sys.stderr, "_init_path: no target package"
                    # Create the target_package.
                    last_dot = target_package_name.rfind('.')
                    if last_dot < 0:
                        package_parent_dir = '.'
                    else:
                        package_parent_dir = \
                          os.path.dirname(
                            # This import better work!
                            target_pkg.import_(target_package_name[:last_dot]) \
                                      .__file__)
                    if debug:
                        print >> sys.stderr, "_init_path package_parent_dir:", \
                                             package_parent_dir
                    target_package_dir = \
                        os.path.join(package_parent_dir,
                                     target_package_name[last_dot + 1:])
                    if debug:
                        print >> sys.stderr, "_init_path target_package_dir:", \
                                             target_package_dir
                    if not os.path.lexists(target_package_dir):
                        if debug:
                            print >> sys.stderr, "_init_path: mkdir", \
                                                 target_package_dir
                        os.mkdir(target_package_dir)
                    init_filepath = \
                        os.path.join(target_package_dir, '__init__.py')
                    if debug:
                        print >> sys.stderr, "_init_path init_filepath:", \
                                             init_filepath
                    if not os.path.lexists(init_filepath):
                        if debug:
                            print >> sys.stderr, "_init_path: creating", \
                                                 init_filepath
                        open(init_filepath, 'w').close()
                tp = target_pkg.target_pkg(
                       target_name,
                       os.path.join(target_package_dir,
                                    'compiled_pyke_files.py'))
            tp.reset()
            target_pkgs[target_package_name] = tp
        tp.add_source_package(source_package_name)

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

    def prove_goal(self, goal_str, **args):
        return goal.compile(goal_str).prove(self, **args)

    def prove_1_goal(self, goal_str, **args):
        return goal.compile(goal_str).prove_1(self, **args)

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

def _get_target_pkg(target_name):
    if target_name in sys.modules:
        return getattr(reload(sys.modules[target_name]), 'targets')
    return getattr(target_pkg.import_(target_name), 'targets')

def test():
    import doctest
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
