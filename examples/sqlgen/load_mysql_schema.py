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


'''
    This module loads universal facts representing a schema into a pyke engine.

    All facts are put in the "schema" fact base.

    It adds five kinds of facts:
        paramstyle(style)
        column(table_name, col_name, type, null, key, default, extra)
        primary_key(table_name, columns)
        many_to_1(table_many, table_1, table_many_columns, table_1_columns)
        links_to(depth, start_table, end_table, joins)

    The many_to_1 facts are determined by column names ending with "_id".
    The part before "_id" is taken as the table name being referred to with a
    primary key of ('id').

    This module only exports one function: load_schema, which you'd call once
    at startup after you've created your pyke engine.
'''

from __future__ import with_statement
import contextlib

from pyke import goal

debug = False

def load_schema(engine, dbi_module, connection):
    _add_fact(engine, "paramstyle", (dbi_module.paramstyle,))
    with contextlib.closing(connection.cursor()) as table_cursor:
        table_cursor.execute("show tables")
        with contextlib.closing(connection.cursor()) as column_cursor:
            for name, in table_cursor.fetchall():
                _load_table(engine, column_cursor, name)
    depth = 1
    while _links_to(engine, depth): depth += 1

def _load_table(engine, cursor, table_name):
    # This doesn't allow sql parameters!
    cursor.execute("show columns from " + table_name)
    for col_name, type, null, key, default, extra in cursor.fetchall():
        _create_column(engine, table_name, col_name, type,
                       null.upper() == 'YES', key, default, extra)

def _create_column(engine, table_name, col_name, type, null, key, default,
                   extra):
    #null = null.upper() == 'YES'
    if not key: key = None
    if not default: default = None
    if not extra: extra = None
    _add_fact(engine, "column",
              (table_name, col_name, type, null, key, default, extra))
    if col_name == 'id':
        _add_fact(engine, "primary_key", (table_name, (col_name,)))
    if col_name.endswith('_id'):
        to_table = col_name[:-3]
        _add_fact(engine, "many_to_1",
                  (table_name, to_table, (col_name,), ('id',)))

many_to_1 = goal.compile(
  'schema.many_to_1($from_table, $to_table, $from_columns, $to_columns)')

links_to = goal.compile(
  'schema.links_to(%depth, $from_table, $to_table, $joins)')

many_to_1_to = goal.compile(
  'schema.many_to_1(%to_table, $end_table, $to_columns, $end_columns)')

def _links_to(engine, depth):
    ans = False
    if depth == 1:
        with many_to_1.prove(engine) as gen1:
            for vars, bogus_plan in gen1:
                from_table, to_table, from_columns, to_columns = \
                  vars['from_table'], vars['to_table'], vars['from_columns'], \
                  vars['to_columns']
                _add_fact(engine, "links_to",
                          (1, from_table, to_table,
                           ((to_table, from_table, from_columns, to_columns),)))
                ans = True
        return ans
    with links_to.prove(engine, depth=depth - 1) as gen2:
        for vars, bogus_plan1 in gen2:
            from_table, to_table, joins = \
              vars['from_table'], vars['to_table'], vars['joins']
            with many_to_1_to.prove(engine, to_table=to_table) as gen3:
                for vars, bogus_plan2 in gen3:
                    end_table, to_columns, end_columns = \
                      vars['end_table'], vars['to_columns'], vars['end_columns']
                    if end_table != from_table and \
                       not any(end_table == join_clause[0]
                               for join_clause in joins):
                        _add_fact(engine, "links_to",
                            (depth, from_table, end_table,
                             joins + ((end_table, to_table, to_columns,
                                       end_columns),)))
                        ans = True
    return ans

def _add_fact(engine, fact, args):
    if debug: print "schema", fact, args
    engine.add_universal_fact("schema", fact, args)
