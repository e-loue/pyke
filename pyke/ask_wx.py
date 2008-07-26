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

if __name__ != "__main__":
    # So we don't screw up doctest runs on boxes that don't have wxPython
    # installed...
    import wx
import itertools
import qa_helpers

def review_ans(dlg, ans, review=None):
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
        msg = u'\n\n'.join(review_str for review_test, review_str in review
                                       if matches(ans, review_test))
        if msg:
            dlg2 = wx.MessageDialog(dlg, msg, 'Answer Information',
                                    wx.OK | wx.ICON_INFORMATION)
            dlg2.ShowModal()
            dlg2.Destroy()

def get_answer(question, title, conv_fn=None, test=None, review=None):
    dlg = wx.TextEntryDialog(None, question, title, u'',
                             wx.CENTRE | wx.RESIZE_BORDER | wx.OK)
    while True:
        status = dlg.ShowModal()
        if status != wx.ID_OK:
            raise AssertionError("dlg.ShowModal failed with %d" % status)
        ans = dlg.GetValue()
        try:
            if conv_fn: ans = conv_fn(ans)
            if test: ans = qa_helpers.match(ans, test)
            break
        except ValueError, e:
            err = wx.MessageDialog(dlg,
                                   u"Answer should be %s\nGot %s" %
                                       (e.message, repr(ans)),
                                   u"Error Notification",
                                   wx.OK | wx.ICON_ERROR)
            err.ShowModal()
            err.Destroy()
            dlg.SetValue(u"")
    review_ans(dlg, ans, review)
    dlg.Destroy()
    return ans

def ask_yn(question, review=None):
    dlg = wx.MessageDialog(None, question, 'User Question',
                           wx.YES_NO | wx.ICON_QUESTION)

    status = dlg.ShowModal()
    if status not in (wx.ID_YES, wx.ID_NO):
        raise AssertionError("dlg.ShowModal failed with %d" % status)
    ans = status == wx.ID_YES
    review_ans(dlg, ans, review)
    dlg.Destroy()
    return ans

def ask_integer(question, match=None, review=None):
    return get_answer(question,
                      qa_helpers.match_prompt(match, int, "Enter Integer %s",
                                              'Enter Integer'),
                      conv_fn=qa_helpers.to_int,
                      test=match,
                      review=review)

def ask_float(question, match=None, review=None):
    return get_answer(question,
                      qa_helpers.match_prompt(match, float, "Enter Number %s",
                                              'Enter Number'),
                      conv_fn=qa_helpers.to_float,
                      test=match,
                      review=review)

def ask_number(question, match=None, review=None):
    return get_answer(question,
                      qa_helpers.match_prompt(match, int, "Enter Number %s",
                                              'Enter Number'),
                      conv_fn=qa_helpers.to_number,
                      test=match,
                      review=review)

def ask_string(question, match=None, review=None):
    return get_answer(question,
                      qa_helpers.match_prompt(match, str, "Enter %s",
                                              'User Question'),
                      test=match,
                      review=review)

def ask_select_1(question, alternatives, review=None):
    dlg = wx.SingleChoiceDialog(None, question, u'User Question',
                                [msg for tag, msg in alternatives],
                                wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER |
                                wx.OK)
    status = dlg.ShowModal()
    if status != wx.ID_OK:
        raise AssertionError("dlg.ShowModal failed with %d" % status)
    selection = dlg.GetSelection()
    #print 'Got selection: %s' % str(selection)
    ans = alternatives[selection][0]
    review_ans(dlg, ans, review)
    dlg.Destroy()
    return ans

def ask_select_n(question, alternatives, review=None):
    #dlg = wx.lib.dialogs.MultiChoiceDialog(None, question, u'User Question',
    #                                       [msg for tag, msg in alternatives])
    dlg = wx.MultiChoiceDialog(None, question, u'User Question',
                               [msg for tag, msg in alternatives],
                               wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER |
                               wx.OK)
    status = dlg.ShowModal()
    if status != wx.ID_OK:
        raise AssertionError("dlg.ShowModal failed with %d" % status)
    #selections = dlg.GetValue()
    selections = dlg.GetSelections()
    #print 'Got selections: %s' % str(selections)
    ans = tuple(alternatives[i][0] for i in selections)
    review_ans(dlg, ans, review)
    dlg.Destroy()
    return ans

def test():
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
