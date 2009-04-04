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
    The target_pkg object keeps track of all of the compiled files within one
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
    '''
        This maintains a list of:
            source_package, source_filepath, compile_time, target_filenames.
    '''
    def __init__(self, module_name, filename, pyke_version = pyke.version,
                       loader = None, sources = None):
        self.package_name = module_name.rsplit('.', 1)[0]
        self.filename = filename
        self.directory = os.path.dirname(self.filename)
        if debug:
            print >> sys.stderr, "target_pkg:", self.package_name, self.filename
        self.loader = loader

        if pyke_version == pyke.version:
            # {(source_package_name, source_filepath):
            #  [compile_time, target_filename, ...]}
            self.sources = sources if sources is not None else {}
        elif self.loader is None:
            self.sources = {}
        else:
            raise AssertionError("%s: wrong version of pyke, "
                                 "running %s, compiled for %s" % 
                                 (pyke.version, pyke_version))
    def reset(self):
        ''' This should be called once by engine.__init__ prior to calling
            add_source_package.
        '''
        if debug: print >> sys.stderr, "target_pkg.reset"
        self.dirty = False
        self.source_packages = {}  # {source_package_name: source_package_dir}
        self.compiled_targets = set([])  # set of target_filename
        self.rb_names = set()
    def add_source_package(self, source_package_name):
        if debug:
            print >> sys.stderr, "target_pkg.add_source_package:", \
                                 source_package_name
        if not self.loader:
            assert source_package_name not in self.source_packages, \
                   "duplicate source package: %s" % source_package_name
            source_package_dir = \
                os.path.dirname(import_(source_package_name).__file__)
            if debug:
                print >> sys.stderr, "source_package_dir:", source_package_dir
            self.source_packages[source_package_name] = source_package_dir
            sources = set([])
            for dirpath, dirnames, filenames \
             in os.walk(source_package_dir, onerror=_raise_exc):
                for filename in filenames:
                    if len(filename) > 4 \
                       and filename[-4:] in ('.krb', '.kfb', '.kqb'):
                        source_abspath = os.path.join(dirpath, filename)
                        assert dirpath.startswith(source_package_dir)
                        source_relpath = \
                            os.path.join(dirpath[len(source_package_dir)+1:],
                                         filename)
                        self.add_source(source_package_name, source_relpath,
                                        os.path.getmtime(source_abspath))
                        sources.add(source_relpath)
            # delete any old source files that are no longer present
            for filepath in [src_filepath
                             for src_pkg_name, src_filepath
                              in self.sources.iterkeys()
                                 if src_pkg_name == source_package_name and \
                                    src_filepath not in sources]:
                if debug:
                    print >> sys.stderr, "del:", source_package_name, filepath
                del self.sources[source_package_name, filepath]
    def add_source(self, source_package_name, source_filepath, source_mtime):
        if debug:
            print >> sys.stderr, "target_pkg.add_source:", \
                                 source_package_name, source_filepath
        rb_name = os.path.basename(source_filepath)[:-4]
        if debug: print >> sys.stderr, "rb_name:", rb_name
        if not Name_test.match(rb_name):
            raise ValueError("%s: %s illegal as python identifier" %
                             (source_filepath, rb_name))
        if rb_name in self.rb_names:
            raise ValueError("%s: duplicate knowledge base name" % rb_name)
        self.rb_names.add(rb_name)
        key = source_package_name, source_filepath
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
        if not self.loader:
            initialized = False
            for (source_package_name, source_filename), value \
             in self.sources.iteritems():
                if not value and source_package_name in self.source_packages:
                    if not initialized:
                        try:
                            krb_compiler
                        except NameError:
                            from pyke import krb_compiler
                        initialized = True
                    target_files = \
                        self.do_by_ext('compile',
                            os.path.join(
                                self.source_packages[source_package_name],
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
                f.write("version = %r\n\n" % pyke.version)
                f.write("try:\n");
                f.write("    loader = __loader__\n")
                f.write("except NameError:\n");
                f.write("    loader = None\n\n");
                f.write("targets = "
                        "target_pkg.target_pkg(__name__, __file__, "
                        "version, loader, {\n")
                for item in self.sources.iteritems():
                    if debug: print >> sys.stderr, "write got:", item
                    if item[0][0] in self.source_packages:
                        if debug: print >> sys.stderr, "writing:", item
                        f.write("    %r: %r,\n" % item)
                f.write("})\n")
    def load(self, engine, load_fc = True, load_bc = True,
                           load_fb = True, load_qb = True):
        load_flags = {'load_fc': load_fc, 'load_bc': load_bc,
                      'load_fb': load_fb, 'load_qb': load_qb}
        if debug: print >> sys.stderr, "target_pkg.load:", load_flags
        for (source_package_name, source_filename), value \
         in self.sources.iteritems():
            if source_package_name in self.source_packages:
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
           (not hasattr(module, 'version') or module.version != pyke.version):
            raise AssertionError("%s: incorrect pyke version: "
                                 "%s, expected %s" %
                                   (filename, module.version, pyke.version))
        if do_import: module.populate(engine)
    def load_pickle(self, filename, engine):
        global pickle
        if debug: print >> sys.stderr, "load_pickle:", filename
        try:
            pickle
        except NameError:
            import cPickle as pickle
        if self.loader:
            import contextlib
            import StringIO
            top_pkg_path = \
                os.path.dirname(sys.modules[self.package_name.split('.')[0]]
                                   .__file__)
            egg_path = os.path.dirname(top_pkg_path)
            assert filename.startswith(egg_path)
            ctx_lib = \
                contextlib.closing(
                    StringIO.StringIO(
                        self.loader.get_data(filename[len(egg_path) + 1:])))
                        # ...   + 1 to drop the '/' too.
        else:
            ctx_lib = open(os.path.join(self.directory, filename), 'rb')
        with ctx_lib as f:
            version = pickle.load(f)
            if version != pyke.version:
                raise AssertionError("%s: incorrect pyke version: "
                                     "%s, expected %s" %
                                       (filename, version, pyke.version))
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
            pickle.dump(pyke.version, f)
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

def test():
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
