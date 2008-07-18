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


import re
import functools

class pool(object):
    r'''
        Keeps track of a set of questions as a unit.  This lets you, for
        example, reset all of the questions in the pool with a single command.

        Call the instance like a function to create (and register) new
        questions.  These should be assigned to variables for individual
        access.
    '''
    def __init__(self):
        self.questions = []
    def __call__(self, format, answer_type, answer_review = None):
        ans = question(format, answer_type, answer_review)
        self.questions.append(ans)
        return ans
    def reset(self):
        for q in self.questions: q.reset()

class question(object):
    r'''
        >>> import sys
        >>> from StringIO import StringIO
        >>> sys.stdin = StringIO("44\n")
        >>> fn_name = question("How old is %s?",
        ...                    integer_answer(1, 120))
        >>> fn_name("Bob")
        ______________________________________________________________________________
        How old is Bob? 
        44
        >>> sys.stdin = StringIO("444\n120\n")
        >>> fn_name("Bruce")
        ______________________________________________________________________________
        How old is Bruce? value, 444, greater than maximum, 120
        <BLANKLINE>
        Try Again:
        ______________________________________________________________________________
        How old is Bruce? 
        120
    '''
    def __init__(self, format, answer_type, answer_review = None):
        self.format = format
        self.answer_type = answer_type
        self.answer_review = answer_review
        self.cache = {}
    def get_params(self, pos_params, kw_params):
        if pos_params:
            assert not kw_params, \
                   "Can not pass both positional and keyword parameters to a " \
                   "question"
            return pos_params, pos_params
        if kw_params:
            return tuple(sorted(kw_params.items(), key=lambda x: x[0])), \
                   kw_params
        return None, None
    def asked(self, *pos_params, **kw_params):
        cache_key, format_params = self.get_params(pos_params, kw_params)
        return cache_key in self.cache
    def __call__(self, *pos_params, **kw_params):
        cache_key, format_params = self.get_params(pos_params, kw_params)
        if cache_key in self.cache:
            return self.cache[cache_key]
        ans = self.answer_type.ask(self.format, format_params)
        self.cache[cache_key] = ans
        if self.answer_review: self.answer_review.review(ans, format_params)
        print
        return ans
    def reset(self):
        self.cache = {}

class ask_user(object):
    ans_prompt = " "
    def ask(self, prompt, format_params):
        while True:
            print '_' * 78
            try:
                return self.convert(self.get_input(prompt, format_params))
            except ValueError, e:
                print e.message
                print
                print "Try Again:"
    def get_input(self, prompt, format_params):
        if format_params:
            return raw_input(prompt % format_params + self.get_ans_prompt())
        return raw_input(prompt + self.get_ans_prompt())
    def get_ans_prompt(self): return self.ans_prompt

class yn_answer(ask_user):
    r'''
        >>> import sys
        >>> from StringIO import StringIO
        >>> ans = yn_answer()
        >>> sys.stdin = StringIO("y\n")
        >>> ans.ask("prompt?", ())
        ______________________________________________________________________________
        prompt? (y/n) True
        >>> sys.stdin = StringIO("no\n")
        >>> ans.ask("prompt?", ())
        ______________________________________________________________________________
        prompt? (y/n) False
        >>> sys.stdin = StringIO("bogus\nf\n")
        >>> ans.ask("prompt?", ())
        ______________________________________________________________________________
        prompt? (y/n) incorrect answer: 'bogus'
        <BLANKLINE>
        Try Again:
        ______________________________________________________________________________
        prompt? (y/n) False
    '''
    ans_prompt = " (y/n) "
    def __init__(self, yes = ('y', 'yes', 't', 'true'),
                       no = ('n', 'no', 'f', 'false')):
        self.yes = yes
        self.no = no
    def convert(self, text):
        ans = text.lower()
        if ans in self.yes: return True
        if ans in self.no: return False
        raise ValueError("incorrect answer: '%s'" % text) 

class integer_answer(ask_user):
    r'''
        >>> import sys
        >>> from StringIO import StringIO
        >>> ans = integer_answer(-10, 10)
        >>> sys.stdin = StringIO("-10\n")
        >>> ans.ask("prompt?", ())
        ______________________________________________________________________________
        prompt? -10
        >>> sys.stdin = StringIO("10\n")
        >>> ans.ask("prompt?", ())
        ______________________________________________________________________________
        prompt? 10
        >>> sys.stdin = StringIO("-11\n-10\n")
        >>> ans.ask("prompt?", ())
        ______________________________________________________________________________
        prompt? value, -11, less than minimum, -10
        <BLANKLINE>
        Try Again:
        ______________________________________________________________________________
        prompt? -10
        >>> sys.stdin = StringIO("11\n10\n")
        >>> ans.ask("prompt?", ())
        ______________________________________________________________________________
        prompt? value, 11, greater than maximum, 10
        <BLANKLINE>
        Try Again:
        ______________________________________________________________________________
        prompt? 10
    '''
    def __init__(self, min = None, max = None):
        self.min = min
        self.max = max
    def convert(self, text):
        ans = int(text)
        if self.min is not None and ans < self.min:
            raise ValueError("value, %d, less than minimum, %d" %
                             (ans, self.min))
        if self.max is not None and ans > self.max:
            raise ValueError("value, %d, greater than maximum, %d" %
                             (ans, self.max))
        return ans

class string_answer(ask_user):
    r'''
        >>> import sys
        >>> from StringIO import StringIO
        >>> ans = string_answer()
        >>> sys.stdin = StringIO("hi mom!\n")
        >>> ans.ask("prompt?", ())
        ______________________________________________________________________________
        prompt? 'hi mom!'
        >>> sys.stdin = StringIO("\n")
        >>> ans.ask("prompt?", ())
        ______________________________________________________________________________
        prompt? ''
        >>> ans = string_answer(r'hi ([a-zA-Z]+)')
        >>> sys.stdin = StringIO("hi mom\n")
        >>> ans.ask("prompt?", ())
        ______________________________________________________________________________
        prompt? 'mom'
        >>> sys.stdin = StringIO("bye mom\nhi dad\n")
        >>> ans.ask("prompt?", ())
        ______________________________________________________________________________
        prompt? invalid response: 'bye mom'
        <BLANKLINE>
        Try Again:
        ______________________________________________________________________________
        prompt? 'dad'
    '''
    def __init__(self, regexp = None):
        self.re = None if regexp is None else re.compile(regexp)
    def convert(self, text):
        if self.re is None: return text
        m = self.re.match(text)
        if m is None: raise ValueError("invalid response: %s" % repr(text))
        if m.lastindex is None: return m.group(0)
        if m.lastindex == 1: return m.group(1)
        return m.groups()

class multiple_choice(ask_user):
    r'''
        >>> import sys
        >>> from StringIO import StringIO

        >>> ans = multiple_choice('small', ('medium', 'average'), 'large')

        >>> sys.stdin = StringIO("1\n")
        >>> ans.ask("prompt?", ())
        ______________________________________________________________________________
        prompt?
        <BLANKLINE>
          1. small
          2. medium
          3. large
        ? [1-3] 'small'

        >>> sys.stdin = StringIO("2\n")
        >>> ans.ask("prompt?", ())
        ______________________________________________________________________________
        prompt?
        <BLANKLINE>
          1. small
          2. medium
          3. large
        ? [1-3] 'average'

        >>> sys.stdin = StringIO("3\n")
        >>> ans.ask("prompt?", ())
        ______________________________________________________________________________
        prompt?
        <BLANKLINE>
          1. small
          2. medium
          3. large
        ? [1-3] 'large'

        >>> sys.stdin = StringIO("0\n1\n")
        >>> ans.ask("prompt?", ())
        ______________________________________________________________________________
        prompt?
        <BLANKLINE>
          1. small
          2. medium
          3. large
        ? [1-3] answer, 0, must be between 1 and 3
        <BLANKLINE>
        Try Again:
        ______________________________________________________________________________
        prompt?
        <BLANKLINE>
          1. small
          2. medium
          3. large
        ? [1-3] 'small'
    '''
    def __init__(self, *choices):
        def get(n, x):
            if isinstance(x, (tuple, list)): return x[n]
            return x
        self.choice_prompts = tuple(map(functools.partial(get, 0), choices))
        self.choice_answers = tuple(map(functools.partial(get, 1), choices))
    def get_input(self, prompt, format_params):
        if format_params: print prompt % format_params
        else: print prompt
        print
        for i, choice_prompt in enumerate(self.choice_prompts):
            if format_params:
                formatted_choice_prompt = choice_prompt % format_params
            else:
                formatted_choice_prompt = choice_prompt
            prefix = "  %d. " % (i + 1)
            print "%s%s" % (prefix,
                            ('\n' + ' ' * len(prefix))
                            .join(formatted_choice_prompt.split('\n')))
        return raw_input("?" + self.get_ans_prompt())
    def get_ans_prompt(self):
        return " [1-%d] " % len(self.choice_prompts)
    def convert(self, text):
        ans = int(text)
        if ans < 1 or ans > len(self.choice_answers):
            raise ValueError("answer, %d, must be between 1 and %d" %
                             (ans, len(self.choice_answers)))
        return self.choice_answers[ans - 1]

class enumerated_review(object):
    def __init__(self, *answers):
        self.answers = answers
    def review(self, ans, format_params):
        for key, msg in self.answers:
            if ans == key:
                if format_params: print msg % format_params
                else: print msg
                break

def test():
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
