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

from __future__ import with_statement, absolute_import, division

def plan_head1(rb_name):
    return (
        "# %s.py" % rb_name,
        "",
        "from __future__ import with_statement, absolute_import, division",
        "from pyke import contexts, pattern, fc_rule, rule_base",
        "from pyke import lookup, assert_",
        "",
    )

def bc_head(rb_name):
    return (
        "# %s_bc.py" % rb_name,
        "",
        "from __future__ import with_statement, absolute_import, division",
        "from pyke import tmp_itertools as itertools",
        "from pyke import contexts, pattern, bc_rule",
        "from pyke import prove",
        "import %s" % rb_name,
    )

def goal(rb_name, rule_name, (goal, goal_name, pattern_args, using),
         pred_plan_lines, python_lines):
    # returns plan_lines, goal_fn_head, goal_fn_tail, goal_decl_lines
    assert goal == 'goal'
    goal_fn_head = (
        "",
        "def %s(rule, arg_patterns, arg_context):" % rule_name,
        ("INDENT", 2),
        "patterns = rule.goal_arg_patterns()",
        "if len(arg_patterns) == len(patterns):",
        ("INDENT", 2),
        "context = contexts.bc_context(rule)",
        "if all(itertools.imap(lambda pat, arg:",
        ("INDENT", 2),
        ("INDENT", 20),
        ("INDENT", 2),
        "pat.match_pattern(context, context,",
        ("INDENT", 18),
        "arg, arg_context),",
        "POPINDENT",
        "POPINDENT",
        "patterns,",
        "arg_patterns)):",
        "POPINDENT",
    )
    goal_fn_tail = (
        "POPINDENT",
        "context.done()",
        "POPINDENT",
        "POPINDENT",
    )
    if not using and not pred_plan_lines and not python_lines:
        plan_fn_name = "None"
        plan_lines = ()
    else:
        plan_fn_name = "%s.%s" % (rb_name, rule_name)
        def_start = "def %s" % rule_name
        using = [line.strip() for line in using if line.strip()]
        if not using:
            def_head = def_start + '(context):'
        else:
            if using[0][0] != '(' or using[-1][-1] != ')':
                raise SyntaxError("%s.%s: using clause missing parenthesis" %
                                      (rb_name, rule_name))
            using[0] = def_start + "(context, " + using[0][1:]
            using[-1] += ':'
            if len(using) == 1:
                def_head = using[0]
            else:
                def_head = splice(using[0],
                                  (('INDENT', 4),),
                                  tuple(using[1:]),
                                  'POPINDENT')
        plan_lines = splice(
                       "",
                       def_head,
                       (('INDENT', 2),),
                       pred_plan_lines,
                       python_lines,
                       'POPINDENT')
    goal_decl_lines = (
        "",
        "bc_rule.bc_rule('%s', %s.This_rule_base, '%s'," %
            (rule_name, rb_name, goal_name),
        ("INDENT", 16),
        "%s, %s," % (rule_name, plan_fn_name),
    ) + list_format(pattern_args, "(", "),")
    return plan_lines, goal_fn_head, goal_fn_tail, goal_decl_lines

def add_brackets(l, start = '(', end = ')'):
    '''
        >>> add_brackets(('a', 'b', 'c'))
        ('(a', ('INDENT', 1), 'b', 'c)', 'POPINDENT')
        >>> add_brackets(('(a', ('INDENT', 1), 'b', 'c)', 'POPINDENT'))
        ('((a', ('INDENT', 1), ('INDENT', 1), 'b', 'c))', 'POPINDENT', 'POPINDENT')
    '''
    if not l: return (start + end,)
    ans = list(l)
    for first, x in enumerate(ans):
        if x != 'POPINDENT' and \
           not (isinstance(x, (tuple, list)) and x[0] == 'INDENT'):
            ans[first] = start + ans[first]
            break
    else:
        first = 0
        ans.insert(first, start)
    for last in range(len(ans) - 1, -1, -1):
        x = ans[last]
        if x != 'POPINDENT' and \
           not (isinstance(x, (tuple, list)) and x[0] == 'INDENT'):
            ans[last] += end
            break
    else:
        last = len(ans)
        ans.insert(last, end)
    if last > first:
        ans.insert(last + 1, "POPINDENT")
        ans.insert(first + 1, ("INDENT", 1))
    return tuple(ans)

def list_format(l, start, end, separator = ','):
    ans = [element + separator for element in l]
    if not ans: return (start + end,)
    ans[0] = start + ans[0]
    ans[-1] += end
    if len(ans) > 1:
        ans.insert(1, ("INDENT", 1))
        ans.append("POPINDENT")
    return tuple(ans)

def merge_pattern(pattern, pattern_list):
    # returns pat_num, new_pattern_list
    if pattern in pattern_list:
        return list(pattern_list).index(pattern), pattern_list
    return len(pattern_list), pattern_list + (pattern,)

def merge_patterns(patterns, pattern_list):
    # returns pat_nums, new_pattern_list
    pat_nums = []
    for pat in patterns:
        pat_num, pattern_list = merge_pattern(pat, pattern_list)
        pat_nums.append(pat_num)
    return tuple(pat_nums), pattern_list

def splice(*args):
    ans = []
    for arg in args:
        if isinstance(arg, (tuple, list)): ans.extend(arg)
        else: ans.append(arg)
    return tuple(ans)

def test():
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
