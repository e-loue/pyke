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

import sys
import os, os.path
from pyke import knowledge_engine, krb_traceback

# Possibly interesting values:
#     CONTENT_LENGTH:
#     CONTENT_TYPE: application/x-www-form-urlencoded
#     PATH_INFO: /hello/mom/and/dad.html
#     QUERY_STRING: this=value&that=too
#     REMOTE_ADDR: 127.0.0.1
#     REQUEST_METHOD: GET
#     SCRIPT_NAME: 
#     wsgi.errors: <file>
#     wsgi.file_wrapper: <file>
#     wsgi.multiprocess: False
#     wsgi.multithread: True
#     wsgi.run_once: False

class trace_cursor(object):
    def __init__(self, cursor):
        self.cursor = cursor
    def execute(self, command, parameters=None):
        sys.stderr.write("\ncursor.execute got:\n")
        sys.stderr.write(command + '\n')
        if parameters: sys.stderr.write("with: %s\n" % str(parameters))
        return self.cursor.execute(command, parameters)
    def __getattr__(self, attr):
        return getattr(self.cursor, attr)

def init(db_connection, trace_sql=False):
    global Engine, Db_connection, Db_cursor
    Engine = knowledge_engine.engine('examples.sqlgen',
                                     'examples.web_framework')
    Db_connection = db_connection
    Db_cursor = db_connection.cursor()
    if trace_sql: Db_cursor = trace_cursor(Db_cursor)
    return Engine

Debug = 0

Web_framework_dir = os.path.dirname(__file__)

def gen_plan(environ, starting_tables, template_name):
    Engine.reset()

    def add_fact(fb_name, env_var):
        fact_name = env_var.split('.')[-1].lower()
        value = environ.get(env_var)
        if value is not None and value != '':
            if Debug:
                print "asserting %s.%s(%s) from %s" % \
                      (fb_name, fact_name, value, env_var)
            Engine.add_case_specific_fact(fb_name, fact_name, (value,))
        elif Debug:
            print "skipping %s.%s: got %s from %s" % \
                  (fb_name, fact_name, value, env_var)
        return value
    
    def add_http(env_var):
        fact_name = env_var[5:].lower()
        value = environ.get(env_var)
        if value is not None and value != '':
            if Debug:
                print "asserting header.%s(%s) from %s" % \
                      (fact_name, value, env_var)
            Engine.add_case_specific_fact("header", fact_name, (value,))
        elif Debug:
            print "skipping header.%s: got %s from %s" % \
                  (fact_name, value, env_var)
        return value

    add_fact("header", "CONTENT_TYPE")
    add_fact("request", "REQUEST_METHOD")
    add_fact("request", "PATH_INFO")
    add_fact("request", "SCRIPT_NAME")
    add_fact("request", "QUERY_STRING")
    add_fact("request", "REMOTE_ADDR")
    add_fact("wsgi", "wsgi.multiprocess")
    add_fact("wsgi", "wsgi.multithread")
    add_fact("wsgi", "wsgi.run_once")

    for env_var in environ.iterkeys():
        if env_var.startswith('HTTP_'): add_http(env_var)

    if Debug > 1:
        for key, value in environ.iteritems():
            print "environ: %s = %s" % (key, value)

    length = int(environ.get("CONTENT_LENGTH") or '0')
    if length:
        request_file = environ['wsgi.input']
        Engine.add_case_specific_fact("request", "body",
                                      (request_file.read(length),))

    Engine.activate('database', 'web')

    try:
        no_vars, plan = \
            Engine.prove_1_goal('web.process($starting_tables, $template_name)',
                                starting_tables=starting_tables,
                                template_name=template_name)
    except:
        traceback = krb_traceback.format_exc(100)
        return None, traceback
    return plan, None

Plans_cache = {}

def wsgi_app(environ, start_response):
    global Plans_cache

    # Parse the path:
    components = environ["PATH_INFO"].lstrip('/').split('/')
    template_name = os.path.join(Web_framework_dir, components[-1])
    starting_tables = []
    starting_keys = {}
    for i in range(0, len(components) - 1, 2):
        starting_tables.append(components[i])
        starting_keys[components[i]] = int(components[i + 1])
    # Convert to tuple so that it can be used as a dict key and sort so
    # different orders compare equal.
    starting_tables = tuple(sorted(starting_tables))

    template_mtime = os.stat(template_name).st_mtime
    mtime, plan = Plans_cache.get((starting_tables, template_name),
                                  (None, None))
    if mtime is None or mtime < template_mtime:
        print "get_plan(..., %s, %s)" % (starting_tables, template_name)
        plan, traceback = gen_plan(environ, starting_tables, template_name)
        if plan is None:
            Db_connection.rollback()
            start_response('500 Server Error', [('Content-Type', 'text/plain')])
            return traceback
        Plans_cache[starting_tables, template_name] = template_mtime, plan

    status, headers, document = plan(Db_connection, Db_cursor, starting_keys)
    start_response(status, headers)
    return document

def test():
    import doctest
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
