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


from __future__ import with_statement
import contextlib
from pyke import test
import load_mysql_schema

class cursor(object):
    rowcount = 1        # This is only check for unique queries...
    def __init__(self, width):
        self.width = width
    def execute(self, str, parameters=None):
        print "execute got:"
        print str
        if parameters: print "with:", parameters
    def fetchone(self, base = 44):
        return (base,) * self.width
    def fetchall(self):
        return tuple(self.fetchone(i) for i in range(1, 5))

def init():
    global db
    import MySQLdb as db
    test.init()
    with contextlib.closing(db.connect(user="movie_user", passwd="user_pw",
                                       db="movie_db")) \
           as conn:
        load_mysql_schema.load_schema(test.Engine, db, conn)

def run_plan(globals, locals):
    plan = locals['plan']
    args = locals['args']
    starting_keys = dict(zip(args[0], range(1, len(args[0]) + 1)))
    print "executing the plan with debug database cursor"
    ans = plan(cursor(len(args[1])), starting_keys)
    print "plan returned:", ans
    while True:
        print
        data_values = raw_input("%s: " % str(args[0])).split()
        if not data_values: break
        starting_keys = dict(zip(args[0], data_values))
        print "executing the plan with real database cursor"
        with contextlib.closing(db.connect(user="movie_user",
                                           passwd="user_pw",
                                           db="movie_db")) \
               as conn:
            with contextlib.closing(conn.cursor()) as cur:
                ans = plan(cur, starting_keys)
        print "plan returned:", ans

def run():
    if not test.Did_init: init()
    test.run('database', fn_to_run_plan = run_plan)

def doc_test():
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    doc_test()

