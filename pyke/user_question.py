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

r'''
    This uses a parser object which is expected to have the following methods:

        - get_token(check_token=None)
        - parse_match()
        - parse_alternatives()
        - parse_review()
'''

from string import Template

class user_question(object):
    match = None
    review = None
    def __init__(self, format):
        self.format = Template(format)
    def __repr__(self):
        head = "<%s" % self.__class__.__name__
        if self.match: head += self.repr_match()
        head += ": %s" % repr(self.format.template)
        if self.review:
            head += " %s" % ' ! '.join(repr(m) for m, text in self.review)
        return head + ">"
    def repr_match(self):
        return "(%s)" % repr(self.match)
    def parse(self, parser):
        self.parse_args(parser)
        self.review = parser.parse_review()
    def parse_args(self, parser): pass
    def set_question_base(self, question_base):
        self.question_base = question_base
    def get_ask_module(self):
        return self.question_base.get_ask_module()
    def ask(self, format_params):
        ask_fn = getattr(self.get_ask_module(),
                         'ask_' + self.__class__.__name__)
        if self.review:
            review = tuple((match, template.substitute(format_params))
                           for match, template in self.review)
        else:
            review = None
        arg2 = self.prepare_arg2(format_params)
        if arg2:
            return ask_fn(self.format.substitute(format_params), arg2,
                          review=review)
        return ask_fn(self.format.substitute(format_params),
                      review=review)
    def prepare_arg2(self, format_params):
        return self.match


class yn(user_question):
    pass

class match_args(user_question):
    def parse_args(self, parser):
        token, value = parser.get_token()
        if token == 'lparen':
            self.match = parser.parse_match()
            parser.get_token('rparen')
        else:
            parser.push_token()

class integer(match_args): pass
class float(match_args): pass
class number(match_args): pass

class string(match_args): pass

class select_1(user_question):
    def repr_match(self):
        return "(%s)" % ' '.join(repr(t) + ':' for t, text in self.match)
    def parse(self, parser):
        self.match, self.review = parser.parse_alternatives()
    def prepare_arg2(self, format_params):
        return tuple((tag, label.substitute(format_params))
                     for tag, label in self.match)

class select_n(select_1): pass

def test():
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
