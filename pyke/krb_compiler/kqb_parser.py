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
from string import Template
import re
import os.path
from pyke import question_base
from pyke import user_question
from pyke import qa_helpers
from pyke.krb_compiler import scanner

class kqb_parser(object):
    blank_line = re.compile(ur'(\s*#)|(\s*$)', re.UNICODE)
    tokenizer = re.compile(ur''' [ \t\f\r\v]* (?: \#.* )? (?:
            (["']) (?P<str> (?: \\. | .)*? ) \1 |        # this must be first!
            [[] (?P<prompt> (?: \\. | .)*? ) []] |
            [$] (?P<param> [a-zA-Z_] [a-zA-Z_0-9]* ) |
            / (?P<regexp1> (?: \\. | .)*? ) / |
            /// (?P<regexp2> (?: \\. | \n | .)*? ) /// | # FIX: this won't work!
            (?P<const> True | False | None ) |
            (?P<id> [a-zA-Z_] [a-zA-Z_0-9]* ) |
            (?P<number> (?: \d+ (?: \.\d* )? |
                            \.\d+ )
                        (?: [eE][-+]?\d+ )? ) |
            (?P<lparen> [(] ) |
            (?P<rparen> [)] ) |
            (?P<comma> , ) |
            (?P<bar> [|] ) |
            (?P<bang> ! ) |
            (?P<equal> = ) |
            (?P<hyphen> - ) |
            (?P<colon> : ) 
        ) [ \t\f\r\v]* (?: \#.* )? ''', re.UNICODE | re.VERBOSE)
    pushed_token = None
    def __init__(self, f):
        # f needs readline() and name.
        self.f = f
        self.lineno = 0
        self.line = ''
        self.column = 0
        self.eof = False
    def readline(self):
        r'''
            >>> from StringIO import StringIO
            >>> p = kqb_parser(StringIO("""
            ... line 1
            ...     # this should be ignored
            ...  line 2
            ...
            ...   line 3
            ... """))
            >>> p.readline()
            >>> p.indent, p.line, p.lineno, p.column
            (0, 'line 1', 2, 0)
            >>> p.readline()
            >>> p.indent, p.line, p.lineno, p.column
            (1, ' line 2', 4, 1)
            >>> p.readline()
            >>> p.indent, p.line, p.lineno, p.column
            (2, '  line 3', 6, 2)
            >>> p.eof
            False
            >>> p.readline()
            >>> p.eof
            True
        '''
        while True:
            line = self.f.readline()
            if line == '':
                self.eof = True
                break
            self.lineno += 1
            line = line.rstrip('\n')
            if not self.blank_line.match(line):
                self.indent, self.column = scanner.count_indent(line)
                self.line = line
                break
    def SyntaxError(self, msg, last_token=True):
        if last_token:
            raise SyntaxError(msg,
                              (self.f.name, self.last_lineno,
                               self.last_column + 1, self.last_line))
        raise SyntaxError(msg,
                          (self.f.name, self.lineno, self.column + 1,
                           self.line))
    def push_token(self):
        #print "push_token:", self.last_token  # FIX
        self.pushed_token = self.last_token
        self.pushed_indent = self.indent
        self.pushed_column = self.column
        self.indent = self.last_indent
        self.column = self.last_column
    def get_token(self, check_token=None):
        r'''
            >>> from StringIO import StringIO
            >>> f = StringIO(r"""
            ...   line 1=2.5: ( /\s* /, $foo) # comment
            ... ,|!-True  "hi\n"  [mom]
            ... """)
            >>> f.name = 'StringIO'
            >>> p = kqb_parser(f)
            >>> p.get_token()
            ('id', 'line')
            >>> p.get_token()
            ('number', 1)
            >>> p.get_token()
            ('equal', None)
            >>> p.get_token()
            ('number', 2.5)
            >>> p.get_token()
            ('colon', None)
            >>> p.get_token()
            ('lparen', None)
            >>> p.get_token()
            ('regexp', '\\s* ')
            >>> p.get_token()
            ('comma', None)
            >>> p.get_token()
            ('param', 'foo')
            >>> p.get_token()
            ('rparen', None)
            >>> p.get_token()
            ('comma', None)
            >>> p.get_token()
            ('bar', None)
            >>> p.get_token()
            ('bang', None)
            >>> p.get_token()
            ('hyphen', None)
            >>> p.get_token()
            ('const', True)
            >>> p.get_token()
            ('str', 'hi\n')
            >>> p.get_token()
            ('prompt', 'mom')
            >>> p.get_token()
            (None, None)
        '''
        if self.pushed_token:
            ans = self.pushed_token
            self.indent = self.pushed_indent
            self.column = self.pushed_column
            self.pushed_token = self.pushed_column = self.pushed_indent = None
            if check_token and check_token != ans[0]:
                self.SyntaxError("expected %s, got %s" % (check_token, ans[0]))
            #print "get_token: returning pushed_token", ans  # FIX
            return ans
        if self.column < len(self.line): self.skip_spaces()
        if self.column >= len(self.line):
            self.readline()
            if self.eof:
                self.last_token = None, None
                #print "get_token: returning EOF"  # FIX
                return self.last_token
        self.last_line = self.line
        self.last_lineno = self.lineno
        self.last_column = self.column
        self.last_indent = self.indent
        match = self.tokenizer.match(self.line, self.column)
        if not match: self.SyntaxError("Scanner error: no legal token")
        token = match.lastgroup
        chars = match.group(token)
        end = match.end()
        indent, ignore = scanner.count_indent(self.line[self.column:end], True)
        self.indent += indent
        self.column = end
        if token == 'str' or token == 'prompt':
            value = scanner.unquote(chars)
        elif token == 'const':
            value = eval(chars)
        elif token == 'number':
            try:
                value = int(chars)
            except ValueError:
                value = float(chars)
        elif token == 'param' or token == 'id':
            value = chars
        elif token == 'regexp1' or token == 'regexp2':
            # FIX
            token = 'regexp'
            value = chars
            self.lineno += chars.count('\n')
            last_nl = chars.rfind('\n')
            if last_nl >= 0:
                self.column = len(chars) - last_nl + 4
        else:
            value = None
        if check_token and check_token != token:
            self.SyntaxError("expected %s, got %s" % (check_token, token))
        self.last_token = str(token), value
        #print "get_token: returning", self.last_token  # FIX
        return self.last_token
    def get_block_string(self, stop=None, hanging=False, ending_newlines=False):
        r'''
            >>> from StringIO import StringIO
            >>> f = StringIO(r"""
            ...     line 1 # comment
            ...        more stuff
            ...     last line
            ... blah    hanging line 1
            ...
            ...         line 2
            ...           indented
            ...         last line
            ...         ! the end !
            ... """)
            >>> f.name = 'StringIO'
            >>> p = kqb_parser(f)
            >>> p.get_block_string()
            u'line 1 # comment\n   more stuff\nlast line'
            >>> p.column = 4
            >>> p.indent = 4
            >>> p.get_block_string('!', True)
            u'hanging line 1\n\nline 2\n  indented\nlast line'
            >>> f = StringIO(r"""
            ...     ! line 1 # comment
            ...          more stuff
            ...       last line
            ... blah
            ... """)
            >>> f.name = 'StringIO'
            >>> p = kqb_parser(f)
            >>> p.readline()
            >>> p.get_token('bang')
            ('bang', None)
            >>> p.get_block_string(hanging=True)
            u'line 1 # comment\n   more stuff\nlast line'
        '''
        if hanging:
            indent, more_chars = \
                scanner.count_indent(self.line[self.column:])
            self.indent += indent
            self.column += more_chars
        else:
            self.readline()
        indent = self.indent
        if self.eof: self.SyntaxError("expected block string, got EOF", False)
        rest_line = self.line[self.column:]
        if self.blank_line.match(rest_line):
            ans = []
        else:
            ans = [rest_line]
        while not self.eof:
            last_lineno = self.lineno
            self.readline()
            if ending_newlines:
                for i in range(self.lineno - last_lineno - 1): ans.append('')
            if self.eof or self.indent < indent or \
               stop and self.line[self.column:].startswith(stop):
                break
            if not ending_newlines:
                for i in range(self.lineno - last_lineno - 1): ans.append('')
            ans.append(' ' * (self.indent - indent) + self.line[self.column:])
        if not ans: self.SyntaxError("expected block string", False)
        return u'\n'.join(scanner.unquote(str) for str in ans)
    def parse_simple_match(self):
        token, value = self.get_token()
        if token == 'str' or token == 'id' or token == 'number' or \
           token == 'const':
            next_token, next_value = self.get_token()
            if next_token == 'prompt' and token == 'str':
                final_token, final_value = self.get_token('regexp')
                return qa_helpers.regexp(final_value, value, next_value)
            if next_token == 'regexp' and token == 'str':
                return qa_helpers.regexp(next_value, value)
            if next_token == 'equal':
                return qa_helpers.qmap(self.parse_simple_match(), value)
            if next_token == 'hyphen' and token == 'number':
                final_token, final_value = self.get_token()
                if final_token == 'number':
                    return slice(value, final_value)
                self.push_token()
                return slice(value, None)
            self.push_token()
            return value
        if token == 'prompt':
            next_token, next_value = self.get_token('regexp')
            return qa_helpers.regexp(next_value, prompt=value)
        if token == 'lparen':
            ans = self.parse_match()
            self.get_token('rparen')
            return ans
        if token == 'regexp':
            return qa_helpers.regexp(value)
        if token == 'hyphen':
            next_token, next_value = self.get_token('number')
            return slice(None, next_value)
        self.SyntaxError("expected match, got %s" % token)
    def parse_match(self):
        r'''
            >>> from StringIO import StringIO
            >>> def do(str):
            ...    ans = StringIO(str)
            ...    ans.name = 'StringIO'
            ...    return kqb_parser(ans).parse_match()
            >>> do(r'/reg\exp/ bob')
            <regexp /reg\exp/>
            >>> do(r'"msg"/reg\exp/ bob')
            <regexp 'msg'/reg\exp/>
            >>> do(r'[prompt]/reg\exp/ bob')
            <regexp [prompt]/reg\exp/>
            >>> do(r'"msg"[prompt]/reg\exp/ bob')
            <regexp 'msg'[prompt]/reg\exp/>
            >>> do(r"44 = id")
            <qmap 44 = 'id'>
            >>> do(r"-5 bob")
            slice(None, 5, None)
            >>> do(r"0-5 bob")
            slice(0, 5, None)
            >>> do(r"0- bob")
            slice(0, None, None)
            >>> do(r"/regexp/|44|3-5 bob")
            (<regexp /regexp/>, 44, slice(3, 5, None))
            >>> do(r"44 id")
            44
        '''
        ans = [self.parse_simple_match()]
        token, value = self.get_token()
        while token == 'bar':
            ans.append(self.parse_simple_match())
            token, value = self.get_token()
        self.push_token()
        if len(ans) == 1: return ans[0]
        return tuple(ans)
    def get_value(self):
        token, value = self.get_token()
        if token not in ('const', 'number', 'id', 'str'):
            self.SyntaxError("expected value, got %s" % token)
        return value
    def skip_spaces(self, pre_increment=0):
        if pre_increment:
            indent, chars = \
                scanner.count_indent(self.line[self.column:
                                               self.column+pre_increment], True)
            self.indent += indent
            self.column += chars
        indent, chars = scanner.count_indent(self.line[self.column:])
        self.indent += indent
        self.column += chars
    def parse_alternatives(self):
        r'''
            >>> from StringIO import StringIO
            >>> def do(str):
            ...    ans = StringIO(str)
            ...    ans.name = 'StringIO'
            ...    p = kqb_parser(ans)
            ...    alt, review = p.parse_alternatives()
            ...    for tag, msg in alt:
            ...        print '%s: %s' % (repr(tag), repr(msg.template))
            ...    for key, msg in sorted(review, key=lambda x: x[0]):
            ...        print repr(key), '!', repr(msg.template)
            >>> do(r"""
            ...     1: hi mom
            ...        how are you?
            ...        ! Just reward!
            ...     bob: yep this is bob
            ...          ! =1
            ...     44: nope, this is just 44
            ...         ! = bob
            ... next
            ... """)
            1: u'hi mom\nhow are you?'
            'bob': u'yep this is bob'
            44: u'nope, this is just 44'
            (1, 'bob', 44) ! u'Just reward!'
        '''
        if self.column >= len(self.line):
            self.readline()
        if self.eof or self.indent == 0:
            self.SyntaxError("no alternatives", False)
        indent = self.indent
        review = {}
        ans = []
        while not self.eof and self.indent == indent:
            tag = self.get_value()
            if tag in review: self.SyntaxError("duplicate tag: %s" % tag)
            self.get_token('colon')
            ans.append((tag, Template(self.get_block_string(stop='!',
                                                            hanging=True))))
            if self.line[self.column] == '!':
                self.skip_spaces(1)
                if self.line[self.column] == '=':
                    self.indent += 1
                    self.column += 1
                    old_value = self.get_value()
                    while not isinstance(review[old_value], tuple):
                        old_value = review[old_value]
                    review[old_value][0].append(tag)
                    review[tag] = old_value
                    self.readline()
                else:
                    review[tag] = \
                        [tag], Template(self.get_block_string(hanging=True))
        if not self.eof and self.indent > indent:
            self.SyntaxError("unexpected indent", False)
        return tuple(ans), \
               tuple((value[0][0] if len(value[0]) == 1
                                  else tuple(value[0]),
                      value[1])
                     for value in review.itervalues()
                      if isinstance(value, tuple)) \
                  if review \
                  else None
    def parse_review(self):
        r'''
            >>> from StringIO import StringIO
            >>> def do(str):
            ...    ans = StringIO(str)
            ...    ans.name = 'StringIO'
            ...    p = kqb_parser(ans)
            ...    review = p.parse_review()
            ...    for key, msg in sorted(review, key=lambda x: x[0]):
            ...        print repr(key), '!', repr(msg.template)
            >>> do(r"""
            ...     1 ! hi mom
            ...         how are you?
            ...         ! Just reward!
            ...     bob! yep this is bob
            ...     3-5! nope, this is just 44
            ... next
            ... """)
            1 ! u'hi mom\nhow are you?\n! Just reward!'
            slice(3, 5, None) ! u'nope, this is just 44'
            'bob' ! u'yep this is bob'
        '''
        if self.column >= len(self.line):
            self.readline()
        if self.eof or self.indent == 0:
            #print "parse_review: None"  # FIX
            return None
        #print "parse_review: self.indent", self.indent, \
        #      "self.column", self.column   # FIX
        indent = self.indent
        review = []
        while not self.eof and self.indent == indent:
            match = self.parse_match()
            self.get_token('bang')
            review.append(
                (match, Template(self.get_block_string(hanging=True))))
        if not self.eof and self.indent > indent:
            self.SyntaxError("unexpected indent", False)
        #print "parse_review:", tuple(review)   # FIX
        return tuple(review)
    def parse_questions(self):
        r''' question_base.question generator.

            >>> from StringIO import StringIO
            >>> def do(str):
            ...    ans = StringIO(str)
            ...    ans.name = 'StringIO'
            ...    p = kqb_parser(ans)
            ...    for q in p.parse_questions():
            ...        print q
            >>> do(r"""
            ... question1($ans)
            ...     This is the question?
            ...     ---
            ...     $ans = yn
            ...
            ... question2($ans)
            ...     This is the second question?
            ...     ---
            ...     $ans = select_1
            ...         1: first
            ...         2: second
            ...         3: third
            ...
            ... """)
            <question question1($ans): $ans = <yn: u'This is the question?'>>
            <question question2($ans): $ans = <select_1(1: 2: 3:): u'This is the second question?'>>
        '''
        self.readline()
        while not self.eof:
            if self.indent > 0: self.SyntaxError("unexpected indent", False)
            token, name = self.get_token('id')
            self.get_token('lparen')
            params = []
            token, param = self.get_token()
            if token != 'rparen':
                while True:
                    if token != 'param':
                        self.SyntaxError("expected $param, got %s" % token)
                    params.append(param)
                    token, ignore = self.get_token()
                    if token == 'rparen': break
                    if token != 'comma':
                        self.SyntaxError("expected comma or rparen, got %s" %
                                         token)
                    token, param = self.get_token()
            format = self.get_block_string(stop='---', ending_newlines=True)
            self.readline()     # ---
            token, answer_param = self.get_token('param')
            self.get_token('equal')
            token, cls = self.get_token('id')
            user_q = getattr(user_question, cls)(format)
            user_q.parse(self)
            yield question_base.question(name, tuple(params), answer_param,
                                         user_q)
            if self.column >= len(self.line): self.readline()

def parse_kqb(filename):
    dirs, base = os.path.split(filename)
    name = base[:-4]
    with open(filename, 'rU') as f:
        base = question_base.question_base(name)
        parser = kqb_parser(f)
        for question in parser.parse_questions():
            base.add_question(question)
    return base

def test():
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
