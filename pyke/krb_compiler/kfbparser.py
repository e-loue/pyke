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

""" See http://www.dabeaz.com/ply/ply.html for syntax of grammer definitions.
""" 

from __future__ import with_statement
import os, os.path
from ply import yacc
from pyke.krb_compiler import scanner
from pyke import fact_base

tokens = scanner.kfb_tokens

def p_file(p):
    ''' file : nl_opt facts
        facts :
        facts : facts fact
    '''
    pass

def p_fact0(p):
    ''' fact : IDENTIFIER_TOK LP_TOK RP_TOK NL_TOK '''
    Fact_base.add_universal_fact(p[1], ())

def p_fact1(p):
    ''' fact : IDENTIFIER_TOK LP_TOK data_list RP_TOK NL_TOK '''
    Fact_base.add_universal_fact(p[1], tuple(p[3]))

def p_none(p):
    ''' data : NONE_TOK
        comma_opt :
        comma_opt : ','
        nl_opt :
        nl_opt : NL_TOK
    '''
    p[0] = None

def p_first(p):
    ''' data : NUMBER_TOK
        data : STRING_TOK
    '''
    p[0] = p[1]

def p_quoted_last(p):
    ''' data : IDENTIFIER_TOK
    '''
    p[0] = p[1]

def p_false(p):
    ''' data : FALSE_TOK
    '''
    p[0] = False

def p_true(p):
    ''' data : TRUE_TOK
    '''
    p[0] = True

def p_empty_tuple(p):
    ''' data : LP_TOK RP_TOK
    '''
    p[0] = ()

def p_start_list(p):
    ''' data_list : data
    '''
    p[0] = [p[1]]

def p_append_list(p):
    ''' data_list : data_list ',' data
    '''
    p[1].append(p[len(p)-1])
    p[0] = p[1]

def p_tuple(p):
    ''' data : LP_TOK data_list comma_opt RP_TOK '''
    p[0] = tuple(p[2])

def p_error(t):
    raise SyntaxError("invalid syntax",
                      scanner.syntaxerror_params(t.lexpos, t.lineno))

parser = None

# Use the first line for normal use, the second for testing changes in the
# grammer (the first line does not report grammer errors!).
def parse(this_module, filename, check_tables = False, debug = 0):
#def parse(this_module, filename, check_tables = False, debug = 1):
    '''
        >>> from pyke.krb_compiler import kfbparser
        >>> kfbparser.parse(kfbparser,
        ...                 'TEST/kfbparse_test.kfb'
        ...                 if os.path.split(os.getcwd())[1] == 'krb_compiler'
        ...                 else 'krb_compiler/TEST/kfbparse_test.kfb',
        ...                 True)
        <fact_base kfbparse_test>
    '''
    global parser, Fact_base
    if parser is None:
        outputdir = os.path.dirname(this_module.__file__)
        if debug:
            parser = yacc.yacc(module=this_module, write_tables=0,
                               debug=debug, debugfile='kfbparser.yacc.out',
                               outputdir=outputdir)
        else:
            if check_tables:
                kfbparser_mtime = os.path.getmtime(this_module.__file__)
                tables_name = os.path.join(outputdir, 'kfbparser_tables.py')
                try:
                    ok = os.path.getmtime(tables_name) >= kfbparser_mtime
                except OSError:
                    ok = False
                if not ok:
                    #print "regenerating kfbparser_tables"
                    try: os.remove(tables_name)
                    except OSError: pass
                    try: os.remove(tables_name + 'c')
                    except OSError: pass
                    try: os.remove(tables_name + 'o')
                    except OSError: pass
            parser = yacc.yacc(module=this_module, debug=0,
                               optimize=1, write_tables=1,
                               tabmodule='pyke.krb_compiler.kfbparser_tables',
                               outputdir=outputdir)
    dirs, base = os.path.split(filename)
    name = base[:-4]
    Fact_base = fact_base.fact_base(None, name, False)
    with open(filename) as f:
        scanner.init(scanner, debug, check_tables, True)
        scanner.lexer.lineno = 1
        scanner.lexer.filename = filename
        #parser.restart()
        parser.parse(f.read(), lexer=scanner.lexer, tracking=True, debug=debug)
    ans = Fact_base
    Fact_base = None
    return ans


def test():
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
