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
import signal
import functools
import wsgiref.simple_server
import wsgi_app

def kill(pids, signum, frame):
    sys.stderr.write("preforked_server(%d) caught SIGINT\n" % os.getpid())
    sys.stderr.write("preforked_server(%d) self.pids is %s\n" %
                     (os.getpid(), str(pids)))
    for pid in pids: os.kill(pid, signal.SIGTERM)
    sys.exit(1)

class RequestHandlerNoLogging(wsgiref.simple_server.WSGIRequestHandler):
    def log_request(self, code='-', size='-'): pass

class server(wsgiref.simple_server.WSGIServer):
    def __init__(self, server_address, rq_handler_class, num_processes,
                 trace_sql, db_engine):
        self.num_processes = num_processes
        self.trace_sql = trace_sql
        self.db_engine = db_engine
        wsgiref.simple_server.WSGIServer.__init__(self, server_address,
                                                        rq_handler_class)
    def init_wsgi(self):
        if self.db_engine.lower() == 'sqlite3':
            import sqlite3 as db
            import examples.sqlgen.load_sqlite3_schema as load_schema
            db_connection = \
                db.connect(os.path.join(os.path.dirname(load_schema.__file__),
                                        'sqlite3.db'))
        elif self.db_engine.lower() == 'mysql':
            import MySQLdb as db
            import examples.sqlgen.load_mysql_schema as load_schema
            db_connection = db.connect(user="movie_user", passwd="user_pw",
                                       db="movie_db")
        else:
            raise ValueError("prefork_server.init_wsgi: "
                             "unrecognized db_engine: " +
                             self.db_engine)
        load_schema.load_schema(wsgi_app.init(db_connection, self.trace_sql),
                                db, db_connection)
    def name(self): return "prefork_server(%d)" % self.num_processes
    def server_activate(self):
        wsgiref.simple_server.WSGIServer.server_activate(self)
        pids = []
        for i in xrange(self.num_processes - 1):
            pid = os.fork()
            if pid == 0:
                self.init_wsgi()
                break
            pids.append(pid)
        else:
            # only run by parent process
            self.init_wsgi()
            signal.signal(signal.SIGINT, functools.partial(kill, pids))

def run(num_processes = 2, port = 8080, logging = False, trace_sql = False,
        db_engine = 'sqlite3'):
    server_address = ('', port)
    httpd = server(server_address,
                   wsgiref.simple_server.WSGIRequestHandler 
                       if logging
                       else RequestHandlerNoLogging,
                   num_processes, trace_sql, db_engine)
    httpd.set_app(wsgi_app.wsgi_app)
    print "Server running..."
    httpd.serve_forever()

if __name__ == "__main__":
    run()
