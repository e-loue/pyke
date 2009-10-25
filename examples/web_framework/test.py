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

from pyke import test
from examples.sqlgen import load_mysql_schema

def init():
    test.init(('.', '../sqlgen'))

def init_fn(engine):
    global Db_connection, Db_cursor
    import MySQLdb as db
    Db_connection = db.connect(user="movie_user", passwd="user_pw",
                               db="movie_db")
    Db_cursor = Db_connection.cursor()
    load_mysql_schema.load_schema(engine, Db_connection)
    engine.add_universal_fact('request', 'request_method', ('GET',))
    engine.add_universal_fact('request', 'path_info', ('/movie/1/movie.html',))
    engine.add_universal_fact('request', 'script_info', ('',))

def run():
    test.run(('web', 'database'), init_fn = init_fn, plan_globals = globals())

def doc_test():
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    doc_test()
