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
import functools
import types
import MySQLdb as db
import pyke
from pyke import krb_traceback, pattern, contexts
import load_mysql_schema

class cursor(object):
    rowcount = 1        # This is only check for unique queries...
    def __init__(self, width):
        self.width = width
    def execute(self, str, *args, **kws):
        if kws:
            if args:
                assert len(args) < 2
                args = args.copy().update(kws)
            else:
                args = kws
        print "execute got:"
        print str
        print "with:", args
    def fetchone(self, base = 44):
        return (base,) * self.width
    def fetchall(self):
        return tuple(self.fetchone(i) for i in range(1, 5))

def parse(str):
    str = str.strip()
    if str[0] == '(': return parse_tuple(str[1:])
    if str[0] in "0123456789.-+": return parse_number(str)
    if str[0] in "\"'": return parse_string(str)
    return parse_symbol(str)

def parse_number(str):
    '''
        >>> parse_number('123abc')
        (123, 'abc')
        >>> parse_number('123e17abc')
        (1.23e+19, 'abc')
        >>> parse_number('-123abc')
        (-123, 'abc')
        >>> parse_number('-1.23e-7abc')
        (-1.23e-07, 'abc')
    '''
    for i in range(1, len(str)):
        if str[i] not in "0123456789.-+e": break
    return eval(str[:i]), str[i:]

def parse_string(str):
    r'''
        >>> parse_string("'hello' mom")
        ('hello', ' mom')
        >>> parse_string(r'"hello\" mom"')
        ('hello" mom', '')
    '''
    quote = str[0]
    end = str.index(quote, 1)
    while str[end - 1] == '\\':
        end = str.index(quote, end + 1)
    return eval(str[:end + 1]), str[end + 1:]

def parse_symbol(str):
    '''
        >>> parse_symbol("abc, def")
        ('abc', ', def')
        >>> parse_symbol("$abc, def")
        ('$abc', ', def')
        >>> parse_symbol("*$abc, def")
        ('*$abc', ', def')
        >>> parse_symbol("*")
        ('*', '')
    '''
    if len(str) == 1: return str, ''
    for i in range(2 if str[0] == '*' and len(str) > 2 else 1, len(str)):
        if str[i].isspace() or str[i] in "\"'(),$*": break
    return str[:i], str[i:]

def parse_tuple(str):
    '''
        >>> parse_tuple("))")
        ((), ')')
        >>> parse_tuple("a, b), c)")
        (('a', 'b'), ', c)')
        >>> parse_tuple("a, (b), c)")
        (('a', ('b',), 'c'), '')
    '''
    ans = []
    str = str.lstrip()
    while str[0] != ')':
        element, str = parse(str)
        ans.append(element)
        str = str.lstrip()
        if str[0] == ',': str = str[1:].lstrip()
    return tuple(ans), str[1:]

def is_pattern(data):
    '''
        >>> is_pattern('abc')
        False
        >>> is_pattern(123)
        False
        >>> is_pattern(())
        False
        >>> is_pattern((1,2,3))
        False
        >>> is_pattern((1,2,'*$_'))
        True
    '''
    if isinstance(data, tuple):
        if data and isinstance(data[-1], types.StringTypes) and \
           data[-1][0] == '*':
            return True
        return any(is_pattern(element) for element in data)
    if isinstance(data, types.StringTypes) and data[0] == '$': return True
    return False

def as_pattern(data):
    if isinstance(data, tuple) and is_pattern(data):
        if isinstance(data[-1], types.StringTypes) and len(data[-1]) > 2 and \
           data[-1][0] == '*' and data[-1][1] == '$':
            if len(data[-1]) == 3 and data[-1][2] == '_':
                rest_var = contexts.anonymous()
            else:
                rest_var = contexts.variable(data[-1][2:])
            return pattern.pattern_tuple(tuple(as_pattern(element)
                                               for element in data[:-1]),
                                         rest_var)
        return pattern.pattern_tuple(tuple(as_pattern(element)
                                           for element in data))
    if isinstance(data, types.StringTypes) and len(data) > 1 and data[0] == '$':
        if len(data) == 2 and data[1] == '_':
            return contexts.anonymous()
        return contexts.variable(data[1:])
    return pattern.pattern_literal(data)

def init():
    global engine, did_init
    engine = pyke.engine()
    with contextlib.closing(db.connect(user="movie_user", passwd="user_pw",
                                       db="movie_db")) \
           as conn:
        load_mysql_schema.load_schema(engine, conn)
    did_init = True

did_init = False

def run():
    if not did_init: init()

    while True:
        print
        goal_str = raw_input("goal: ")
        if not goal_str: break
        goal, args_str = parse(goal_str)
        if goal == "trace":
            engine.trace("database", args_str.strip())
            continue
        if goal == "untrace":
            engine.untrace("database", args_str.strip())
            continue
        args = parse(args_str)[0]
        print "proving: %s%s" % (goal, args)
        goal_args = tuple(as_pattern(arg) for arg in args)
        engine.reset()
        context = contexts.simple_context()
        try:
            engine.activate('database')
            for prototype_plan \
             in engine.prove('database', goal, context, goal_args):
                print "got: %s%s" % \
                      (goal, tuple(arg.as_data(context, True)
                                   for arg in goal_args))
                if not prototype_plan:
                    print "no plan returned"
                else:
                    starting_data = dict(zip(args[0],
                                             range(1, len(args[0]) + 1)))
                    print "executing the plan with debug database cursor"
                    ans = prototype_plan.create_plan()(
                              cursor(len(args[1])), starting_data)
                    print "plan returned:", ans
                    while True:
                        print
                        data_values = raw_input("%s: " % str(args[0])).split()
                        if not data_values: break
                        starting_data = dict(zip(args[0], data_values))
                        print "executing the plan with real database cursor"
                        with contextlib.closing(db.connect(user="movie_user",
                                                           passwd="user_pw",
                                                           db="movie_db")) \
                               as conn:
                            with contextlib.closing(conn.cursor()) as cur:
                                ans = prototype_plan.create_plan() \
                                        (cur, starting_data)
                        print "plan returned:", ans
        except:
            krb_traceback.print_exc(100)

def test():
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()

