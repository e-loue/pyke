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

import os.path
import wsgi_app
import wsgiref.simple_server

class RequestHandlerNoLogging(wsgiref.simple_server.WSGIRequestHandler):
    def log_request(self, code='-', size='-'): pass

def init(trace_sql = False, db_engine = 'sqlite3'):
    if db_engine.lower() == 'sqlite3':
        import sqlite3 as db
        import sqlgen.load_sqlite3_schema as load_schema
        db_connection = \
            db.connect(os.path.join(os.path.dirname(load_schema.__file__),
                                    'sqlite3.db'))
    elif db_engine.lower() == 'mysql':
        import MySQLdb as db
        import sqlgen.load_mysql_schema as load_schema
        db_connection = db.connect(user="movie_user", passwd="user_pw",
                                   db="movie_db")
    else:
        raise ValueError("simple_server.init: unrecognized db_engine: " +
                         db_engine)
    load_schema.load_schema(wsgi_app.init(db_connection, trace_sql), db,
                            db_connection)

def run(port = 8080, logging = True, trace_sql = False, db_engine = 'sqlite3'):
    init(trace_sql, db_engine)
    server_address = ('', port)
    httpd = wsgiref.simple_server.WSGIServer(
                server_address,
                wsgiref.simple_server.WSGIRequestHandler 
                    if logging
                    else RequestHandlerNoLogging)
    httpd.set_app(wsgi_app.wsgi_app)
    print "Server running..."
    httpd.serve_forever()

if __name__ == "__main__":
    run()
