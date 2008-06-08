# $Id$
# coding=utf-8
# 
# Copyright © 2007 Bruce Frederiksen
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
from ply import lex

debug=0

states = (
    ('indent', 'exclusive'),
    ('code', 'exclusive'),
    ('checknl', 'exclusive'),
)

keywords = frozenset((
    'as',
    'assert',
    'bc_extras',
    'check',
    'extending',
    'False',
    'fc_extras',
    'first',
    'forall',
    'foreach',
    'in',
    'None',
    'notany',
    'plan_extras',
    'python',
    'require',
    'step',
    'taking',
    'True',
    'use',
    'when',
    'with',
    'without',
))

tokens = tuple(x.upper() + '_TOK' for x in keywords) + (
    'ANONYMOUS_VAR_TOK',
    'CODE_TOK',
  # 'DATE_TOK',         # FIX: Add the definition for this!
    'DEINDENT_TOK',
    'IDENTIFIER_TOK',
    'INDENT_TOK',
  # 'LB_TOK',
  # 'LC_TOK',
    'LP_TOK',
    'NL_TOK',
    'NOT_NL_TOK',
    'NUMBER_TOK',
    'PATTERN_VAR_TOK',
  # 'RB_TOK',
  # 'RC_TOK',
    'RP_TOK',
    'STRING_TOK',
)

literals = '*:,!.='     # FIX: delete ':'

t_ignore = ' \t'

t_ignore_comment = r'\#.*'

def t_continuation(t):
    r'\\(\r)?\n'
    t.lexer.lineno += 1

def t_NL_TOK(t):
    # newline, followed by any number of empty or comment only lines
    r'(\r)?\n([ \t]*(\#.*)?(\r)?\n)*'
    t.lexer.lineno += t.value.count('\n')
    if nesting_level == 0:
        t.lexer.begin('indent')
        t.lexer.skip(-1)        # put the final '\n' back for tp_indent_sp!
        return t

indent_levels = []

# to prevent getting a warning...
t_indent_ignore = ''

def t_indent_sp(t):
    # ply doesn't like re's that can be empty, so we'll include the prior
    # newline char in the re and then skip over it when we count the indent
    # level.  The tp_NL_TOK function does a skip(-1) to retain the final '\n'
    # for t_indent_sp.
    r'\n[ \t]*'
    indent = count_indent(t.value[1:])
    current_indent = indent_levels[-1] if indent_levels else 0
    if debug:
        print "t_indent_sp: t.value", repr(t.value), "indent", indent, \
              "current_indent", current_indent, \
              "indent_levels", indent_levels, \
              "t.lexpos", t.lexpos, \
              "t.lexer.lexpos", t.lexer.lexpos, \
              "t.lexer.lexdata[]", repr(t.lexer.lexdata[t.lexpos])
    if indent > current_indent:
        t.type = 'INDENT_TOK'
        indent_levels.append(indent)
        t.lexer.begin('INITIAL')
        if debug: print "INDENT_TOK: indent_levels", indent_levels
        return t
    if indent < current_indent:
        if indent > 0 and indent not in indent_levels:
            raise SyntaxError(
                      "deindent doesn't match any previous indent level",
                      syntaxerror_params(t.lexpos))
        t.type = 'DEINDENT_TOK'
        del indent_levels[-1]
        if indent < (indent_levels[-1] if indent_levels else 0):
            if debug: print " -- pushing indent back"
            t.lexer.skip(-len(t.value))
        else:
            if debug: print " -- doing begin('INITIAL')"
            t.lexer.begin('INITIAL')
        if debug: print "DEINDENT_TOK: indent_levels", indent_levels
        return t
    # else indent == current_indent
    t.lexer.begin('INITIAL')
    if debug: print "no indent: indent_levels", indent_levels

t_checknl_ignore = ' \t'

def t_checknl_nl(t):
    # optional comment followed by newline
    r'(\#.*)?(\r)?\n'
    t.lexer.lineno += 1
    t.lexer.begin('indent')
    t.lexer.skip(-1)        # put the final '\n' back for tp_indent_sp!
    t.type = 'NL_TOK'
    return t

def t_checknl_other(t):
    # something other than newline
    r'[^\#\r\n]'
    t.lexer.skip(-1)        # put the final char back!
    t.type = 'NOT_NL_TOK'
    return t

def start_code(plan_name = None, multiline = False,
               var_format = "(context['%s'])"):
    global current_line, code, current_plan_name, code__level
    global pattern_var_format, plan_vars_needed, code_nesting_level
    global code_lineno, code_lexpos
    global code_indent_level
    pattern_var_format = var_format
    plan_vars_needed = []
    current_line = ''
    code = []
    if multiline: code_indent_level = indent_levels[-1]
    else: code_indent_level = 1000000000
    current_plan_name = plan_name
    code_nesting_level = 0
    code_lineno = code_lexpos = None
    lexer.begin('code')

def mark(t):
    global code_lineno, code_lexpos
    if code_lineno is None:
        code_lineno = t.lexer.lineno
        code_lexpos = t.lexpos

# to prevent getting a warning...
t_code_ignore = ''

def t_code_string(t):
    r"'''([^\\]|\\.)*?'''|" \
    r'"""([^\\]|\\.)*?"""|' \
    r"'([^'\\\n\r]|\\.|\\(\r)?\n)*?'|" \
    r'"([^"\\\n\r]|\\.|\\(\r)?\n)*?"'
    global current_line
    current_line += t.value
    mark(t)
    if debug: print "scanner saw string:", t.value
    t.lexer.lineno += t.value.count('\n')

def t_code_comment(t):
    r'[ \t\f\r]*\#.*'
    global current_line
    if debug: print "scanner saw comment:", t.value
    #current_line += t.value

def t_code_plan(t):
    r'\$\$'
    global current_line
    mark(t)
    if debug:
        print "scanner saw '$$', current_plan_name is", current_plan_name
    if not current_plan_name:
        raise SyntaxError("'$$' only allowed in plan_specs within the "
                          "'when' clause",
                          syntaxerror_params(t.lexpos))
    current_line += pattern_var_format % current_plan_name
    plan_vars_needed.append(current_plan_name)

def t_code_pattern_var(t):
    r'\$[a-zA-Z_][a-zA-Z0-9_]*\b'
    global current_line
    mark(t)
    if not pattern_var_format:
        raise SyntaxError("$<name> only allowed in backward chaining rules",
                          syntaxerror_params(t.lexpos))
    current_line += pattern_var_format % t.value[1:]
    plan_vars_needed.append(t.value[1:])
    if debug: print "scanner saw pattern_var:", t.value

def t_code_continuation(t):
    r'\\(\r)?\n'
    global current_line
    t.lexer.lineno += 1
    current_line += '\\'
    code.append(current_line)
    current_line = ''
    if debug: print "scanner saw continuation:", t.value

def t_code_open(t):
    r'[{([]'
    global current_line, code_nesting_level
    mark(t)
    code_nesting_level += 1
    current_line += t.value

def t_code_close(t):
    r'[]})]'
    global current_line, code_nesting_level
    mark(t)
    if code_nesting_level <= 0:
        raise SyntaxError("unmatched %s" % repr(t.value),
                          syntaxerror_params(t.lexpos))
    code_nesting_level -= 1
    current_line += t.value

def t_code_symbol(t):
    r'''[0-9a-zA-Z_]+'''
    global current_line
    mark(t)
    current_line += t.value
    if debug: print "scanner saw symbol:", t.value

def t_code_space(t):
    r'''[ \t]+'''
    global current_line
    current_line += t.value
    if debug: print "scanner saw space chars:", t.value

def t_code_other(t):
    r'''[^][(){}$\\'"\r\n0-9a-zA-Z_ \t]+'''
    global current_line
    mark(t)
    current_line += t.value
    if debug: print "scanner saw other chars:", t.value

def t_code_NL_TOK(t):
    r'(\r)?\n([ \t]*(\#.*)?(\r)?\n)*[ \t]*'
    global current_line
    if current_line:
        code.append(current_line)
        current_line = ''
    indent = count_indent(t.value[t.value.rindex('\n') + 1:])
    if debug: print "scanner saw nl:", t.value, "new indent is", indent
    if indent < code_indent_level and code_nesting_level == 0:
        t.lexer.skip(-len(t.value))
        t.type = 'CODE_TOK'
        t.value = tuple(code), tuple(plan_vars_needed), code_lineno, code_lexpos
        if debug: print "scanner begin('INITIAL')"
        t.lexer.begin('INITIAL')
        return t
    t.lexer.lineno += t.value.count('\n')
    current_line = ' ' * (indent - code_indent_level)

# strings:
def t_tsqstring(t):
    r"[uU]?[rR]?'''([^\\]|\\.)*?'''"
    #t.value = unquote(t.value[3:-3])
    t.type = 'STRING_TOK'
    t.lexer.lineno += t.value.count('\n')
    return t

def t_tdqstring(t):
    r'[uU]?[rR]?"""([^\\]|\\.)*?"""'
    #t.value = unquote(t.value[3:-3])
    t.type = 'STRING_TOK'
    t.lexer.lineno += t.value.count('\n')
    return t

def t_sqstring(t):
    r"[uU]?[rR]?'([^'\\\n\r]|\\.|\\(\r)?\n)*?'"
    #t.value = unquote(t.value[1:-1])
    t.lexer.lineno += t.value.count('\n')
    t.type = 'STRING_TOK'
    return t

def t_dqstring(t):
    r'[uU]?[rR]?"([^"\\\n\r]|\\.|\\(\r)?\n)*?"'
    #t.value = unquote(t.value[1:-1])
    t.type = 'STRING_TOK'
    t.lexer.lineno += t.value.count('\n')
    return t
# end strings

def t_ANONYMOUS_VAR_TOK(t):
    r'\$_([a-zA-Z_][a-zA-Z0-9_]*)?'
    t.value = "'" + t.value[1:] + "'"
    return t

def t_PATTERN_VAR_TOK(t):
    r'\$[a-zA-Z_][a-zA-Z0-9_]*'
    t.value = "'" + t.value[1:] + "'"
    return t

def t_IDENTIFIER_TOK(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in keywords: t.type = t.value.upper() + '_TOK'
    return t

# numbers:
def t_float(t):
    r'[-+]?([0-9]+(\.[0-9]*([eE][-+][0-9]+)?|[eE][-+][0-9]+)|\.[0-9]+([eE][-+][0-9]+)?)'
    t.value = float(t.value)
    t.type = 'NUMBER_TOK'
    return t

def t_hexint(t):
    r'[-+]?0[xX][0-9a-fA-F]+'
    t.value = int(t.value, 16)
    t.type = 'NUMBER_TOK'
    return t

def t_octalint(t):
    r'[-+]?0[0-7]*'
    t.value = int(t.value, 8)
    t.type = 'NUMBER_TOK'
    return t

def t_int(t):
    r'[-+]?[1-9][0-9]*'
    t.value = int(t.value)
    t.type = 'NUMBER_TOK'
    return t
# end numbers

nesting_level = 0

def t_LB_TOK(t):
    r'\['
    global nesting_level
    nesting_level += 1
    #return t

def t_LC_TOK(t):
    r'\{'
    global nesting_level
    nesting_level += 1
    #return t

def t_LP_TOK(t):
    r'\('
    global nesting_level
    nesting_level += 1
    return t

def t_RB_TOK(t):
    r'\]'
    global nesting_level
    assert nesting_level > 0
    nesting_level -= 1
    #return t

def t_RC_TOK(t):
    r'\}'
    global nesting_level
    assert nesting_level > 0
    nesting_level -= 1
    #return t

def t_RP_TOK(t):
    r'\)'
    global nesting_level
    assert nesting_level > 0
    nesting_level -= 1
    return t

def t_ANY_error(t):
    raise SyntaxError("illegal character %s" % repr(t.value[0]),
                      syntaxerror_params(t.lexpos))

# helper functions:

def count_indent(s):
    r'''
        >>> count_indent('')
        0
        >>> count_indent('   ')
        3
        >>> count_indent('\t')
        8
        >>> count_indent('\t ')
        9
        >>> count_indent('\t\t')
        16
        >>> count_indent('   \t')
        8
        >>> count_indent('       \t')
        8
        >>> count_indent('        \t')
        16
    '''
    ans = 0
    for c in s:
        if c == '\t': ans = (ans + 8) & ~7
        else: ans += 1
    return ans

escapes = {
    'a': '\a',
    'b': '\b',
    'f': '\f',
    'n': '\n',
    'r': '\r',
    't': '\t',
    'v': '\v',
    '\\': '\\',
    '\'': '\'',
    '\"': '\"',
}

def unquote(s):
    start = 0
    ans = []
    i = s.find('\\', start)
    while i >= 0:
        ans.append(s[start:i])
        e = escapes.get(s[i+1])
        if e:                   # single char escape code
            ans.append(e)
            start = i + 2
        elif s[i+1] == '\n':    # ignore \ at end of line
            start = i + 2
        elif s[i+1] == '\r':    # ignore \ at end of line
            if s[i+2] == '\n': start = i + 3
            else: start = i + 2
        elif s[i+1:i+3] == 'N{':
            end = s.index('}', i + 3)
            ans.append(unicodedata.lookup(s[i+3:end]))
            start = end + 1
        elif s[i+1] == 'u':
            ans.append(unichr(int(s[i+2:i+6], 16)))
            start = i + 6
        elif s[i+1] == 'U':
            ans.append(unichr(int(s[i+2:i+10], 16)))
            start = i + 10
        elif s[i+1] in string.octdigits:
            if s[i+2] not in string.octdigits:
                ans.append(unichr(int(s[i+2:i+3], 8)))
                start = i + 3
            elif s[i+3] not in string.octdigits:
                ans.append(unichr(int(s[i+2:i+4], 8)))
                start = i + 4
            else:
                ans.append(unichr(int(s[i+2:i+5], 8)))
                start = i + 5
        elif s[i+1] == 'x':
            if s[i+3] not in string.hexdigits:
                ans.append(unichr(int(s[i+2:i+3], 16)))
                start = i + 3
            else:
                ans.append(unichr(int(s[i+2:i+4], 16)))
                start = i + 4
        else:
            ans.append(s[i])
            start = i + 1
        i = s.find('\\', start)
    ans.append(s[start:])
    return ''.join(ans)

lexer = lex.lex(debug=0)

class token_iterator(object):
    ''' This is only used for testing the scanner.
    '''
    def __init__(self, input):
        lexer.lineno = 1
        lexer.input(input)
    def __iter__(self): return self
    def next(self):
        t = lex.token()
        if t: return t
        raise StopIteration

def tokenize(s):
    r'''
        >>> tokenize("# This is a comment\n# line 2 of comment\n\n"
        ...          "# comment after blank line\n")
        LexToken(NL_TOK,'\n# line 2 of comment\n\n# comment after blank line\n',1,19)
        >>> tokenize('name1\n    forall   foreach\n           \nname2')
        LexToken(IDENTIFIER_TOK,'name1',1,0)
        LexToken(NL_TOK,'\n',1,5)
        LexToken(INDENT_TOK,'\n    ',2,5)
        LexToken(FORALL_TOK,'forall',2,10)
        LexToken(FOREACH_TOK,'foreach',2,19)
        LexToken(NL_TOK,'\n           \n',2,26)
        LexToken(DEINDENT_TOK,'\n',4,38)
        LexToken(IDENTIFIER_TOK,'name2',4,39)
    '''
    for t in token_iterator(s):
        print t

def tokenize_file(filename = 'TEST/scan_test'):
    r""" Used for testing.

        >>> import os, os.path
        >>> tokenize_file('TEST/scan_test'
        ...               if os.path.split(os.getcwd())[1] == 'krb_compiler'
        ...               else 'krb_compiler/TEST/scan_test')
        LexToken(NL_TOK,'\n# line 2 of comment\n\n# comment after blank line\n',1,19)
        LexToken(IDENTIFIER_TOK,'name1',5,68)
        LexToken(:,':',5,73)
        LexToken(NL_TOK,'\n',5,74)
        LexToken(INDENT_TOK,'\n    ',6,74)
        LexToken(FOREACH_TOK,'foreach',6,79)
        LexToken(NL_TOK,'\n',6,86)
        LexToken(INDENT_TOK,'\n\t',7,86)
        LexToken(LP_TOK,'(',7,88)
        LexToken(NUMBER_TOK,100,7,89)
        LexToken(NUMBER_TOK,64,7,93)
        LexToken(ANONYMOUS_VAR_TOK,"'_'",7,98)
        LexToken(PATTERN_VAR_TOK,"'foo'",7,101)
        LexToken(NUMBER_TOK,256,8,118)
        LexToken(NUMBER_TOK,0,8,124)
        LexToken(RP_TOK,')',8,125)
        LexToken(NL_TOK,'\n',8,126)
        LexToken(NUMBER_TOK,3.1400000000000001,9,129)
        LexToken(NUMBER_TOK,0.98999999999999999,9,134)
        LexToken(NUMBER_TOK,3.0,10,143)
        LexToken(NUMBER_TOK,0.29999999999999999,10,146)
        LexToken(NUMBER_TOK,3,10,149)
        LexToken(IDENTIFIER_TOK,'e6',10,150)
        LexToken(NUMBER_TOK,3.0000000000000001e-06,10,153)
        LexToken(NL_TOK,'\n',10,158)
        LexToken(DEINDENT_TOK,'\n    ',11,158)
        LexToken(ASSERT_TOK,'assert',11,163)
        LexToken(NL_TOK,'\n',11,169)
        LexToken(INDENT_TOK,'\n\t',12,169)
        LexToken(STRING_TOK,"'this is a string'",12,172)
        LexToken(STRING_TOK,'"so is this"',12,191)
        LexToken(STRING_TOK,"'''\n\tand this \\t too'''",12,204)
        LexToken(STRING_TOK,"'should be\\\n        able to do this too'",13,229)
        LexToken(TRUE_TOK,'True',15,278)
        LexToken(NL_TOK,'\n',15,283)
        LexToken(!,'!',16,292)
        LexToken(IDENTIFIER_TOK,'can',16,293)
        LexToken(IDENTIFIER_TOK,'I',17,311)
        LexToken(IDENTIFIER_TOK,'do',17,313)
        LexToken(IDENTIFIER_TOK,'this',17,316)
        LexToken(NL_TOK,'\n',17,320)
        LexToken(IDENTIFIER_TOK,'too',18,329)
        LexToken(NL_TOK,'\n',18,332)
        LexToken(DEINDENT_TOK,'\n',19,332)
        LexToken(DEINDENT_TOK,'\n',19,332)
    """
    with open(filename) as f:
        tokenize(f.read())

def syntaxerror_params(pos = None, lineno = None):
    '''
        Returns (filename, lineno, column, line) for use in as the second
        argument to SyntaxError exceptions.
    '''
    if pos is None: pos = lexer.lexpos
    start = pos
    if lineno is None: lineno = lexer.lineno
    while start > 0 and lexer.lexdata[start] in '\r\n':
        start -= 1
    end = start
    if debug: print "pos", pos, "lineno", lineno, "start", start
    start = max(lexer.lexdata.rfind('\r', 0, start),
                lexer.lexdata.rfind('\n', 0, start)) + 1
    column = pos - start + 1
    end1 = lexer.lexdata.find('\r', end)
    end2 = lexer.lexdata.find('\n', end)
    if end1 < 0: end = end2
    elif end2 < 0: end = end1
    else: end = min(end1, end2)
    if debug: print "start", start, "column", column, "end", end
    return (lexer.filename, lineno, column, lexer.lexdata[start:end])

def init():
    global indent_levels, nesting_level
    indent_levels = []
    nesting_level = 0

def test():
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
