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

""" See http://www.dabeaz.com/ply/ply.html for syntax of grammer definitions.
""" 

from __future__ import with_statement
import itertools
from ply import yacc
from pyke.krb_compiler import scanner

tokens = scanner.tokens

def p_file(p):
    ''' file : nls_opt parent_opt fc_rules bc_rules_opt
    '''
    p[0] = ('file', p[2], (tuple(p[3]), ()), p[4])

def p_file_fc_extras(p):
    ''' file : nls_opt parent_opt fc_rules fc_extras bc_rules_opt
    '''
    p[0] = ('file', p[2], (tuple(p[3]), p[4]), p[5])

def p_file_bc(p):
    ''' file : nls_opt parent_opt bc_rules_section
    '''
    p[0] = ('file', p[2], ((), ()), p[3])

# Uncomment this to generate an error in the grammer.
#def p_bogus(p):
#    ''' file : nls_opt parent_opt bc_rules_opt
#    '''
#    p[0] = ('file', p[2], ((), ()), p[3])

def p_parent(p):
    ''' parent_opt : EXTENDING_TOK IDENTIFIER_TOK without_opt nls
    '''
    p[0] = ('parent', p[2], tuple(p[3]))

def p_second(p):
    ''' without_opt : WITHOUT_TOK without_names comma_opt
    '''
    p[0] = p[2]

def p_fourth(p):
    ''' when_opt : WHEN_TOK NL_TOK reset_plan_vars INDENT_TOK bc_premises DEINDENT_TOK
    '''
    p[0] = p[5]

def p_reset_plan_vars(p):
    ''' reset_plan_vars :
    '''
    global plan_var, plan_var_number
    plan_var_number = 1
    plan_var = 'plan#%d' % plan_var_number
    p[0] = None

def p_inc_plan_vars(p):
    ''' inc_plan_vars :
    '''
    global plan_var, plan_var_number
    plan_var_number += 1
    plan_var = 'plan#%d' % plan_var_number
    p[0] = None

def p_fifth(p):
    ''' bc_extras_opt : BC_EXTRAS_TOK NL_TOK start_extra_statements INDENT_TOK python_extras_code nls DEINDENT_TOK
        fc_extras : FC_EXTRAS_TOK NL_TOK start_extra_statements INDENT_TOK python_extras_code nls DEINDENT_TOK
        plan_extras_opt : PLAN_EXTRAS_TOK NL_TOK start_extra_statements INDENT_TOK python_extras_code nls DEINDENT_TOK
        with_opt : WITH_TOK NL_TOK start_python_statements INDENT_TOK python_plan_code nls DEINDENT_TOK
    '''
    p[0] = p[5]

def p_none(p):
    ''' bc_require_opt :
        comma_opt :
        comma_opt : ','
        colon_opt :
        data : NONE_TOK
        fc_require_opt :
        nls : NL_TOK
        nls : nls NL_TOK
        nls_opt :
        nls_opt : nls
        parent_opt :
        plan_spec : nls
        rest_opt : comma_opt
    '''
    p[0] = None

def p_colon_deprication(p):
    ''' colon_opt : ':'
    '''
    if False:
        import sys
        sys.stderr.write("%s(%d): use of ':' deprecated\n" %
                         (scanner.lexer.filename, p.lineno(1)))
    p[0] = None

def p_fc_rule(p):
    ''' fc_rule : IDENTIFIER_TOK colon_opt NL_TOK INDENT_TOK foreach_opt ASSERT_TOK NL_TOK INDENT_TOK assertions DEINDENT_TOK DEINDENT_TOK
    '''
    p[0] = ('fc_rule', p[1], p[5], tuple(p[9]))

def p_foreach(p):
    ''' foreach_opt : FOREACH_TOK NL_TOK INDENT_TOK fc_premises DEINDENT_TOK
    '''
    p[0] = tuple(p[4])

def p_fc_premise(p):
    ''' fc_premise : IDENTIFIER_TOK '.' IDENTIFIER_TOK LP_TOK patterns_opt RP_TOK nls
    '''
    p[0] = ('fc_premise', p[1], p[3], tuple(p[5]), p.lineno(1), p.lineno(6))

def p_fc_notany(p):
    ''' fc_premise : NOTANY_TOK nls INDENT_TOK fc_premises DEINDENT_TOK
    '''
    p[0] = ('fc_notany', tuple(p[4]), p.lineno(1))

def p_fc_forall(p):
    ''' fc_premise : FORALL_TOK nls INDENT_TOK fc_premises DEINDENT_TOK fc_require_opt
    '''
    p[0] = ('fc_forall', tuple(p[4]), p[6], p.lineno(1), p.linespan(6)[1])

def p_fc_require_opt(p):
    ''' fc_require_opt : REQUIRE_TOK nls INDENT_TOK fc_premises DEINDENT_TOK
    '''
    p[0] = tuple(p[4])

def p_python_eq(p):
    ''' python_premise : pattern start_python_code '=' python_rule_code nls
    '''
    p[0] = ('python_eq', p[1], p[4], p.linespan(1)[0], p.linespan(4)[1])

def p_python_in(p):
    ''' python_premise : pattern start_python_code IN_TOK python_rule_code nls
    '''
    p[0] = ('python_in', p[1], p[4], p.linespan(1)[0], p.linespan(4)[1])

def p_python_check(p):
    ''' python_premise : start_python_code CHECK_TOK python_rule_code nls
    '''
    p[0] = ('python_check', p[3], p.lineno(2), p.linespan(3)[1])

def p_assertion(p):
    ''' assertion : IDENTIFIER_TOK '.' IDENTIFIER_TOK LP_TOK patterns_opt RP_TOK NL_TOK
    '''
    p[0] = ('assert', p[1], p[3], tuple(p[5]), p.lineno(1), p.lineno(6))

def p_python_assertion_n(p):
    ''' assertion : check_nl PYTHON_TOK nls start_python_assertion INDENT_TOK python_rule_code nls DEINDENT_TOK
    '''
    p[0] = ('python_assertion', p[6], p.lineno(2), p.linespan(6)[1])

def p_python_assertion_1(p):
    ''' assertion : check_nl PYTHON_TOK start_python_code NOT_NL_TOK python_rule_code nls
    '''
    p[0] = ('python_assertion', p[5], p.lineno(2), p.linespan(5)[1])

def p_check_nl(p):
    ''' check_nl :
    '''
    scanner.lexer.begin('checknl')
    p[0] = None

def p_bc_rule(p):
    ''' bc_rule : IDENTIFIER_TOK colon_opt NL_TOK INDENT_TOK USE_TOK goal when_opt with_opt DEINDENT_TOK
    '''
    p[0] = ('bc_rule', p[1], p[6], tuple(p[7]), tuple(p[8][0]), tuple(p[8][1]))

def p_empty_bc_rules_opt(p):
    ''' bc_rules_opt :
    '''
    p[0] = ((), (), ())

def p_bc_rules_section(p):
    ''' bc_rules_section : bc_rules bc_extras_opt plan_extras_opt
    '''
    p[0] = (tuple(p[1]), p[2], p[3])

def p_goal(p):
    ''' goal : IDENTIFIER_TOK LP_TOK patterns_opt RP_TOK taking_opt nls
    '''
    p[0] = ('goal', p[1], tuple(p[3]), p[5], p.lineno(1), p.lineno(4))

def p_name_sym(p):
    ''' name : IDENTIFIER_TOK
    '''
    p[0] = repr(p[1])

def p_name_pat_var(p):
    ''' name : PATTERN_VAR_TOK
    '''
    p[0] = "context.lookup_data(%s)" % p[1]

def p_bc_premise1(p):
    ''' bc_premise : name LP_TOK patterns_opt RP_TOK plan_spec
    '''
    p[0] = ('bc_premise', False, None, p[1], tuple(p[3]), p[5],
            p.linespan(1)[0], p.lineno(4))

def p_bc_premise2(p):
    ''' bc_premise : '!' name LP_TOK patterns_opt RP_TOK plan_spec
    '''
    p[0] = ('bc_premise', True, None, p[2], tuple(p[4]), p[6],
            p.lineno(1), p.lineno(5))

def p_bc_premise3(p):
    ''' bc_premise : name '.' name LP_TOK patterns_opt RP_TOK plan_spec
    '''
    p[0] = ('bc_premise', False, p[1], p[3], tuple(p[5]), p[7],
            p.linespan(1)[0], p.lineno(6))

def p_bc_premise4(p):
    ''' bc_premise : '!' name '.' name LP_TOK patterns_opt RP_TOK plan_spec
    '''
    p[0] = ('bc_premise', True, p[2], p[4], tuple(p[6]), p[8],
            p.lineno(1), p.lineno(7))

def p_bc_notany(p):
    ''' bc_premise : NOTANY_TOK nls INDENT_TOK bc_premises DEINDENT_TOK
    '''
    p[0] = ('bc_notany', tuple(p[4]), p.lineno(1))

def p_bc_forall(p):
    ''' bc_premise : FORALL_TOK nls INDENT_TOK bc_premises DEINDENT_TOK bc_require_opt
    '''
    p[0] = ('bc_forall', tuple(p[4]), p[6], p.lineno(1), p.linespan(6)[1])

def p_bc_require_opt(p):
    ''' bc_require_opt : REQUIRE_TOK nls INDENT_TOK bc_premises DEINDENT_TOK
    '''
    p[0] = tuple(p[4])

def p_as(p):
    ''' plan_spec : AS_TOK PATTERN_VAR_TOK nls
    '''
    p[0] = ('as', p[2][1:-1])

def p_step_code(p):
    ''' plan_spec : STEP_TOK NUMBER_TOK nls start_python_plan_call INDENT_TOK python_plan_code nls DEINDENT_TOK
    '''
    p[0] = ('plan_spec', p[2], plan_var, p[6][0], p[6][1],
            p.lineno(1), p.lexpos(1))

def p_code(p):
    ''' plan_spec : nls start_python_plan_call INDENT_TOK python_plan_code nls DEINDENT_TOK
    '''
    p[0] = ('plan_spec', None, plan_var, p[4][0], p[4][1], p[4][2], p[4][3])

def p_start_python_code(p):
    ''' start_python_code :
    '''
    scanner.start_code(var_format = "context.lookup_data('%s')")
    p[0] = None

def p_start_python_plan_call(p):
    ''' start_python_plan_call :
    '''
    scanner.start_code(plan_name = plan_var, multiline = True)
    p[0] = None

def p_start_python_statements(p):
    ''' start_python_statements :
    '''
    scanner.start_code(multiline = True)
    p[0] = None

def p_start_extra_statements(p):
    ''' start_extra_statements :
    '''
    scanner.start_code(multiline = True, var_format = None)
    p[0] = None

def p_start_python_assertion(p):
    ''' start_python_assertion :
    '''
    scanner.start_code(multiline = True,
                       var_format = "context.lookup_data('%s')")
    p[0] = None

def p_python_rule_code(p):
    ''' python_rule_code : CODE_TOK
    '''
    p[0] = p[1]

def p_python_plan_code(p):
    ''' python_plan_code : CODE_TOK
    '''
    p[0] = p[1]

def p_python_extras_code(p):
    ''' python_extras_code : CODE_TOK
    '''
    p[0] = p[1][0]

def p_pattern_var(p):
    ''' variable : PATTERN_VAR_TOK
    '''
    p[0] = "contexts.variable(%s)" % p[1]

def p_anonymous_var(p):
    ''' variable : ANONYMOUS_VAR_TOK
    '''
    p[0] = "contexts.anonymous()"

def p_first(p):
    ''' bc_premise : python_premise
        bc_rules_opt : bc_rules_section
        data : NUMBER_TOK
        data : STRING_TOK
        fc_premise : python_premise
        pattern : pattern_proper
        pattern_proper : variable
        patterns_opt : patterns comma_opt
    '''
    p[0] = p[1]

def p_last(p):
    ''' rest_opt : ',' '*' variable
    '''
    p[0] = p[len(p)-1]

def p_taking(p):
    ''' taking_opt : start_python_code TAKING_TOK python_rule_code
    '''
    p[0] = p[3][0]

def p_quoted_last(p):
    ''' data : IDENTIFIER_TOK
    '''
    p[0] = "'" + p[len(p)-1] + "'"

def p_false(p):
    ''' data : FALSE_TOK
    '''
    p[0] = False

def p_true(p):
    ''' data : TRUE_TOK
    '''
    p[0] = True

def p_start_list(p):
    ''' assertions : assertion
        bc_premises : bc_premise
        bc_rules : bc_rule
        data_list : data
        fc_premises : fc_premise
        fc_rules : fc_rule
        patterns : pattern
        patterns_proper : pattern_proper
        without_names : IDENTIFIER_TOK
    '''
    p[0] = [p[1]]

def p_empty_tuple(p):
    ''' bc_extras_opt :
        data : LP_TOK RP_TOK
        foreach_opt :
        patterns_opt :
        plan_extras_opt :
        taking_opt :
        when_opt :
        without_opt :
    '''
    p[0] = ()

def p_double_empty_tuple(p):
    ''' with_opt :
    '''
    p[0] = (), ()

def p_append_list(p):
    ''' assertions : assertions assertion
        bc_premises : bc_premises inc_plan_vars bc_premise
        bc_rules : bc_rules bc_rule
        data_list : data_list ',' data
        fc_premises : fc_premises fc_premise
        fc_rules : fc_rules fc_rule
        patterns : patterns ',' pattern
        patterns_proper : patterns_proper ',' pattern
        without_names : without_names ',' IDENTIFIER_TOK
    '''
    p[1].append(p[len(p)-1])
    p[0] = p[1]

def p_pattern(p):
    ''' pattern : data '''
    p[0] = "pattern.pattern_literal(%s)" % str(p[1])

def p_pattern_tuple1(p):
    ''' pattern_proper : LP_TOK '*' variable RP_TOK '''
    p[0] = "pattern.pattern_tuple((), %s)" % p[3]

def p_pattern_tuple2(p):
    ''' pattern_proper : LP_TOK data_list ',' '*' variable RP_TOK '''
    p[0] = "pattern.pattern_tuple((%s), %s)" % \
               (' '.join("pattern.pattern_literal(%s)," % str(x) for x in p[2]),
                p[5])

def p_pattern_tuple3(p):
    ''' pattern_proper : LP_TOK data_list ',' patterns_proper rest_opt RP_TOK '''
    p[0] = "pattern.pattern_tuple((%s), %s)" % \
               (' '.join(itertools.chain(("pattern.pattern_literal(%s)," % str(x)
                                           for x in p[2]),
                                         (str(x) + ',' for x in p[4]))),
                p[5])

def p_pattern_tuple4(p):
    ''' pattern_proper : LP_TOK patterns_proper rest_opt RP_TOK '''
    p[0] = "pattern.pattern_tuple((%s), %s)" % \
               (' '.join(str(x) + ',' for x in p[2]),
                p[3])

def p_tuple(p):
    ''' data : LP_TOK data_list comma_opt RP_TOK '''
    p[0] = '(' + ' '.join(str(x) + ',' for x in p[2]) + ')'

def p_error(t):
    raise SyntaxError("invalid syntax",
                      scanner.syntaxerror_params(t.lexpos, t.lineno))

# Use the first line for normal use, the second for testing changes in the
# grammer (the first line does not report grammer errors!).
parser = yacc.yacc(write_tables=0, debug=0)
#parser = yacc.yacc(write_tables=0)

def parse(filename, debug = 0):
    with open(filename) as f:
        scanner.init()
        scanner.lexer.lineno = 1
        scanner.lexer.filename = filename
        scanner.debug = debug
        #parser.restart()
        return parser.parse(f.read(), lexer=scanner.lexer, tracking=True,
                            debug=debug)

def run(filename='TEST/parse_test'):
    r""" Used for testing.

        >>> import os, os.path
        >>> run('TEST/parse_test'
        ...     if os.path.split(os.getcwd())[1] == 'krb_compiler'
        ...     else 'krb_compiler/TEST/parse_test')
        ('file',
         None,
         ((('fc_rule',
            'name1',
            (('fc_premise',
              'a',
              'b',
              ("pattern.pattern_literal('x')", "contexts.variable('b')"),
              7,
              7),),
            (('assert', 'c', 'd', ("contexts.variable('b')",), 9, 9),)),),
          ()),
         ((('bc_rule',
            'name2',
            ('goal',
             'x',
             ('pattern.pattern_literal(1)',
              "contexts.variable('c')",
              "pattern.pattern_literal((1, 'b',))",
              "pattern.pattern_tuple((pattern.pattern_literal(1), pattern.pattern_literal('b'), contexts.variable('c'),), None)"),
             (' (a, b, c)',),
             12,
             12),
            (('bc_premise',
              False,
              "'a'",
              "'b'",
              ("pattern.pattern_literal('x')", "contexts.variable('c')"),
              ('plan_spec',
               None,
               'plan#1',
               ('line1', "line2 (context['d']) end2"),
               ('d',),
               15,
               219),
              14,
              14),
             ('bc_premise',
              False,
              None,
              "'x'",
              ('pattern.pattern_literal(1)',
               'pattern.pattern_literal(2)',
               'pattern.pattern_literal(3)'),
              ('plan_spec',
               None,
               'plan#2',
               ("some (context['plan'])(stuff) \\",
                '                and more stuff fail here'),
               ('plan',),
               18,
               280),
              17,
              17)),
            ("a (context['plan']) b",),
            ('plan',)),
           ('bc_rule',
            'name3',
            ('goal',
             'x',
             ('pattern.pattern_literal(1)',
              "contexts.variable('c')",
              "pattern.pattern_literal((1, 'b',))",
              "pattern.pattern_tuple((pattern.pattern_literal(1), pattern.pattern_literal('b'), contexts.variable('c'),), None)"),
             (),
             24,
             24),
            (('bc_premise',
              False,
              "'a'",
              "'b'",
              ("pattern.pattern_literal('x')", "contexts.variable('c')"),
              ('plan_spec',
               None,
               'plan#1',
               ('line1', "line2 (context['d']) end2"),
               ('d',),
               27,
               452),
              26,
              26),
             ('bc_premise',
              False,
              None,
              "'x'",
              ('pattern.pattern_literal(1)',
               'pattern.pattern_literal(2)',
               'pattern.pattern_literal(3)'),
              ('as', 'foo_fn'),
              29,
              29)),
            (),
            ())),
          (),
          ()))

    """
    import pprint
    pprint.pprint(parse(filename))

def test():
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
