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

'''

import itertools
from pyke import contexts

class selector(object):
    def __init__(self):
        self.all = []           # [(pat_context, pattern, link)...]
        self.full_vars = []     # [(pat_context, pattern, [link])...]
        self.partial_vars = []  # [(pat_context, pattern, [link])...]
        self.data = {}          # {data: [link]}
    def add(self, pat_context, pattern, link):
        self.all.append((pat_context, pattern, link))
        if pattern.is_data(pat_context):
            self.data.set_default(pattern.as_data(pat_context), []).append(link)
        else:
            self.vars # FIX ??
    def gen_subset(self, pat_context, pattern):
        ''' yields links without binding any pattern variables.
        '''
        if pattern.is_data(pat_context):
            for link in self.data[pattern.as_data(pat_context)]: yield link
        else:
            for p_c, p, links in self.full_vars:
                for link in links: yield link
            if not isinstance(pattern, contexts.variable):
                self.partial_vars # FIX subsets
    def gen_match(self, pat_context, pattern):
        ''' yields links binding pattern variables.
        '''
        if pattern.is_data(pat_context):
            for link in self.data[pattern.as_data(pat_context)]: yield link
        elif isinstance(pattern, contexts.variable):
            self.all # FIX all
        else:
            self.partial_vars # FIX matches
            self.full_vars # FIX all

class cache_args(object):
    def __init__(self):
        self.args_list = []     # [(pat_context, (pattern...))...]
        self.hashes = {}        # (len, (index...)): (other_indices,
                                #       {(arg...): [other_args_from_factn...]})
    def reset(self):
        self.args_list = []
        self.hashes.clear()
    def lookup(self, bindings, pat_context, patterns):
        """ Binds patterns to successive facts, yielding None for each
            successful match.  Undoes bindings upon continuation, so that no
            bindings remain at StopIteration.
        """
        indices = tuple(enum for enum in enumerate(patterns)
                             if enum[1].is_data(pat_context))
        other_indices, other_arg_lists = \
            self._get_hashed(len(patterns),
                             tuple(index[0] for index in indices),
                             tuple(index[1].as_data(pat_context)
                                   for index in indices))
        if other_arg_lists:
            for args in other_arg_lists:
                mark = bindings.mark(True)
                try:
                    if all(itertools.imap(lambda i, arg:
                                            patterns[i].match_data(bindings,
                                                                   pat_context,
                                                                   arg),
                                          other_indices,
                                          args)):
                        bindings.end_save_all_undo()
                        yield
                    else:
                        bindings.end_save_all_undo()
                finally:
                    bindings.undo_to_mark(mark)
    def _get_hashed(self, len, indices, args):
        ans = self.hashes.get((len, indices))
        if ans is None: ans = self._hash(len, indices)
        other_indices, arg_map = ans
        return other_indices, arg_map.get(args, ())
    def _hash(self, length, indices):
        args_hash = {}
        new_entry = (tuple(i for i in range(length) if i not in indices),
                     args_hash)
        self.hashes[length, indices] = new_entry
        for args in itertools.chain(self.universal_facts,
                                    self.case_specific_facts):
            if len(args) == length:
                selected_args = tuple(arg for i, arg in enumerate(args)
                                          if i in indices)
                args_hash.setdefault(selected_args, []) \
                         .append(tuple(arg for i, arg in enumerate(args)
                                           if i not in indices))
        return new_entry
    def add_universal_fact(self, args):
        assert args not in self.case_specific_facts, \
               "add_universal_fact: fact already present as specific fact"
        if args not in self.universal_facts:
            self.universal_facts.append(args)
            self.add_args(args)
    def add_case_specific_fact(self, args):
        if args not in self.universal_facts and \
           args not in self.case_specific_facts:
            self.case_specific_facts.append(args)
            self.add_args(args)
            for fc_rule, foreach_index in self.fc_rule_refs:
                fc_rule.new_fact(args, foreach_index)
    def add_args(self, args):
        for (length, indices), (other_indices, arg_map) \
         in self.hashes.iteritems():
            if length == len(args):
                selected_args = tuple(arg for i, arg in enumerate(args)
                                          if i in indices)
                arg_map.setdefault(selected_args, []) \
                       .append(tuple(arg for i, arg in enumerate(args)
                                         if i not in indices))

def test():
    import doctest
    import sys
    # FIX sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
