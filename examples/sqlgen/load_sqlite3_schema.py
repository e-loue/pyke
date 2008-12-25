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

    It adds two kinds of facts:
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

debug = False

def load_schema(engine, connection):
    with contextlib.closing(connection.cursor()) as table_cursor:
        table_cursor.execute("""select name from sqlite_master
                                 where type='table'
                             """)
        with contextlib.closing(connection.cursor()) as column_cursor:
            for name, in table_cursor.fetchall():
                _load_table(engine, column_cursor, name)
    depth = 1
    while _links_to(engine, depth): depth += 1

def _load_table(engine, cursor, table_name):
    # This doesn't allow sql parameters!
    cursor.execute("pragma table_info(%s)" % table_name)
    for col_num, col_name, type, null_flag, default, key in cursor.fetchall():
        _create_column(engine, table_name, col_name, type, null_flag != 99,
                       key, default, None)

def _create_column(engine, table_name, col_name, type, null, key, default,
                   extra):
    null = null.upper() == 'YES'
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

def _links_to(engine, depth):
    ans = False
    if depth == 1:
        with engine.prove_n("schema", "many_to_1", (), 4) as gen1:
            for (from_table, to_table, from_columns, to_columns), bogus_plan \
             in gen1:
                _add_fact(engine, "links_to",
                          (1, from_table, to_table,
                           ((to_table, from_table, from_columns, to_columns),)))
                ans = True
        return ans
    with engine.prove_n("schema", "links_to", (depth - 1,), 3) as gen2:
        for (from_table, to_table, joins), bogus_plan1 in gen2:
            with engine.prove_n("schema", "many_to_1", (to_table,), 3) as gen3:
                for (end_table, to_columns, end_columns), bogus_plan2 in gen3:
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
