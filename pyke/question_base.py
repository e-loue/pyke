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


import contextlib
import unique
from pyke import knowledge_base

class question_base(knowledge_base.knowledge_base):
    r'''
        Each instance keeps track of a related set of questions.
    '''
    def __init__(self, name):
        r'''
            This is only used by the compiler, so only creates an instance
            suitable for pickling.

            Specifically, this means that the self.engine is just set to None
            and the instance is not registered with any engine.
        '''
        super(question_base, self).__init__(None, name, register=False)
    def add_question(self, question):
        name = question.name
        if name in self.entity_lists:
            raise AssertionError("question_base %s: duplicate question, %s" %
                                    (self.name, name))
        self.entity_lists[name] = question
        question.set_knowledge_base(self)
    def get_ask_module(self):
        if hasattr(self, 'ask_module'): return self.ask_module
        return self.engine.get_ask_module()

class question(knowledge_base.knowledge_entity_list):
    r'''
        This represents one question in a question_base.  It takes care of
        lookup parameters and caching and delegates the work of actually
        asking the user a question to the user_question object by calling its
        'ask' method passing the format parameters.
    '''
    not_found = unique.unique('question.not_found')
    def __init__(self, name, params, answer_param, user_question):
        super(question, self).__init__(name)
        self.params = tuple(params)
        self.answer_param = answer_param
        try:
            self.answer_param_position = list(params).index(answer_param)
        except ValueError:
            raise ValueError("question %s: answer parameter, %s, "
                             "not in params list: %s" % (answer_param, params))
        self.input_param_positions = \
            tuple(filter(lambda i: i != self.answer_param_position,
                         range(len(self.params))))
        self.user_question = user_question
        self.cache = {}
    def __repr__(self):
        return "<question %s(%s): $%s = %s>" % \
               (self.name, ', '.join('$' + p for p in self.params),
                self.answer_param, repr(self.user_question))
    def set_knowledge_base(self, question_base):
        self.knowledge_base = question_base
        self.user_question.set_question_base(question_base)
    def lookup(self, bindings, pat_context, patterns):
        input_params = tuple((self.params[i], patterns[i].as_data(pat_context))
                             for i in self.input_param_positions)
        format_params = dict(input_params)
        ans = self.cache.get(input_params, self.not_found)
        if ans is self.not_found:
            ans = self.cache[input_params] = \
                self.user_question.ask(format_params)
        def gen():
            mark = bindings.mark(True)
            end_done = False
            try:
                if patterns[self.answer_param_position] \
                       .match_data(bindings, pat_context, ans):
                    bindings.end_save_all_undo()
                    end_done = True
                    yield
            finally:
                if not end_done: bindings.end_save_all_undo()
                bindings.undo_to_mark(mark)
        return contextlib.closing(gen())
    def reset(self):
        self.cache.clear()


def test():
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
