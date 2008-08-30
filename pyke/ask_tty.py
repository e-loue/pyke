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
    A "match" here is one of:
        - an instance of qa_helpers.regexp
            - msg (for error message)
            - prompt (without the [])
            - match(str) returns converted value (None if no match)
        - an instance of qa_helpers.map
            - test (a match)
            - value (value to use)
        - an instance of slice (step must be None)
        - a tuple of matches (implied "or")
        - some other python value (which stands for itself)

    A "review" here is a tuple of (match, review_string)

    "Alternatives" here is a tuple of (tag, label_string)
'''

import itertools
import qa_helpers

encoding = 'UTF-8'

# The answer has been converted to lowercase before these matches:
yes_match = ('y', 'yes', 't', 'true')
no_match = ('n', 'no', 'f', 'false')

def get_answer(question, match_prompt, conv_fn=None, test=None, review=None):
    r'''
        >>> from StringIO import StringIO
        >>> import sys
        >>> sys.stdin = StringIO('4\n')
        >>> get_answer(u'enter number?', '[0-10]', qa_helpers.to_int,
        ...            slice(3,5))
        ______________________________________________________________________________
        enter number? [0-10] 4
        >>> sys.stdin = StringIO('2\n4\n')
        >>> get_answer(u'enter number?', '\n[0-10]', qa_helpers.to_int,
        ...            slice(3,5))
        ______________________________________________________________________________
        enter number?
        [0-10] answer should be between 3 and 5, got 2
        <BLANKLINE>
        Try Again:
        ______________________________________________________________________________
        enter number?
        [0-10] 4
        >>> sys.stdin = StringIO('4\n')
        >>> get_answer(u'enter number?\n', '[0-10]', qa_helpers.to_int, slice(3,5),
        ...            ((3, u'not enough'), (4, u'hurray!'), (5, u'too much')))
        ______________________________________________________________________________
        enter number?
        [0-10] hurray!
        4
    '''
    if not question[-1].isspace() and \
       (not match_prompt or not match_prompt[0].isspace()):
        question += ' '
    question += match_prompt
    if match_prompt and not match_prompt[-1].isspace(): question += ' '
    if encoding: question = question.encode(encoding)
    while True:
        print "_" * 78
        ans = raw_input(question)
        try:
            if encoding: ans = ans.decode(encoding)
            if conv_fn: ans = conv_fn(ans)
            if test: ans = qa_helpers.match(ans, test)
            break
        except ValueError, e:
            print "answer should be %s, got %s" % (e.message, repr(ans))
            print
            print "Try Again:"
    if review:
        def matches2(ans, test):
            try:
                qa_helpers.match(ans, test)
                return True
            except ValueError:
                return False
        def matches(ans, test):
            if isinstance(ans, (tuple, list)):
                return any(itertools.imap(lambda elem: matches2(elem, test),
                                          ans))
            return matches2(ans, test)
        for review_test, review_str in review:
            if matches(ans, review_test):
                print review_str
    return ans

def ask_yn(question, review=None):
    r'''
        >>> from StringIO import StringIO
        >>> import sys
        >>> sys.stdin = StringIO('yes\n')
        >>> ask_yn(u'got it?')
        ______________________________________________________________________________
        got it? (y/n) True
        >>> sys.stdin = StringIO('N\n')
        >>> ask_yn(u'got it?')
        ______________________________________________________________________________
        got it? (y/n) False
    '''
    return get_answer(question, u"(y/n)", conv_fn=lambda str: str.lower(),
                      test=(qa_helpers.map(yes_match, True),
                            qa_helpers.map(no_match, False)),
                      review=review)

def ask_integer(question, match=None, review=None):
    r'''
        >>> from StringIO import StringIO
        >>> import sys
        >>> sys.stdin = StringIO('4\n')
        >>> ask_integer(u'enter number?')
        ______________________________________________________________________________
        enter number? (int) 4
    '''
    return get_answer(question, qa_helpers.match_prompt(match, int, u"[%s]",
                                                        u'(int)'),
                      conv_fn=qa_helpers.to_int,
                      test=match,
                      review=review)

def ask_float(question, match=None, review=None):
    r'''
        >>> from StringIO import StringIO
        >>> import sys
        >>> sys.stdin = StringIO('4\n')
        >>> ask_float(u'enter number?')
        ______________________________________________________________________________
        enter number? (float) 4.0
    '''
    return get_answer(question, qa_helpers.match_prompt(match, float, u"[%s]",
                                                        u'(float)'),
                      conv_fn=qa_helpers.to_float,
                      test=match,
                      review=review)

def ask_number(question, match=None, review=None):
    r'''
        >>> from StringIO import StringIO
        >>> import sys
        >>> sys.stdin = StringIO('4\n')
        >>> ask_number(u'enter number?')
        ______________________________________________________________________________
        enter number? (number) 4
    '''
    return get_answer(question, qa_helpers.match_prompt(match, int, u"[%s]",
                                                        u'(number)'),
                      conv_fn=qa_helpers.to_number,
                      test=match,
                      review=review)

def ask_string(question, match=None, review=None):
    r'''
        >>> from StringIO import StringIO
        >>> import sys
        >>> sys.stdin = StringIO('yes\n')
        >>> ask_string(u'enter string?')
        ______________________________________________________________________________
        enter string? u'yes'
    '''
    return get_answer(question, qa_helpers.match_prompt(match, str, u"[%s]",
                                                        u''),
                      test=match,
                      review=review)

def ask_select_1(question, alternatives, review=None):
    r'''
        >>> from StringIO import StringIO
        >>> import sys
        >>> sys.stdin = StringIO('2\n')
        >>> ask_select_1(u'which one?',
        ...              (('a', u'first one'), ('b', u'second one'),
        ...               ('c', u'third one')))
        ______________________________________________________________________________
        which one?
          1. first one
          2. second one
          3. third one
        ? [1-3] 'b'
    '''
    match = slice(1, len(alternatives))
    question += u''.join(u'\n%3d. %s' %
                             (i + 1, u'\n     '.join(text.split(u'\n')))
                        for i, (tag, text) in enumerate(alternatives))
    i = get_answer(question, qa_helpers.match_prompt(match, int, u"\n? [%s]"),
                   conv_fn=qa_helpers.to_int,
                   test=match,
                   review=review)
    return alternatives[i-1][0]

def ask_select_n(question, alternatives, review=None):
    r'''
        >>> from StringIO import StringIO
        >>> import sys
        >>> sys.stdin = StringIO('1,3\n')
        >>> ask_select_n(u'which one?',
        ...              (('a', u'first one'), ('b', u'second one'),
        ...               ('c', u'third one')))
        ______________________________________________________________________________
        which one?
          1. first one
          2. second one
          3. third one
        ? [1-3, ...] ('a', 'c')
    '''
    match = slice(1, len(alternatives))
    question += u''.join(u'\n%3d. %s' %
                             (i + 1, u'\n     '.join(text.split('\n')))
                        for i, (tag, text) in enumerate(alternatives))
    i_tuple = get_answer(question, qa_helpers.match_prompt(match, int,
                                                           u"\n? [%s, ...]"),
                         conv_fn=lambda str:
                                     qa_helpers.to_tuple(str,
                                         conv_fn=qa_helpers.to_int,
                                         test=match),
                         review=review)
    return tuple(alternatives[i-1][0] for i in i_tuple)

def test():
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
