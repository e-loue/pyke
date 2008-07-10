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
import os
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
    def __init__(self, server_address, rq_handler_class, num_processes):
        self.num_processes = num_processes
        wsgiref.simple_server.WSGIServer.__init__(self, server_address,
                                                        rq_handler_class)
    def name(self): return "prefork_server(%d)" % self.num_processes
    def server_activate(self):
        wsgiref.simple_server.WSGIServer.server_activate(self)
        pids = []
        for i in xrange(self.num_processes - 1):
            pid = os.fork()
            if pid == 0: break
            pids.append(pid)
        else:
            # only run by parent process
            signal.signal(signal.SIGINT, functools.partial(kill, pids))

def run(num_processes = 2, port = 8080, logging = False):
    server_address = ('', port)
    httpd = server(server_address,
                   wsgiref.simple_server.WSGIRequestHandler 
                       if logging
                       else RequestHandlerNoLogging,
                   num_processes)
    httpd.set_app(wsgi_app.wsgi_app)
    httpd.serve_forever()

if __name__ == "__main__":
    run()
