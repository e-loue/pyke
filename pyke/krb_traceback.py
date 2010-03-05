# $Id$
# coding=utf-8
# 
# Copyright © 2008 Bruce Frederiksen
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

import linecache
import traceback
import os.path
import sys

def print_tb(traceback, limit=None, file=None):
    if file is None: file = sys.stderr
    for line in format_list(extract_tb(traceback, limit)): file.write(line)

def print_exception(type, value, traceback, limit=None, file=None):
    if file is None: file = sys.stderr
    if traceback:
        file.write('Traceback (most recent call last):\n')
        print_tb(traceback, limit, file)
    lines = format_exception_only(type, value)
    file.write(lines[0])
    for line in lines[1:]: file.write(' ' + line)

def print_exc(limit=None, file=None):
    type, value, traceback = sys.exc_info()
    print_exception(type, value, traceback, limit, file)

def format_exc(limit=None):
    type, value, traceback = sys.exc_info()
    return format_exception(type, value, traceback, limit)

def print_last(limit=None, file=None):
    print_exception(sys.last_type, sys.last_value, sys.last_traceback,
                    limit, file)

def print_stack(f=None, limit=None, file=None):
    if file is None: file = sys.stderr
    for line in format_list(extract_stack(f, limit)): file.write(line)

def extract_tb(tb, limit=None):
    ans = convert_tb(traceback.extract_tb(tb))
    if limit is not None and len(ans) > limit:
        return ans[len(ans) - limit:]
    return ans

def extract_stack(f=None, limit=None):
    ans = convert_tb(traceback.extract_stack(f))
    if limit is not None and len(ans) > limit:
        return ans[len(ans) - limit:]
    return ans

format_list = traceback.format_list

format_exception_only = traceback.format_exception_only

def format_exception(type, value, traceback, limit=None):
    ans = []
    if traceback:
        ans.append('Traceback (most recent call last):\n')
        ans.extend(format_list(extract_tb(traceback, limit)))
    lines = format_exception_only(type, value)
    ans.append(lines[0])
    for line in lines[1:]: ans.append(' ' + line)
    return ''.join(ans)

def format_tb(tb, limit=None):
    return format_list(extract_tb(tb, limit))

def format_stack(f=None, limit=None):
    return format_list(extract_stack(f, limit))

def convert_lineno(module, lineno):
    for (py_start, py_end), (krb_start, krb_end) in module.Krb_lineno_map:
        if py_start <= lineno <= py_end: return krb_start

def convert_tb(extracted_tb):
    '''
        extracted_tb is list of (filename, lineno, functionname, line)
    '''
    ans = []
    batch = []
    for info in extracted_tb:
        filename, lineno, functionname, line = info
        if filename.endswith('_fc.py') or filename.endswith('_bc.py'):
            pathname = filename[:-3]
            while True:
                module_name = pathname.replace(os.path.sep, '.')
                if module_name in sys.modules:
                    module = sys.modules[module_name]
                    if hasattr(module, 'Krb_filename'):
                        krb_lineno = convert_lineno(module, lineno)
                        if krb_lineno is not None:
                            if not ans: ans = batch
                            batch = []
                            krb_filename = \
                                os.path.normpath(
                                  os.path.join(os.path.dirname(module.__file__),
                                               module.Krb_filename))
                            linecache.checkcache(krb_filename)
                            line = linecache.getline(krb_filename, krb_lineno)
                            if line: line = line.strip()
                            else: line = None
                            ans.append((krb_filename, krb_lineno, functionname,
                                        line))
                            info = None
                        else:
                            ans.extend(batch)
                            ans.append(info)
                            batch = []
                            info = None
                    break
                sep_index = pathname.find(os.path.sep)
                if sep_index < 0: break
                pathname = pathname[sep_index + 1:]
        if info: batch.append(info)
    return ans + batch

