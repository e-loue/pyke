# $Id$
# coding=utf-8
# 
# Copyright © 2007-2008 Bruce Frederiksen
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

import pyke

def fc_head(rb_name):
    return (
        "# %s_fc.py" % rb_name,
        "",
        "from __future__ import with_statement",
        "from pyke import contexts, pattern, fc_rule, knowledge_base",
        "",
        "version = %s" % repr(pyke.version)
    )

def bc_head(rb_name):
    return (
        "# %s_bc.py" % rb_name,
        "",
        "from __future__ import with_statement",
        "import itertools",
        "from pyke import contexts, pattern, bc_rule",
        "",
        "version = %s" % repr(pyke.version)
    )

def plan_head(rb_name):
    return (
        "# %s_plans.py" % rb_name,
        "",
        "version = %s" % repr(pyke.version)
    )

def goal(rb_name, rule_name,
         (goal, goal_name, pattern_args, taking, start_lineno, end_lineno),
         pred_plan_lines, python_lines):
    # returns plan_lines, goal_fn_head, goal_fn_tail, goal_decl_lines
    assert goal == 'goal'
    goal_fn_head = (
        "",
        "def %s(rule, arg_patterns, arg_context):" % rule_name,
        ("INDENT", 2),
        "engine = rule.rule_base.engine",
        "patterns = rule.goal_arg_patterns()",
        "if len(arg_patterns) == len(patterns):",
        ("INDENT", 2),
        "context = contexts.bc_context(rule)",
        "try:",
        ("INDENT", 2),
        ("STARTING_LINENO", start_lineno),
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
        ("ENDING_LINENO", end_lineno),
        "POPINDENT",
        "rule.rule_base.num_bc_rules_matched += 1",
    )
    goal_fn_tail = (
        "POPINDENT",
        "POPINDENT",
        "finally:",
        ("INDENT", 2),
        "context.done()",
        "POPINDENT",
        "POPINDENT",
        "POPINDENT",
    )
    if not taking and not pred_plan_lines and not python_lines:
        plan_fn_name = "None"
        plan_lines = ()
    else:
        plan_fn_name = "%s_plans.%s" % (rb_name, rule_name)
        def_start = "def %s" % rule_name
        taking = [line.strip() for line in taking if line.strip()]
        if not taking:
            def_head = def_start + '(context):'
        else:
            if taking[0][0] != '(' or taking[-1][-1] != ')':
                from pyke.krb_compiler import scanner
                end = scanner.lexer.lexpos
                taking_start = scanner.lexer.lexdata.rfind('taking', 0, end)
                if taking_start < 0:
                    raise SyntaxError("'taking' clause: missing parenthesis",
                                      scanner.syntaxerror_params())
                taking_start += len('taking')
                while taking_start < len(scanner.lexdata) and \
                      scanner.lexdata[taking_start].isspace():
                    taking_start += 1
                lineno = scanner.lexer.lineno - \
                         scanner.lexer.lexdata.count('\n', taking_start,
                                                     scanner.lexer.lexpos)
                raise SyntaxError("'taking' clause: missing parenthesis",
                                  scanner.syntaxerror_params(taking_start,
                                                             lineno))
            taking[0] = def_start + "(context, " + taking[0][1:]
            taking[-1] += ':'
            if len(taking) == 1:
                def_head = taking[0]
            else:
                def_head = (taking[0],
                            ('INDENT', 4),
                            tuple(taking[1:]),
                            "POPINDENT",
                           )
        plan_lines = ("",
                      def_head,
                      ('INDENT', 2),
                      pred_plan_lines,
                      python_lines,
                      "POPINDENT",
                     )
    goal_decl_lines = (
        "",
        "bc_rule.bc_rule('%s', This_rule_base, '%s'," % (rule_name, goal_name),
        ("INDENT", 16),
        "%s, %s," % (rule_name, plan_fn_name),
    ) + list_format(pattern_args, "(", "),")
    return plan_lines, goal_fn_head, goal_fn_tail, goal_decl_lines

def add_start(l, start):
    '''
        >>> add_start(('a', 'b', 'c'), '^')
        (0, ['^a', 'b', 'c'])
        >>> add_start(('POPINDENT', ('INDENT', 2), ((('b',), 'c'),),), '^')
        (2, ['POPINDENT', ('INDENT', 2), ((('^b',), 'c'),)])
        >>> add_start((('POPINDENT', ('INDENT', 2)), ((('b',), 'c'),),), '^')
        (1, [('POPINDENT', ('INDENT', 2)), ((('^b',), 'c'),)])
        >>> add_start(('POPINDENT', ('INDENT', 2)), '^')
        (0, ['^', 'POPINDENT', ('INDENT', 2)])
    '''
    ans = list(l)
    for first, x in enumerate(ans):
        if x != 'POPINDENT' and \
           not (isinstance(x, (tuple, list)) and x[0] == 'INDENT'):
            if not isinstance(x, (tuple, list)):
                ans[first] = start + ans[first]
                return first, ans
            f, x2 = add_start(x, start)
            if len(x) == len(x2):
                ans[first] = tuple(x2)
                return first, ans
    first = 0
    ans.insert(first, start)
    return first, ans

def add_end(l, end):
    '''
        >>> add_end(('a', 'b', 'c'), '^')
        (2, ['a', 'b', 'c^'])
        >>> add_end(((((('b',), 'c'),),), 'POPINDENT', ('INDENT', 2)), '^')
        (0, [(((('b',), 'c^'),),), 'POPINDENT', ('INDENT', 2)])
        >>> add_end((((('b',), 'c'),), ('POPINDENT', ('INDENT', 2))), '^')
        (0, [((('b',), 'c^'),), ('POPINDENT', ('INDENT', 2))])
        >>> add_end(('POPINDENT', ('INDENT', 2)), '^')
        (2, ['POPINDENT', ('INDENT', 2), '^'])
    '''
    ans = list(l)
    for last in range(len(ans) - 1, -1, -1):
        x = ans[last]
        if x != 'POPINDENT' and \
           not (isinstance(x, (tuple, list)) and x[0] == 'INDENT'):
            if not isinstance(x, (tuple, list)):
                ans[last] += end
                return last, ans
            e, x2 = add_end(x, end)
            if len(x) == len(x2):
                ans[last] = tuple(x2)
                return last, ans
    last = len(ans)
    ans.insert(last, end)
    return last, ans

def add_brackets(l, start = '(', end = ')'):
    '''
        >>> add_brackets(('a', 'b', 'c'))
        ('(a', ('INDENT', 1), 'b', 'c)', 'POPINDENT')
        >>> add_brackets(('(a', ('INDENT', 1), 'b', 'c)', 'POPINDENT'))
        ('((a', ('INDENT', 1), ('INDENT', 1), 'b', 'c))', 'POPINDENT', 'POPINDENT')
    '''
    if not l: return start + end
    first, ans = add_start(l, start)
    last, ans = add_end(ans, end)
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

def syntax_error(msg, lineno, pos):
    raise SyntaxError(msg, scanner.syntaxerror_params(pos, lineno))

def test():
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
