# $Id$
# coding=utf-8
# 
# Copyright © 2009 Bruce Frederiksen
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

"""
    Each target_pkg object keeps track of all of the compiled files within one
    compiled_krb package.
"""

from __future__ import with_statement
import os, os.path
import time
import sys
import re
import pyke

debug = False

Name_test = re.compile(r'[a-zA-Z_][a-zA-Z0-9_]*$')

class target_pkg(object):
    r'''This manages all of the target files in a compiled_krb directory.

    There is one instance per compiled_krb directory.  It keeps track of
    everything in that directory and manages recompiling the sources when
    the compiled targets are missing or out of date.

    This instance is stored permanently in the "targets" variable of the
    compiled_pyke_files.py module in the compiled_krb directory.

    This maintains the following information for each compiled target file:
        source_package, source_filepath, compile_time, target_filename.
    '''
    def __init__(self, module_name, filename = None,
                       pyke_version = pyke.version,
                       loader = None, sources = None, compiler_version = 0):
        r'''

        The parameters are:

            module_name:  the complete dotted name of the compiled_pyke_files
                          module for this object.
            filename:     the absolute path to the compiled_pyke_files.py/c/o
                          file.
            pyke_version: the version of pyke used to compile the target files.
            loader:       the __loader__ attribute of the compiled_pyke_files
                          module (only set if the compiled_krb directory has
                          been zipped, otherwise None).
            sources:      {(source_package_name, path_from_package,
                            source_filepath):
                           [compile_time, target_file...]}
            compiler_version:
                          the version of the pyke compiler used to compile all
                          of the targets in this compiled_krb directory.

        This class is instantiated in two different circumstances:

        1.  From compiled_krb/compiled_pyke_files.py with a list of all of the
            compiled files in that compiled_krb directory.

            In this case, all of the parameters are passed to __init__.

        2.  From knowledge_engine.engine.__init__ (actually _create_target_pkg).

            In this case, only the first parameter is passed to __init__.

        Either way, after importing compiled_pyke_files or creating a new
        instance directly, reset is called by
        knowledge_engine.engine._create_target_pkg.
        '''

        # compiled_krb package name
        self.package_name = module_name.rsplit('.', 1)[0]

        if sources is None:
            # compiled_pyke_files.py does not exist.

            # Creating a new target_pkg object from scratch.
            try:
                # See if the self.package_name (e.g., compiled_krb) exists.
                target_package_dir = \
                    os.path.dirname(import_(self.package_name).__file__)
            except ImportError:
                if debug:
                    print >> sys.stderr, "target_pkg: no target package", \
                                         self.package_name
                # Create the target_package.
                last_dot = self.package_name.rfind('.')
                if last_dot < 0:
                    assert filename is not None
                    package_parent_dir = \
                      os.path.dirname(os.path.dirname(filename))
                else:
                    package_parent_dir = \
                      os.path.dirname(
                        # This import better work!
                        import_(self.package_name[:last_dot]).__file__)
                    if filename is not None:
                        assert os.path.normpath(package_parent_dir) == \
                                 os.path.normpath(
                                   os.path.dirname(os.path.dirname(filename)))
                if debug:
                    print >> sys.stderr, "target_pkg package_parent_dir:", \
                                         package_parent_dir
                target_package_dir = \
                    os.path.join(package_parent_dir,
                                 self.package_name[last_dot + 1:])
                if debug:
                    print >> sys.stderr, "target_pkg target_package_dir:", \
                                         target_package_dir
                if not os.path.lexists(target_package_dir):
                    if debug:
                        print >> sys.stderr, "target_pkg: mkdir", \
                                             target_package_dir
                    os.mkdir(target_package_dir)

                # Does __init__.py file exist?
                init_filepath = \
                    os.path.join(target_package_dir, '__init__.py')
                if debug:
                    print >> sys.stderr, "target_pkg init_filepath:", \
                                         init_filepath
                if not os.path.lexists(init_filepath):
                    # Create empty __init__.py file.
                    if debug:
                        print >> sys.stderr, "target_pkg: creating", \
                                             init_filepath
                    open(init_filepath, 'w').close()
            filename = os.path.join(target_package_dir,
                                    'compiled_pyke_files.py')

        if filename.endswith('.py'):
            self.filename = filename
        else:
            self.filename = filename[:-1]
        self.directory = os.path.dirname(self.filename)
        if debug:
            print >> sys.stderr, "target_pkg:", self.package_name, self.filename
        self.loader = loader

        if compiler_version == pyke.compiler_version:
            # {(source_package_name, source_filepath):
            #  [compile_time, target_filename, ...]}
            self.sources = sources if sources is not None else {}
        elif self.loader is None:
            # Force recompile of everything
            self.sources = {}
        else:
            # Loading incorrect pyke.compiler_version from zip file.
            # Can't recompile to zip file...
            raise AssertionError("%s: wrong version of pyke, "
                                 "running %s, compiled for %s" % 
                                 (module_name, pyke.version, pyke_version))

    def reset(self, check_sources = True):
        ''' This should be called once by engine.__init__ prior to calling
            add_source_package.
        '''
        if debug: print >> sys.stderr, "target_pkg.reset"
        self.dirty = False
        self.check_sources = check_sources

        # {(source_package_name, path_from_package): source_package_dir}
        self.source_packages = {}

        self.compiled_targets = set()  # set of target_filename
        self.rb_names = set()

    def add_source_package(self, source_package_name, path_from_package,
                                 source_package_dir):
        if debug:
            print >> sys.stderr, "target_pkg.add_source_package:", \
                                 source_package_name, source_package_dir
        if not self.loader:
            assert (source_package_name, path_from_package) not in \
                     self.source_packages, \
                   "duplicate source package: %s" % path_from_package
            if debug:
                print >> sys.stderr, "source_package_dir:", source_package_dir
                print >> sys.stderr, "path_from_package:", path_from_package
            source_dir = os.path.normpath(os.path.join(source_package_dir,
                                                       path_from_package))
            self.source_packages[source_package_name, path_from_package] = \
                source_dir
            sources = set([])
            for dirpath, dirnames, filenames \
             in os.walk(source_dir, onerror=_raise_exc):
                for filename in filenames:
                    if filename.endswith(('.krb', '.kfb', '.kqb')):
                        source_abspath = os.path.join(dirpath, filename)
                        assert dirpath.startswith(source_dir)
                        source_relpath = \
                            os.path.join(dirpath[len(source_dir)+1:],
                                         filename)
                        self.add_source(source_package_name, path_from_package,
                                        source_relpath,
                                        os.path.getmtime(source_abspath))
                        sources.add(source_relpath)

            # Delete old source file info for files that are no longer present
            for deleted_filepath \
             in [src_filepath
                 for src_pkg_name, src_path_from_pkg, src_filepath
                  in self.sources.iterkeys()
                     if src_pkg_name == source_package_name and
                        src_path_from_pkg == path_from_package and
                        src_filepath not in sources]:
                if debug:
                    print >> sys.stderr, "del:", source_package_name, filepath
                del self.sources[source_package_name, path_from_package,
                                 deleted_filepath]

    def add_source(self, source_package_name, path_from_package,
                         source_filepath, source_mtime):
        if debug:
            print >> sys.stderr, "target_pkg.add_source:", \
                                 source_package_name, path_from_package, \
                                 source_filepath
        rb_name = os.path.splitext(os.path.basename(source_filepath))[0]
        if debug: print >> sys.stderr, "rb_name:", rb_name
        if not Name_test.match(rb_name):
            raise ValueError("%s: %s illegal as python identifier" %
                             (source_filepath, rb_name))
        if rb_name in self.rb_names:
            raise ValueError("%s: duplicate knowledge base name" % rb_name)
        self.rb_names.add(rb_name)
        key = source_package_name, path_from_package, source_filepath
        if debug: print >> sys.stderr, "key:", key
        if self.sources.get(key, (0,))[0] < source_mtime:
            if debug:
                print >> sys.stderr, source_filepath, "needs to be compiled"
            self.sources[key] = []
            self.dirty = True

    def do_by_ext(self, prefix, filename, *args):
        ext = os.path.splitext(filename)[1][1:]
        return getattr(self, "%s_%s" % (prefix, ext))(filename, *args)

    def compile(self, engine):
        if debug: print >> sys.stderr, "%s.compile:" % self.package_name
        global krb_compiler
        if self.check_sources and not self.loader:
            initialized = False
            for (source_package_name, path_from_package, source_filename), \
                value \
             in self.sources.iteritems():
                if not value and \
                   (source_package_name, path_from_package) in \
                     self.source_packages:
                    if not initialized:
                        try:
                            krb_compiler
                        except NameError:
                            from pyke import krb_compiler
                        initialized = True
                    target_files = \
                        self.do_by_ext('compile',
                            os.path.join(
                                self.source_packages[source_package_name,
                                                     path_from_package],
                                source_filename))
                    if debug: print >> sys.stderr, "target_files:", target_files
                    value.append(time.time())
                    value.extend(target_files)
                    self.compiled_targets.update(target_files)

    def compile_krb(self, source_filename):
        if debug: print >> sys.stderr, "compile_krb:", source_filename
        rb_name = os.path.basename(source_filename)[:-4]
        return krb_compiler.compile_krb(rb_name, self.package_name,
                                        self.directory, source_filename)

    def compile_kfb(self, source_filename):
        if debug: print >> sys.stderr, "compile_kfb:", source_filename
        try:
            fbc_name = os.path.basename(source_filename)[:-4] + '.fbc'
            fbc_path = os.path.join(self.directory, fbc_name)
            self.pickle_it(krb_compiler.compile_kfb(source_filename), fbc_path)
            return (fbc_name,)
        except:
            if os.path.lexists(fbc_path): os.remove(fbc_path)
            raise

    def compile_kqb(self, source_filename):
        if debug: print >> sys.stderr, "compile_kqb:", source_filename
        try:
            qbc_name = os.path.basename(source_filename)[:-4] + '.qbc'
            qbc_path = os.path.join(self.directory, qbc_name)
            self.pickle_it(krb_compiler.compile_kqb(source_filename), qbc_path)
            return (qbc_name,)
        except:
            if os.path.lexists(qbc_path): os.remove(qbc_path)
            raise

    def write(self):
        if debug: print >> sys.stderr, "target_pkg.write"
        if self.dirty:
            sys.stderr.write('writing [%s]/%s\n' % 
                               (self.package_name,
                                os.path.basename(self.filename)))
            with open(self.filename, 'w') as f:
                f.write("# compiled_pyke_files.py\n\n")
                f.write("from pyke import target_pkg\n\n")
                f.write("pyke_version = %r\n\n" % pyke.version)
                f.write("compiler_version = %r\n\n" % pyke.compiler_version)
                f.write("try:\n");
                f.write("    loader = __loader__\n")
                f.write("except NameError:\n");
                f.write("    loader = None\n\n");
                f.write("targets = target_pkg.target_pkg(__name__, __file__, "
                        "pyke_version, loader, {\n")
                for key, value in self.sources.iteritems():
                    if debug: print >> sys.stderr, "write got:", key, value
                    if (key[0], key[1]) in self.source_packages:
                        if debug: print >> sys.stderr, "writing:", key, value
                        f.write("    %r: %r,\n" % (key, value))
                f.write("  },\n  compiler_version)\n")

    def load(self, engine, load_fc = True, load_bc = True,
                           load_fb = True, load_qb = True):
        load_flags = {'load_fc': load_fc, 'load_bc': load_bc,
                      'load_fb': load_fb, 'load_qb': load_qb}
        if debug: print >> sys.stderr, "target_pkg.load:", load_flags
        for (source_package_name, path_from_package, source_filename), value \
         in self.sources.iteritems():
            if not self.check_sources or self.loader or \
               (source_package_name, path_from_package) in self.source_packages:
                for target_filename in value[1:]:
                    if debug: print >> sys.stderr, "load:", target_filename
                    self.do_by_ext('load', target_filename, engine, load_flags)

    def load_py(self, target_filename, engine, flags):
        if debug: print >> sys.stderr, "load_py:", target_filename
        target_module = target_filename[:-3]  # strip '.py' extension.
        module_path = self.package_name + '.' + target_module
        if target_module.endswith('_fc'):
            if flags['load_fc']:
                self.load_module(module_path, target_filename, engine)
        elif target_module.endswith('_bc'):
            if flags['load_bc']:
                self.load_module(module_path, target_filename, engine)
        elif target_module.endswith('_plans'):
            if flags['load_bc']:
                self.load_module(module_path, target_filename, engine, False)
        else:
            raise AssertionError("target_pkg.load_py: "
                                 "unknown target file type: %s" %
                                   target_filename)

    def load_fbc(self, target_filename, engine, flags):
        if debug: print >> sys.stderr, "load_fbc:", target_filename
        if flags['load_fb']:
            self.load_pickle(target_filename, engine)

    def load_qbc(self, target_filename, engine, flags):
        if debug: print >> sys.stderr, "load_qbc:", target_filename
        if flags['load_qb']:
            self.load_pickle(target_filename, engine)

    def load_module(self, module_path, filename, engine, do_import = True):
        if debug: print >> sys.stderr, "load_module:", module_path, filename
        module = None
        if module_path in sys.modules:
            if debug: print >> sys.stderr, "load_module: already imported"
            module = sys.modules[module_path]
            if filename in self.compiled_targets:
                if debug: print >> sys.stderr, "load_module: reloading"
                module = reload(module)
        elif do_import:
            if debug: print >> sys.stderr, "load_module: importing"
            module = import_(module_path)
        if module is not None and \
           getattr(module, 'compiler_version', 0) != pyke.compiler_version:
            raise AssertionError("%s: incorrect pyke version: running "
                                 "%s, expected %s" %
                                   (filename, pyke.version,
                                    module.pyke_version))
        if do_import: module.populate(engine)

    def load_pickle(self, filename, engine):
        global pickle
        if debug: print >> sys.stderr, "load_pickle:", filename
        try:
            pickle
        except NameError:
            import cPickle as pickle
        full_path = os.path.join(self.directory, filename)
        if self.loader:
            import contextlib
            import StringIO
            ctx_lib = \
                contextlib.closing(
                    StringIO.StringIO(self.loader.get_data(full_path)))
        else:
            ctx_lib = open(full_path, 'rb')
        with ctx_lib as f:
            versions = pickle.load(f)
            if isinstance(versions, tuple):
                pyke_version, compiler_version = versions
            else:
                pyke_version, compiler_version = versions, 0
            if compiler_version != pyke.compiler_version:
                raise AssertionError("%s: incorrect pyke version: running "
                                     "%s, expected %s" %
                                       (filename, pyke.version, pyke_version))
            pickle.load(f).register(engine)

    def pickle_it(self, obj, path):
        global pickle
        try:
            pickle
        except NameError:
            import cPickle as pickle
            import copy_reg
            copy_reg.pickle(slice, lambda s: (slice, (s.start, s.stop, s.step)))
        sys.stderr.write("writing [%s]/%s\n" %
                           (self.package_name, os.path.basename(path)))
        with open(path, 'wb') as f:
            pickle.dump((pyke.version, pyke.compiler_version), f)
            pickle.dump(obj, f)

def _raise_exc(exc): raise exc

def import_(modulename):
    ''' modulepath does not include .py
    '''
    if debug: print >> sys.stderr, "import_:", modulename
    mod = __import__(modulename)
    for comp in modulename.split('.')[1:]:
        mod = getattr(mod, comp)
    return mod

