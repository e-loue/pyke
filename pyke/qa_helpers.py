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


import types
import re
import sys

class regexp(object):
    r'''
        >>> m = regexp(ur'(hi)\s*there', u'the msg', u'the prompt')
        >>> m
        <regexp u'the msg'[the prompt]/(hi)\s*there/>
        >>> m.msg
        u'the msg'
        >>> m.prompt
        u'the prompt'
        >>> m.match(u'hithere')
        u'hi'
    '''
    def __init__(self, regexp, msg=None, prompt=None):
        self.re = re.compile(regexp, re.UNICODE | re.VERBOSE)
        self.pattern = regexp
        self.msg = msg
        self.prompt = prompt

    def __repr__(self):
        if self.msg:
            if self.prompt:
                return '<regexp %r[%s]/%s/>' % \
                       (self.msg, str(self.prompt), self.pattern)
            return '<regexp %r/%s/>' % (self.msg, self.pattern)
        if self.prompt:
            return '<regexp [%s]/%s/>' % (self.prompt, self.pattern)
        return '<regexp /%s/>' % self.pattern

    def __getstate__(self):
        return self.pattern, self.msg, self.prompt

    def __setstate__(self, args):
        self.pattern, self.msg, self.prompt = args
        self.re = re.compile(self.pattern, re.UNICODE | re.VERBOSE)

    def match(self, str):
        m = self.re.match(str)
        if m and m.end() == len(str):
            if m.lastindex > 1: return m.groups()
            if m.lastindex == 1: return m.group(1)
            return str

class qmap(object):
    r'''
        >>> m = qmap(u'y', True)
        >>> m
        <qmap True = u'y'>
        >>> m.test
        u'y'
        >>> m.value
        True
    '''
    def __init__(self, test, value):
        self.test = test
        self.value = value

    def __repr__(self):
        return "<qmap %s = %s>" % (repr(self.value), repr(self.test))

if sys.version_info[0] < 3:
    def urepr(x):
        r'''
            >>> urepr(44)
            u'44'
            >>> tuple(urepr('hi\n'))
            (u"'", u'h', u'i', u'\\', u'n', u"'")
        '''
        if isinstance(x, types.StringTypes):
            return repr(x.encode('utf-8')).decode('utf-8')
        return unicode(x)
else:
    urepr = repr

def to_int(str):
    r'''
        >>> to_int(u' -34')
        -34
        >>> to_int(u' +43')
        43
        >>> to_int(u'43x')
        Traceback (most recent call last):
            ...
        ValueError: illegal integer: '43x'
    '''
    try:
        return int(str)
    except ValueError:
        raise ValueError(u"illegal integer: %s" % urepr(str))

def to_float(str):
    r'''
        >>> str(to_float(u' -34.444'))
        '-34.444'
        >>> str(to_float(u' +43'))
        '43.0'
        >>> to_float(u'43.3.3')
        Traceback (most recent call last):
            ...
        ValueError: illegal floating point number: '43.3.3'
    '''
    try:
        return float(str)
    except ValueError:
        raise ValueError(u"illegal floating point number: %s" % urepr(str))

def to_number(str):
    r'''
        >>> str(to_number(u' -34.444'))
        '-34.444'
        >>> to_number(u' +43')
        43
        >>> to_number(u'43.3.3')
        Traceback (most recent call last):
            ...
        ValueError: illegal number: '43.3.3'
    '''
    try:
        return to_int(str)
    except ValueError:
        try:
            return to_float(str)
        except ValueError:
            raise ValueError(u"illegal number: %s" % urepr(str))

def to_tuple(str, conv_fn=None, test=None, separator=','):
    r'''
        >>> to_tuple(u'1, 2,3', to_int)
        (1, 2, 3)
        >>> to_tuple(u'1, 2.5, -7e3', to_number)
        (1, 2.5, -7000.0)
        >>> to_tuple(u'43', to_number)
        (43,)
        >>> to_tuple(u'1,43.3.3', to_number)
        Traceback (most recent call last):
            ...
        ValueError: illegal number: '43.3.3'
    '''

    def conv_element(elem):
        elem = elem.strip()
        if conv_fn: elem = conv_fn(elem)
        if test: elem = match(elem, test)
        return elem

    return tuple(conv_element(elem) for elem in str.split(separator))

def msg_for(test, type):
    r'''
        >>> msg_for(None, int)
        >>> msg_for(regexp(u'', u'the msg'), int)
        u'the msg'
        >>> msg_for(qmap(44, True), int)
        u'44'
        >>> msg_for(slice(3, 55), int)
        u'between 3 and 55'
        >>> msg_for(slice(None, 55), int)
        u'<= 55'
        >>> msg_for(slice(3, None), int)
        u'>= 3'
        >>> msg_for(slice(None, None), int)
        u''
        >>> msg_for(slice(3, 55), str)
        u'between 3 and 55 characters'
        >>> msg_for(slice(None, 55), str)
        u'<= 55 characters'
        >>> msg_for(slice(3, None), str)
        u'>= 3 characters'
        >>> msg_for(slice(None, None), str)
        u''
        >>> msg_for((slice(3, 5), True), str)
        u'between 3 and 5 characters or True'
        >>> msg_for(True, str)
        u'True'
    '''
    if test is None: return None
    if isinstance(test, regexp): return test.msg
    if isinstance(test, qmap): return msg_for(test.test, type)
    if isinstance(test, slice):
        if test.start is None:
            if test.stop is not None: ans = u"<= %d" % test.stop
            else: ans = u""
        elif test.stop is None:
            ans = u">= %d" % test.start
        else:
            ans = u"between %d and %d" % (test.start, test.stop)
        if (type == str or type == unicode) and ans: ans += u' characters'
        return ans
    if isinstance(test, (tuple, list)):
        return u' or '.join(filter(None, (msg_for(test_i, type)
                                          for test_i in test)))
    return urepr(test)

def match_prompt(test, type, format, default=u''):
    r'''
        >>> match_prompt(None, int, u' [%s] ')
        u''
        >>> match_prompt(regexp(u'', u'', u'the prompt'), int, u' [%s] ')
        u' [the prompt] '
        >>> match_prompt(qmap(44, True), int, u' [%s] ')
        u' [44] '
        >>> match_prompt(slice(3, 55), int, u' [%s] ')
        u' [3-55] '
        >>> match_prompt(slice(None, 55), int, u' [%s] ')
        u' [max 55] '
        >>> match_prompt(slice(3, None), int, u' [%s] ')
        u' [min 3] '
        >>> match_prompt(slice(None, None), int, u' [%s] ', u'foo')
        u'foo'
        >>> match_prompt(slice(3, 55), str, u' [%s] ')
        u' [len: 3-55] '
        >>> match_prompt(slice(None, 55), str, u' [%s] ')
        u' [len <= 55] '
        >>> match_prompt(slice(3, None), str, u' [%s] ')
        u' [len >= 3] '
        >>> match_prompt(slice(None, None), str, u' [%s] ')
        u''
        >>> match_prompt((slice(3, 5), True), str, u' [%s] ')
        u' [len: 3-5 or True] '
        >>> match_prompt(True, str, u' [%s] ')
        u' [True] '
    '''

    def prompt_body(test, type):
        if test is None: return None
        if isinstance(test, regexp): return test.prompt
        if isinstance(test, qmap): return prompt_body(test.test, type)
        if isinstance(test, slice):
            if test.start is None:
                if test.stop is not None:
                    if issubclass(type, types.StringTypes):
                        return u"len <= %d" % test.stop
                    else:
                        return u"max %d" % test.stop
                else: return u""
            elif test.stop is None:
                if issubclass(type, types.StringTypes):
                    return u"len >= %d" % test.start
                else:
                    return u"min %d" % test.start
            else:
                if issubclass(type, types.StringTypes):
                    return u"len: %d-%d" % (test.start, test.stop)
                else:
                    return u"%d-%d" % (test.start, test.stop)
        if isinstance(test, (tuple, list)):
            return u' or '.join(filter(None, (prompt_body(test_i, type)
                                              for test_i in test)))
        return urepr(test)

    body = prompt_body(test, type)
    if body: return format % body
    return default

def match(ans, test):
    r'''
        >>> match(u'foobar', None)
        u'foobar'
        >>> match(u'hithere', regexp(ur'(hi)\s*there', u'hi there'))
        u'hi'
        >>> match(u'hi mom', regexp(ur'(hi)\s*there', u'hi there'))
        Traceback (most recent call last):
            ...
        ValueError: hi there
        >>> match(u'y', qmap(u'y', True))
        True
        >>> match(2, qmap(slice(3, 5), True))
        Traceback (most recent call last):
            ...
        ValueError: between 3 and 5
        >>> match(3, slice(3,5))
        3
        >>> match(2, slice(3,5))
        Traceback (most recent call last):
            ...
        ValueError: between 3 and 5
        >>> match(2, (slice(3,5), slice(5,10), 2))
        2
        >>> match(2, 2)
        2
    '''
    if test is None: return ans
    if isinstance(test, regexp):
        ans = test.match(ans)
        if ans is not None: return ans
    if isinstance(test, qmap):
        match(ans, test.test)   # raises ValueError if it doesn't match
        return test.value
    elif isinstance(test, slice):
        if isinstance(ans, types.StringTypes): value = len(ans)
        else: value = ans
        if (test.start is None or value >= test.start) and \
           (test.stop is None or value <= test.stop):
            return ans
    elif isinstance(test, (tuple, list)):
        for test_i in test:
            try:
                return match(ans, test_i)
            except ValueError:
                pass
    elif test == ans: return ans
    raise ValueError(msg_for(test, type(ans)))

