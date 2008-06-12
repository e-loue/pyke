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

class question(object):
    r'''
        >>> import sys
        >>> from StringIO import StringIO
        >>> sys.stdin = StringIO("44\n")
        >>> fn_name = question("How old is %s",
        ...                    integer_answer(1, 120))
        >>> fn_name("Bob")
        How old is Bob? 44
        >>> sys.stdin = StringIO("444\n")
        >>> fn_name("Bruce")
        Traceback (most recent call last):
           ...
        ValueError: value, 444, greater than maximum, 120
    '''
    def __init__(self, format, answer_type):
        self.format = format
        self.answer_type = answer_type
        self.cache = {}
    def __call__(self, *pos_params, **kw_params):
        if pos_params:
            cache_key = format_params = pos_params
        elif kw_params:
            cache_key = tuple(sorted(kw_params.items(), key=lambda x: x[0]))
            format_params = kw_params
        else:
            cache_key = format_params = None
        if cache_key in self.cache:
            return self.cache[cache_key]
        ans = self.answer_type.ask(self.format % format_params
                                   if format_params
                                   else self.format)
        self.cache[cache_key] = ans
        return ans

class ask_user(object):
    prompt_ans = "? "
    def ask(self, prompt):
        return self.convert(self.get_input(prompt))
    def get_input(self, prompt):
        return raw_input(prompt + self.prompt_ans)

class yn_answer(ask_user):
    r'''
        >>> import sys
        >>> from StringIO import StringIO
        >>> ans = yn_answer()
        >>> sys.stdin = StringIO("y\n")
        >>> ans.ask("prompt")
        prompt (y/n)? True
        >>> sys.stdin = StringIO("no\n")
        >>> ans.ask("prompt")
        prompt (y/n)? False
        >>> sys.stdin = StringIO("bogus\n")
        >>> ans.ask("prompt")
        Traceback (most recent call last):
           ...
        ValueError: incorrect answer: 'bogus'
    '''
    prompt_ans = " (y/n)? "
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
        >>> ans.ask("prompt")
        prompt? -10
        >>> sys.stdin = StringIO("10\n")
        >>> ans.ask("prompt")
        prompt? 10
        >>> sys.stdin = StringIO("-11\n")
        >>> ans.ask("prompt")
        Traceback (most recent call last):
           ...
        ValueError: value, -11, less than minimum, -10
        >>> sys.stdin = StringIO("11\n")
        >>> ans.ask("prompt")
        Traceback (most recent call last):
           ...
        ValueError: value, 11, greater than maximum, 10
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
        >>> ans.ask("prompt")
        prompt? 'hi mom!'
        >>> sys.stdin = StringIO("\n")
        >>> ans.ask("prompt")
        prompt? ''
        >>> ans = string_answer(r'hi ([a-zA-Z]+)')
        >>> sys.stdin = StringIO("hi mom\n")
        >>> ans.ask("prompt")
        prompt? 'mom'
        >>> sys.stdin = StringIO("bye mom\n")
        >>> ans.ask("prompt")
        Traceback (most recent call last):
           ...
        ValueError: invalid response: 'bye mom'
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
        >>> ans.ask("prompt")
        prompt? 
        1. small
        2. medium
        3. large
        ? 'small'

        >>> sys.stdin = StringIO("2\n")
        >>> ans.ask("prompt")
        prompt? 
        1. small
        2. medium
        3. large
        ? 'average'

        >>> sys.stdin = StringIO("3\n")
        >>> ans.ask("prompt")
        prompt? 
        1. small
        2. medium
        3. large
        ? 'large'

        >>> sys.stdin = StringIO("0\n")
        >>> ans.ask("prompt")
        Traceback (most recent call last):
           ...
        ValueError: answer, 0, must be between 1 and 3
    '''
    def __init__(self, *choices):
        def get(n, x):
            if isinstance(x, (tuple, list)): return x[n]
            return x
        self.choice_prompts = tuple(map(functools.partial(get, 0), choices))
        self.choice_answers = tuple(map(functools.partial(get, 1), choices))
    def get_input(self, prompt):
        print prompt + self.prompt_ans
        for i, choice_prompt in enumerate(self.choice_prompts):
            print "%d. %s" % (i + 1, choice_prompt)
        return raw_input(self.prompt_ans)
    def convert(self, text):
        ans = int(text)
        if ans < 1 or ans > len(self.choice_answers):
            raise ValueError("answer, %d, must be between 1 and %d" %
                             (ans, len(self.choice_answers)))
        return self.choice_answers[ans - 1]

def test():
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
