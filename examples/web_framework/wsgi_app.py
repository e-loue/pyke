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
import MySQLdb as db
from pyke import knowledge_engine, krb_traceback
from examples.sqlgen import load_mysql_schema

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

Initialized = False

def init():
    global Initialized, Engine, Db_connection, Db_cursor
    Engine = knowledge_engine.engine(('.', '../sqlgen'))
    Db_connection = db.connect(user="movie_user", passwd="user_pw",
                               db="movie_db")
    Db_cursor = Db_connection.cursor()
    load_mysql_schema.load_schema(Engine, Db_connection)
    Initialized = True

Debug = 0

def wsgi_app(environ, start_response):
    if not Initialized: init()
    else: Engine.reset()

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
    path = add_fact("request", "PATH_INFO")
    add_fact("request", "SCRIPT_NAME")
    add_fact("request", "QUERY_STRING")
    add_fact("request", "REMOTE_ADDR")
    add_fact("wsgi", "wsgi.multiprocess")
    add_fact("wsgi", "wsgi.multithread")
    add_fact("wsgi", "wsgi.run_once")

    for env_var in environ.keys():
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

    movie_id, template_name = path.lstrip('/').split('/')
    try:
        no_vars, plan = \
            Engine.prove_1("web", "process", (('movie',), template_name), 0)
    except:
        traceback = krb_traceback.format_exc(100)
        Db_connection.rollback()
        start_response('500 Server Error', [('Content-Type', 'text/plain')])
        return traceback

    status, headers, document = plan(Db_cursor, {'movie': int(movie_id)})
    start_response(status, headers)
    return document

def test():
    import doctest
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
