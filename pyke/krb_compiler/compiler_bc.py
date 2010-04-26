# compiler_bc.py

from __future__ import with_statement
import itertools
from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def file(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                helpers.fc_head(context.lookup_data('rb_name'))):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                  helpers.bc_head(context.lookup_data('rb_name'))):
            context.end_save_all_undo()
            mark3 = context.mark(True)
            if rule.pattern(2).match_data(context, context,
                    helpers.plan_head(context.lookup_data('rb_name'))):
              context.end_save_all_undo()
              flag_4 = False
              with engine.prove(rule.rule_base.root_name, 'rule_decl', context,
                                (rule.pattern(3),
                                 rule.pattern(4),
                                 rule.pattern(5),)) \
                as gen_4:
                for x_4 in gen_4:
                  flag_4 = True
                  assert x_4 is None, \
                    "compiler.file: got unexpected plan from when clause 4"
                  flag_5 = False
                  with engine.prove(rule.rule_base.root_name, 'fc_rules', context,
                                    (rule.pattern(6),
                                     rule.pattern(7),
                                     rule.pattern(8),)) \
                    as gen_5:
                    for x_5 in gen_5:
                      flag_5 = True
                      assert x_5 is None, \
                        "compiler.file: got unexpected plan from when clause 5"
                      flag_6 = False
                      with engine.prove(rule.rule_base.root_name, 'bc_rules', context,
                                        (rule.pattern(3),
                                         rule.pattern(9),
                                         rule.pattern(10),
                                         rule.pattern(11),
                                         rule.pattern(12),)) \
                        as gen_6:
                        for x_6 in gen_6:
                          flag_6 = True
                          assert x_6 is None, \
                            "compiler.file: got unexpected plan from when clause 6"
                          mark7 = context.mark(True)
                          if rule.pattern(13).match_data(context, context,
                                  (context.lookup_data('fc_head'),
                                 context.lookup_data('fc_fun_lines'),
                                 "",
                                 "def populate(engine):",
                                 ('INDENT', 2),
                                 context.lookup_data('decl_line'),
                                 context.lookup_data('fc_init_lines'),
                                 'POPINDENT',
                                 "",
                                 context.lookup_data('fc_extra_lines'),
                                 ) \
                                                         if context.lookup_data('fc_fun_lines') \
                                                         else ()):
                            context.end_save_all_undo()
                            mark8 = context.mark(True)
                            if rule.pattern(14).match_data(context, context,
                                    (context.lookup_data('plan_head'),
                                   context.lookup_data('bc_plan_lines'),
                                   "",
                                   context.lookup_data('plan_extra_lines')) \
                                                           if context.lookup_data('bc_plan_lines') \
                                                           else ()):
                              context.end_save_all_undo()
                              mark9 = context.mark(True)
                              if rule.pattern(15).match_data(context, context,
                                      (context.lookup_data('bc_head'),
                                     ("from %s import %s_plans" %
                                     (context.lookup_data('generated_root_pkg'), context.lookup_data('rb_name'))
                                     if context.lookup_data('bc_plan_lines')
                                     else ()),
                                     context.lookup_data('bc_bc_fun_lines'),
                                     "",
                                     "def populate(engine):",
                                     ('INDENT', 2),
                                     context.lookup_data('decl_line'),
                                     context.lookup_data('bc_bc_init_lines'),
                                     'POPINDENT',
                                     "",
                                     context.lookup_data('bc_extra_lines')) \
                                                             if context.lookup_data('bc_bc_fun_lines') \
                                                             else ()):
                                context.end_save_all_undo()
                                rule.rule_base.num_bc_rule_successes += 1
                                yield
                              else: context.end_save_all_undo()
                              context.undo_to_mark(mark9)
                            else: context.end_save_all_undo()
                            context.undo_to_mark(mark8)
                          else: context.end_save_all_undo()
                          context.undo_to_mark(mark7)
                      if not flag_6:
                        raise AssertionError("compiler.file: 'when' clause 6 failed")
                  if not flag_5:
                    raise AssertionError("compiler.file: 'when' clause 5 failed")
              if not flag_4:
                raise AssertionError("compiler.file: 'when' clause 4 failed")
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def rule_decl(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                "This_rule_base = engine.get_create(%r)" % context.lookup_data('rb_name')):
          context.end_save_all_undo()
          rule.rule_base.num_bc_rule_successes += 1
          yield
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def rule_decl_with_parent(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                "This_rule_base = engine.get_create(%r, %r, %s)" % \
                                        (context.lookup_data('rb_name'), context.lookup_data('parent'),
               tuple(repr(sym) for sym in context.lookup_data('excluded_symbols')))):
          context.end_save_all_undo()
          rule.rule_base.num_bc_rule_successes += 1
          yield
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def fc_rules(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        fc_funs = []
        fc_init = []
        forall91_worked = True
        for python_ans in \
             context.lookup_data('fc_rules'):
          mark2 = context.mark(True)
          if rule.pattern(0).match_data(context, context, python_ans):
            context.end_save_all_undo()
            forall91_worked = False
            flag_3 = False
            with engine.prove(rule.rule_base.root_name, 'fc_rule', context,
                              (rule.pattern(0),
                               rule.pattern(1),
                               rule.pattern(2),)) \
              as gen_3:
              for x_3 in gen_3:
                flag_3 = True
                assert x_3 is None, \
                  "compiler.fc_rules: got unexpected plan from when clause 3"
                fc_funs.append(context.lookup_data('fc_fun_1'))
                fc_init.append(context.lookup_data('fc_init_1'))
                forall91_worked = True
                if forall91_worked: break
            if not flag_3:
              raise AssertionError("compiler.fc_rules: 'when' clause 3 failed")
            if not forall91_worked:
              context.undo_to_mark(mark2)
              break
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        if forall91_worked:
          mark5 = context.mark(True)
          if rule.pattern(3).match_data(context, context,
                  tuple(fc_funs)):
            context.end_save_all_undo()
            mark6 = context.mark(True)
            if rule.pattern(4).match_data(context, context,
                    tuple(fc_init)):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark6)
          else: context.end_save_all_undo()
          context.undo_to_mark(mark5)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def fc_rule_(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        flag_1 = False
        with engine.prove(rule.rule_base.root_name, 'fc_premises', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),
                           rule.pattern(4),
                           rule.pattern(5),
                           rule.pattern(6),
                           rule.pattern(7),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(8),
                           rule.pattern(9),
                           rule.pattern(10),)) \
          as gen_1:
          for x_1 in gen_1:
            flag_1 = True
            assert x_1 is None, \
              "compiler.fc_rule_: got unexpected plan from when clause 1"
            flag_2 = False
            with engine.prove(rule.rule_base.root_name, 'assertions', context,
                              (rule.pattern(11),
                               rule.pattern(12),
                               rule.pattern(10),
                               rule.pattern(13),)) \
              as gen_2:
              for x_2 in gen_2:
                flag_2 = True
                assert x_2 is None, \
                  "compiler.fc_rule_: got unexpected plan from when clause 2"
                mark3 = context.mark(True)
                if rule.pattern(14).match_data(context, context,
                        ("",
                       "def %s(rule, context = None, index = None):" % context.lookup_data('rule_name'),
                       ("INDENT", 2),
                       "engine = rule.rule_base.engine",
                       "if context is None: context = contexts.simple_context()",
                       "try:",
                       ("INDENT", 2),
                       context.lookup_data('prem_fn_head'),
                       context.lookup_data('asserts_fn_lines'),
                       "rule.rule_base.num_fc_rules_triggered += 1",
                       context.lookup_data('prem_fn_tail'),
                       "POPINDENT",
                       "finally:",
                       ("INDENT", 2),
                       "context.done()",
                       "POPINDENT",
                       "POPINDENT",
                       )):
                  context.end_save_all_undo()
                  mark4 = context.mark(True)
                  if rule.pattern(15).match_data(context, context,
                          ("",
                         "fc_rule.fc_rule('%(name)s', This_rule_base, %(name)s," %
                         {'name': context.lookup_data('rule_name')},
                         ("INDENT", 2),
                         helpers.add_brackets(context.lookup_data('prem_decl_lines'), '(', '),'),
                         helpers.list_format(context.lookup_data('patterns_out'), '(', '))'),
                         "POPINDENT",
                         )):
                    context.end_save_all_undo()
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
                  else: context.end_save_all_undo()
                  context.undo_to_mark(mark4)
                else: context.end_save_all_undo()
                context.undo_to_mark(mark3)
            if not flag_2:
              raise AssertionError("compiler.fc_rule_: 'when' clause 2 failed")
        if not flag_1:
          raise AssertionError("compiler.fc_rule_: 'when' clause 1 failed")
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def fc_premises0(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        rule.rule_base.num_bc_rule_successes += 1
        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def fc_premises1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        flag_1 = False
        with engine.prove(rule.rule_base.root_name, 'fc_premise', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),
                           rule.pattern(4),
                           rule.pattern(5),
                           rule.pattern(6),
                           rule.pattern(7),
                           rule.pattern(8),
                           rule.pattern(9),
                           rule.pattern(10),
                           rule.pattern(11),
                           rule.pattern(12),)) \
          as gen_1:
          for x_1 in gen_1:
            flag_1 = True
            assert x_1 is None, \
              "compiler.fc_premises1: got unexpected plan from when clause 1"
            flag_2 = False
            with engine.prove(rule.rule_base.root_name, 'fc_premises', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(13),
                               rule.pattern(14),
                               rule.pattern(4),
                               rule.pattern(5),
                               rule.pattern(15),
                               rule.pattern(16),
                               rule.pattern(9),
                               rule.pattern(17),
                               rule.pattern(18),
                               rule.pattern(12),
                               rule.pattern(19),)) \
              as gen_2:
              for x_2 in gen_2:
                flag_2 = True
                assert x_2 is None, \
                  "compiler.fc_premises1: got unexpected plan from when clause 2"
                mark3 = context.mark(True)
                if rule.pattern(20).match_data(context, context,
                        context.lookup_data('decl_lines1') + context.lookup_data('decl_lines2')):
                  context.end_save_all_undo()
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
                else: context.end_save_all_undo()
                context.undo_to_mark(mark3)
            if not flag_2:
              raise AssertionError("compiler.fc_premises1: 'when' clause 2 failed")
        if not flag_1:
          raise AssertionError("compiler.fc_premises1: 'when' clause 1 failed")
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def fc_premise(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'gen_fc_for', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),
                           rule.pattern(4),
                           rule.pattern(5),
                           rule.pattern(6),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "compiler.fc_premise: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(7).match_data(context, context,
                    (() if context.lookup_data('break_cond') is None
                   else "if %s: break" % context.lookup_data('break_cond'),
                   'POPINDENT',
                   'POPINDENT',),):
              context.end_save_all_undo()
              mark3 = context.mark(True)
              if rule.pattern(8).match_data(context, context,
                      context.lookup_data('clause_num') + 1):
                context.end_save_all_undo()
                mark4 = context.mark(True)
                if rule.pattern(9).match_data(context, context,
                        context.lookup_data('decl_num_in') + 1):
                  context.end_save_all_undo()
                  mark5 = context.mark(True)
                  if rule.pattern(10).match_data(context, context,
                          ("(%r, %r," % (context.lookup_data('kb_name'), context.lookup_data('entity_name')),
                         ('INDENT', 1),
                         helpers.list_format(context.lookup_data('arg_patterns'), '(', '),'),
                         "%s)," % context.lookup_data('multi_match'),
                         "POPINDENT",
                         )):
                    context.end_save_all_undo()
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
                  else: context.end_save_all_undo()
                  context.undo_to_mark(mark5)
                else: context.end_save_all_undo()
                context.undo_to_mark(mark4)
              else: context.end_save_all_undo()
              context.undo_to_mark(mark3)
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def gen_fc_for_false(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                (('STARTING_LINENO', context.lookup_data('start_lineno')),
               "with knowledge_base.Gen_once if index == %d \\" % \
                                       context.lookup_data('decl_num'),
               ('INDENT', 9),
               "else engine.lookup(%r, %r, context," % \
                                         (context.lookup_data('kb_name'), context.lookup_data('entity_name')),
               ('INDENT', 19),
               "rule.foreach_patterns(%d)) \\" % context.lookup_data('decl_num'),
               'POPINDENT',
               'POPINDENT',
               ('INDENT', 2),
               "as gen_%d:" % context.lookup_data('decl_num'),
               "for dummy in gen_%d:" % context.lookup_data('decl_num'),
               ('ENDING_LINENO', context.lookup_data('end_lineno')),
               ('INDENT', 2),
               )):
          context.end_save_all_undo()
          rule.rule_base.num_bc_rule_successes += 1
          yield
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def gen_fc_for_true(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                (('STARTING_LINENO', context.lookup_data('start_lineno')),
               "with engine.lookup(%r, %r, context, \\" % \
                                       (context.lookup_data('kb_name'), context.lookup_data('entity_name')),
               ('INDENT', 19),
               "rule.foreach_patterns(%d)) \\" % context.lookup_data('decl_num'),
               'POPINDENT',
               ('INDENT', 2),
               "as gen_%d:" % context.lookup_data('decl_num'),
               "for dummy in gen_%d:" % context.lookup_data('decl_num'),
               ('ENDING_LINENO', context.lookup_data('end_lineno')),
               ('INDENT', 2))):
          context.end_save_all_undo()
          rule.rule_base.num_bc_rule_successes += 1
          yield
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def fc_first(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                "first%d_worked" % context.lookup_data('clause_num')):
          context.end_save_all_undo()
          flag_2 = False
          with engine.prove(rule.rule_base.root_name, 'fc_premises', context,
                            (rule.pattern(1),
                             rule.pattern(2),
                             rule.pattern(3),
                             rule.pattern(4),
                             rule.pattern(0),
                             rule.pattern(5),
                             rule.pattern(6),
                             rule.pattern(7),
                             rule.pattern(8),
                             rule.pattern(9),
                             rule.pattern(10),
                             rule.pattern(11),
                             rule.pattern(12),)) \
            as gen_2:
            for x_2 in gen_2:
              flag_2 = True
              assert x_2 is None, \
                "compiler.fc_first: got unexpected plan from when clause 2"
              mark3 = context.mark(True)
              if rule.pattern(13).match_data(context, context,
                      "%s = False" % context.lookup_data('break_cond')):
                context.end_save_all_undo()
                mark4 = context.mark(True)
                if rule.pattern(14).match_data(context, context,
                        "%s = True" % context.lookup_data('break_cond')):
                  context.end_save_all_undo()
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
                else: context.end_save_all_undo()
                context.undo_to_mark(mark4)
              else: context.end_save_all_undo()
              context.undo_to_mark(mark3)
          if not flag_2:
            raise AssertionError("compiler.fc_first: 'when' clause 2 failed")
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def fc_forall_None(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        flag_1 = False
        with engine.prove(rule.rule_base.root_name, 'fc_premises', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),
                           rule.pattern(4),
                           rule.pattern(5),
                           rule.pattern(6),
                           rule.pattern(7),
                           rule.pattern(8),
                           rule.pattern(9),
                           rule.pattern(10),
                           rule.pattern(11),
                           rule.pattern(12),)) \
          as gen_1:
          for x_1 in gen_1:
            flag_1 = True
            assert x_1 is None, \
              "compiler.fc_forall_None: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(13).match_data(context, context,
                    context.lookup_data('fn_head1') + context.lookup_data('fn_tail1')):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        if not flag_1:
          raise AssertionError("compiler.fc_forall_None: 'when' clause 1 failed")
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def fc_forall_require(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                "forall%d_worked" % context.lookup_data('start_lineno')):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                  "not forall%d_worked" % context.lookup_data('start_lineno')):
            context.end_save_all_undo()
            flag_3 = False
            with engine.prove(rule.rule_base.root_name, 'fc_premises', context,
                              (rule.pattern(2),
                               rule.pattern(3),
                               rule.pattern(4),
                               rule.pattern(5),
                               rule.pattern(1),
                               rule.pattern(6),
                               rule.pattern(7),
                               rule.pattern(8),
                               rule.pattern(9),
                               rule.pattern(10),
                               rule.pattern(11),
                               rule.pattern(12),
                               rule.pattern(13),)) \
              as gen_3:
              for x_3 in gen_3:
                flag_3 = True
                assert x_3 is None, \
                  "compiler.fc_forall_require: got unexpected plan from when clause 3"
                flag_4 = False
                with engine.prove(rule.rule_base.root_name, 'fc_premises', context,
                                  (rule.pattern(2),
                                   rule.pattern(4),
                                   rule.pattern(14),
                                   rule.pattern(15),
                                   rule.pattern(0),
                                   rule.pattern(6),
                                   rule.pattern(16),
                                   rule.pattern(17),
                                   rule.pattern(10),
                                   rule.pattern(18),
                                   rule.pattern(19),
                                   rule.pattern(13),
                                   rule.pattern(20),)) \
                  as gen_4:
                  for x_4 in gen_4:
                    flag_4 = True
                    assert x_4 is None, \
                      "compiler.fc_forall_require: got unexpected plan from when clause 4"
                    mark5 = context.mark(True)
                    if rule.pattern(21).match_data(context, context,
                            ("forall%d_worked = True" % context.lookup_data('start_lineno'),
                           context.lookup_data('fn_head1'),
                           "forall%d_worked = False" % context.lookup_data('start_lineno'),
                           context.lookup_data('fn_head2'),
                           "forall%d_worked = True" % context.lookup_data('start_lineno'),
                           context.lookup_data('fn_tail2'),
                           context.lookup_data('fn_tail1'),
                           "if forall%d_worked:" % context.lookup_data('start_lineno'),
                           ("INDENT", 2))):
                      context.end_save_all_undo()
                      mark6 = context.mark(True)
                      if rule.pattern(22).match_data(context, context,
                              context.lookup_data('decl_lines1') + context.lookup_data('decl_lines2')):
                        context.end_save_all_undo()
                        rule.rule_base.num_bc_rule_successes += 1
                        yield
                      else: context.end_save_all_undo()
                      context.undo_to_mark(mark6)
                    else: context.end_save_all_undo()
                    context.undo_to_mark(mark5)
                if not flag_4:
                  raise AssertionError("compiler.fc_forall_require: 'when' clause 4 failed")
            if not flag_3:
              raise AssertionError("compiler.fc_forall_require: 'when' clause 3 failed")
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def fc_notany(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                "notany%d_worked" % context.lookup_data('start_lineno')):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                  "not notany%d_worked" % context.lookup_data('start_lineno')):
            context.end_save_all_undo()
            flag_3 = False
            with engine.prove(rule.rule_base.root_name, 'fc_premises', context,
                              (rule.pattern(2),
                               rule.pattern(3),
                               rule.pattern(4),
                               rule.pattern(5),
                               rule.pattern(1),
                               rule.pattern(6),
                               rule.pattern(7),
                               rule.pattern(8),
                               rule.pattern(9),
                               rule.pattern(10),
                               rule.pattern(11),
                               rule.pattern(12),
                               rule.pattern(13),)) \
              as gen_3:
              for x_3 in gen_3:
                flag_3 = True
                assert x_3 is None, \
                  "compiler.fc_notany: got unexpected plan from when clause 3"
                mark4 = context.mark(True)
                if rule.pattern(14).match_data(context, context,
                        ("notany%d_worked = True" % context.lookup_data('start_lineno'),
                       context.lookup_data('fn_head1'),
                       "notany%d_worked = False" % context.lookup_data('start_lineno'),
                       context.lookup_data('fn_tail1'),
                       "if notany%d_worked:" % context.lookup_data('start_lineno'),
                       ("INDENT", 2))):
                  context.end_save_all_undo()
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
                else: context.end_save_all_undo()
                context.undo_to_mark(mark4)
            if not flag_3:
              raise AssertionError("compiler.fc_notany: 'when' clause 3 failed")
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def fc_python_premise(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                context.lookup_data('clause_num') + 1):
          context.end_save_all_undo()
          with engine.prove(rule.rule_base.root_name, 'python_premise', context,
                            (rule.pattern(1),
                             rule.pattern(2),
                             rule.pattern(3),
                             rule.pattern(4),
                             rule.pattern(5),
                             rule.pattern(6),
                             rule.pattern(7),)) \
            as gen_2:
            for x_2 in gen_2:
              assert x_2 is None, \
                "compiler.fc_python_premise: got unexpected plan from when clause 2"
              rule.rule_base.num_bc_rule_successes += 1
              yield
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def assertions_0(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        rule.rule_base.num_bc_rule_successes += 1
        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def assertions_n(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        flag_1 = False
        with engine.prove(rule.rule_base.root_name, 'assertion', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),)) \
          as gen_1:
          for x_1 in gen_1:
            flag_1 = True
            assert x_1 is None, \
              "compiler.assertions_n: got unexpected plan from when clause 1"
            flag_2 = False
            with engine.prove(rule.rule_base.root_name, 'assertions', context,
                              (rule.pattern(4),
                               rule.pattern(5),
                               rule.pattern(3),
                               rule.pattern(6),)) \
              as gen_2:
              for x_2 in gen_2:
                flag_2 = True
                assert x_2 is None, \
                  "compiler.assertions_n: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
            if not flag_2:
              raise AssertionError("compiler.assertions_n: 'when' clause 2 failed")
        if not flag_1:
          raise AssertionError("compiler.assertions_n: 'when' clause 1 failed")
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def assertion(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                \
                           helpers.merge_patterns(context.lookup_data('patterns'), context.lookup_data('patterns_in'))):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                  (('STARTING_LINENO', context.lookup_data('start_lineno')),
                 "engine.assert_(%r, %r," % (context.lookup_data('kb_name'), context.lookup_data('entity_name')),
                 ('INDENT', 15),
                 helpers.list_format(
                 ("rule.pattern(%d).as_data(context)" % pat_num
                 for pat_num in context.lookup_data('pat_nums')),
                 '(', ')),'),
                 ('ENDING_LINENO', context.lookup_data('end_lineno')),
                 "POPINDENT",
                 )):
            context.end_save_all_undo()
            rule.rule_base.num_bc_rule_successes += 1
            yield
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def python_assertion(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        rule.rule_base.num_bc_rule_successes += 1
        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def bc_rules(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        bc_plan_lines = []
        bc_bc_funs = []
        bc_bc_init = []
        forall356_worked = True
        for python_ans in \
             context.lookup_data('bc_rules'):
          mark2 = context.mark(True)
          if rule.pattern(0).match_data(context, context, python_ans):
            context.end_save_all_undo()
            forall356_worked = False
            flag_3 = False
            with engine.prove(rule.rule_base.root_name, 'bc_rule', context,
                              (rule.pattern(1),
                               rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(3),
                               rule.pattern(4),)) \
              as gen_3:
              for x_3 in gen_3:
                flag_3 = True
                assert x_3 is None, \
                  "compiler.bc_rules: got unexpected plan from when clause 3"
                bc_plan_lines.extend(context.lookup_data('bc_plan1'))
                bc_bc_funs.append(context.lookup_data('bc_bc_fun1'))
                bc_bc_init.append(context.lookup_data('bc_bc_init1'))
                forall356_worked = True
                if forall356_worked: break
            if not flag_3:
              raise AssertionError("compiler.bc_rules: 'when' clause 3 failed")
            if not forall356_worked:
              context.undo_to_mark(mark2)
              break
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        if forall356_worked:
          mark5 = context.mark(True)
          if rule.pattern(5).match_data(context, context,
                  tuple(bc_plan_lines)):
            context.end_save_all_undo()
            mark6 = context.mark(True)
            if rule.pattern(6).match_data(context, context,
                    tuple(bc_bc_funs)):
              context.end_save_all_undo()
              mark7 = context.mark(True)
              if rule.pattern(7).match_data(context, context,
                      tuple(bc_bc_init)):
                context.end_save_all_undo()
                rule.rule_base.num_bc_rule_successes += 1
                yield
              else: context.end_save_all_undo()
              context.undo_to_mark(mark7)
            else: context.end_save_all_undo()
            context.undo_to_mark(mark6)
          else: context.end_save_all_undo()
          context.undo_to_mark(mark5)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def bc_rule_(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        flag_1 = False
        with engine.prove(rule.rule_base.root_name, 'bc_premises', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),
                           rule.pattern(4),
                           rule.pattern(5),
                           rule.pattern(6),
                           rule.pattern(7),)) \
          as gen_1:
          for x_1 in gen_1:
            flag_1 = True
            assert x_1 is None, \
              "compiler.bc_rule_: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(8).match_data(context, context,
                    \
                               helpers.goal(context.lookup_data('rb_name'), context.lookup_data('name'), context.lookup_data('goal'),
                   context.lookup_data('prem_plan_lines'), context.lookup_data('python_lines'))):
              context.end_save_all_undo()
              mark3 = context.mark(True)
              if rule.pattern(9).match_data(context, context,
                      (context.lookup_data('goal_fn_head'),
                     context.lookup_data('prem_fn_head'),
                     'rule.rule_base.num_bc_rule_successes += 1',
                     'yield context' if context.lookup_data('plan_lines') else 'yield',
                     context.lookup_data('prem_fn_tail'),
                     'rule.rule_base.num_bc_rule_failures += 1',
                     context.lookup_data('goal_fn_tail'),
                     )):
                context.end_save_all_undo()
                mark4 = context.mark(True)
                if rule.pattern(10).match_data(context, context,
                        (context.lookup_data('goal_decl_lines'),
                       context.lookup_data('prem_decl_lines'),
                       "POPINDENT",
                       )):
                  context.end_save_all_undo()
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
                else: context.end_save_all_undo()
                context.undo_to_mark(mark4)
              else: context.end_save_all_undo()
              context.undo_to_mark(mark3)
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        if not flag_1:
          raise AssertionError("compiler.bc_rule_: 'when' clause 1 failed")
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def bc_premises(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        flag_1 = False
        with engine.prove(rule.rule_base.root_name, 'bc_premises1', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),
                           rule.pattern(4),
                           rule.pattern(5),
                           rule.pattern(6),
                           rule.pattern(7),
                           rule.pattern(8),
                           rule.pattern(9),
                           rule.pattern(10),
                           rule.pattern(11),
                           rule.pattern(12),
                           rule.pattern(13),)) \
          as gen_1:
          for x_1 in gen_1:
            flag_1 = True
            assert x_1 is None, \
              "compiler.bc_premises: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(14).match_data(context, context,
                    helpers.list_format(context.lookup_data('patterns'), '(', '))')):
              context.end_save_all_undo()
              mark3 = context.mark(True)
              if rule.pattern(15).match_data(context, context,
                      ('(' + ' '.join(tuple(repr(plan_var_name) + ','
                     for plan_var_name
                     in context.lookup_data('plan_var_names'))) +
                     '),',) + context.lookup_data('pat_lines')):
                context.end_save_all_undo()
                mark4 = context.mark(True)
                if rule.pattern(16).match_data(context, context,
                        tuple(itertools.chain.from_iterable(itertools.chain(
                       (lines for step, lines in context.lookup_data('plan_lines1') if step is None),
                       (lines for step, lines
                       in sorted(((step, lines) for step, lines in context.lookup_data('plan_lines1')
                       if step is not None),
                       key=lambda t: t[0])))))):
                  context.end_save_all_undo()
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
                else: context.end_save_all_undo()
                context.undo_to_mark(mark4)
              else: context.end_save_all_undo()
              context.undo_to_mark(mark3)
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        if not flag_1:
          raise AssertionError("compiler.bc_premises: 'when' clause 1 failed")
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def bc_premises1_0(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        rule.rule_base.num_bc_rule_successes += 1
        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def bc_premises1_n(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        flag_1 = False
        with engine.prove(rule.rule_base.root_name, 'bc_premise', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),
                           rule.pattern(4),
                           rule.pattern(5),
                           rule.pattern(6),
                           rule.pattern(7),
                           rule.pattern(8),
                           rule.pattern(9),
                           rule.pattern(10),
                           rule.pattern(11),
                           rule.pattern(12),
                           rule.pattern(13),)) \
          as gen_1:
          for x_1 in gen_1:
            flag_1 = True
            assert x_1 is None, \
              "compiler.bc_premises1_n: got unexpected plan from when clause 1"
            flag_2 = False
            with engine.prove(rule.rule_base.root_name, 'bc_premises1', context,
                              (rule.pattern(0),
                               rule.pattern(1),
                               rule.pattern(3),
                               rule.pattern(14),
                               rule.pattern(15),
                               rule.pattern(5),
                               rule.pattern(6),
                               rule.pattern(8),
                               rule.pattern(16),
                               rule.pattern(10),
                               rule.pattern(17),
                               rule.pattern(18),
                               rule.pattern(19),
                               rule.pattern(20),)) \
              as gen_2:
              for x_2 in gen_2:
                flag_2 = True
                assert x_2 is None, \
                  "compiler.bc_premises1_n: got unexpected plan from when clause 2"
                mark3 = context.mark(True)
                if rule.pattern(21).match_data(context, context,
                        context.lookup_data('plan_lines1') + context.lookup_data('plan_lines2')):
                  context.end_save_all_undo()
                  mark4 = context.mark(True)
                  if rule.pattern(22).match_data(context, context,
                          context.lookup_data('fn_head1') + context.lookup_data('fn_head2')):
                    context.end_save_all_undo()
                    mark5 = context.mark(True)
                    if rule.pattern(23).match_data(context, context,
                            context.lookup_data('fn_tail2') + context.lookup_data('fn_tail1')):
                      context.end_save_all_undo()
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
                    else: context.end_save_all_undo()
                    context.undo_to_mark(mark5)
                  else: context.end_save_all_undo()
                  context.undo_to_mark(mark4)
                else: context.end_save_all_undo()
                context.undo_to_mark(mark3)
            if not flag_2:
              raise AssertionError("compiler.bc_premises1_n: 'when' clause 2 failed")
        if not flag_1:
          raise AssertionError("compiler.bc_premises1_n: 'when' clause 1 failed")
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def bc_premise(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                context.lookup_data('clause_num') + 1):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                  context.lookup_data('kb_name') or "rule.rule_base.root_name"):
            context.end_save_all_undo()
            mark3 = context.mark(True)
            if rule.pattern(2).match_data(context, context,
                    \
                               helpers.merge_patterns(context.lookup_data('arg_patterns'), context.lookup_data('patterns_in'))):
              context.end_save_all_undo()
              mark4 = context.mark(True)
              if rule.pattern(3).match_data(context, context,
                      (('STARTING_LINENO', context.lookup_data('start_lineno')),
                     "with engine.prove(%s, %s, context," %
                     (context.lookup_data('kb_name2'), context.lookup_data('entity_name')),
                     ('INDENT', 2),
                     ('INDENT', 16),
                     helpers.list_format(('rule.pattern(%d)' % pat_num
                     for pat_num in context.lookup_data('pat_nums')),
                     '(', ')) \\'),
                     'POPINDENT',
                     "as gen_%d:" % context.lookup_data('clause_num'),
                     "for x_%d in gen_%d:" % (context.lookup_data('clause_num'), context.lookup_data('clause_num')),
                     ('INDENT', 2),
                     )):
                context.end_save_all_undo()
                flag_5 = False
                with engine.prove(rule.rule_base.root_name, 'add_required', context,
                                  (rule.pattern(4),
                                   rule.pattern(5),
                                   rule.pattern(6),
                                   rule.pattern(7),
                                   rule.pattern(3),
                                   rule.pattern(8),
                                   rule.pattern(9),
                                   rule.pattern(10),)) \
                  as gen_5:
                  for x_5 in gen_5:
                    flag_5 = True
                    assert x_5 is None, \
                      "compiler.bc_premise: got unexpected plan from when clause 5"
                    flag_6 = False
                    with engine.prove(rule.rule_base.root_name, 'gen_plan_lines', context,
                                      (rule.pattern(5),
                                       rule.pattern(6),
                                       rule.pattern(7),
                                       rule.pattern(11),
                                       rule.pattern(12),
                                       rule.pattern(13),
                                       rule.pattern(14),
                                       rule.pattern(15),
                                       rule.pattern(16),
                                       rule.pattern(17),
                                       rule.pattern(18),)) \
                      as gen_6:
                      for x_6 in gen_6:
                        flag_6 = True
                        assert x_6 is None, \
                          "compiler.bc_premise: got unexpected plan from when clause 6"
                        mark7 = context.mark(True)
                        if rule.pattern(19).match_data(context, context,
                                helpers.merge_patterns(context.lookup_data('plan_vars_needed'),
                               context.lookup_data('plan_var_names_in'))):
                          context.end_save_all_undo()
                          mark8 = context.mark(True)
                          if rule.pattern(20).match_data(context, context,
                                  context.lookup_data('fn_head2') + context.lookup_data('fn_head3') + (('ENDING_LINENO', context.lookup_data('end_lineno')),)):
                            context.end_save_all_undo()
                            mark9 = context.mark(True)
                            if rule.pattern(21).match_data(context, context,
                                    (context.lookup_data('fn_tail3'),
                                   () if context.lookup_data('break_cond') is None
                                   else "if %s: break" % context.lookup_data('break_cond'),
                                   context.lookup_data('fn_tail2'))):
                              context.end_save_all_undo()
                              rule.rule_base.num_bc_rule_successes += 1
                              yield
                            else: context.end_save_all_undo()
                            context.undo_to_mark(mark9)
                          else: context.end_save_all_undo()
                          context.undo_to_mark(mark8)
                        else: context.end_save_all_undo()
                        context.undo_to_mark(mark7)
                    if not flag_6:
                      raise AssertionError("compiler.bc_premise: 'when' clause 6 failed")
                if not flag_5:
                  raise AssertionError("compiler.bc_premise: 'when' clause 5 failed")
              else: context.end_save_all_undo()
              context.undo_to_mark(mark4)
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def bc_first(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                "first%d_worked" % context.lookup_data('clause_num')):
          context.end_save_all_undo()
          flag_2 = False
          with engine.prove(rule.rule_base.root_name, 'bc_premises1', context,
                            (rule.pattern(1),
                             rule.pattern(2),
                             rule.pattern(3),
                             rule.pattern(4),
                             rule.pattern(5),
                             rule.pattern(0),
                             rule.pattern(6),
                             rule.pattern(7),
                             rule.pattern(8),
                             rule.pattern(9),
                             rule.pattern(10),
                             rule.pattern(11),
                             rule.pattern(12),
                             rule.pattern(13),)) \
            as gen_2:
            for x_2 in gen_2:
              flag_2 = True
              assert x_2 is None, \
                "compiler.bc_first: got unexpected plan from when clause 2"
              flag_3 = False
              with engine.prove(rule.rule_base.root_name, 'add_required', context,
                                (rule.pattern(14),
                                 rule.pattern(1),
                                 rule.pattern(2),
                                 rule.pattern(3),
                                 rule.pattern(12),
                                 rule.pattern(13),
                                 rule.pattern(15),
                                 rule.pattern(16),)) \
                as gen_3:
                for x_3 in gen_3:
                  flag_3 = True
                  assert x_3 is None, \
                    "compiler.bc_first: got unexpected plan from when clause 3"
                  mark4 = context.mark(True)
                  if rule.pattern(17).match_data(context, context,
                          "%s = False" % context.lookup_data('break_cond')):
                    context.end_save_all_undo()
                    mark5 = context.mark(True)
                    if rule.pattern(18).match_data(context, context,
                            "%s = True" % context.lookup_data('break_cond')):
                      context.end_save_all_undo()
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
                    else: context.end_save_all_undo()
                    context.undo_to_mark(mark5)
                  else: context.end_save_all_undo()
                  context.undo_to_mark(mark4)
              if not flag_3:
                raise AssertionError("compiler.bc_first: 'when' clause 3 failed")
          if not flag_2:
            raise AssertionError("compiler.bc_first: 'when' clause 2 failed")
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def bc_forall_None(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        flag_1 = False
        with engine.prove(rule.rule_base.root_name, 'bc_premises1', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),
                           rule.pattern(4),
                           rule.pattern(5),
                           rule.pattern(6),
                           rule.pattern(7),
                           rule.pattern(8),
                           rule.pattern(9),
                           rule.pattern(10),
                           rule.pattern(11),
                           rule.pattern(12),
                           rule.pattern(13),)) \
          as gen_1:
          for x_1 in gen_1:
            flag_1 = True
            assert x_1 is None, \
              "compiler.bc_forall_None: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(14).match_data(context, context,
                    context.lookup_data('fn_head1') + context.lookup_data('fn_tail')):
              context.end_save_all_undo()
              rule.rule_base.num_bc_rule_successes += 1
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark2)
        if not flag_1:
          raise AssertionError("compiler.bc_forall_None: 'when' clause 1 failed")
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def bc_forall_require(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                "forall%d_worked" % context.lookup_data('start_lineno')):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                  "not forall%d_worked" % context.lookup_data('start_lineno')):
            context.end_save_all_undo()
            flag_3 = False
            with engine.prove(rule.rule_base.root_name, 'bc_premises1', context,
                              (rule.pattern(2),
                               rule.pattern(3),
                               rule.pattern(4),
                               rule.pattern(5),
                               rule.pattern(6),
                               rule.pattern(1),
                               rule.pattern(7),
                               rule.pattern(8),
                               rule.pattern(9),
                               rule.pattern(10),
                               rule.pattern(11),
                               rule.pattern(12),
                               rule.pattern(13),
                               rule.pattern(14),)) \
              as gen_3:
              for x_3 in gen_3:
                flag_3 = True
                assert x_3 is None, \
                  "compiler.bc_forall_require: got unexpected plan from when clause 3"
                flag_4 = False
                with engine.prove(rule.rule_base.root_name, 'bc_premises1', context,
                                  (rule.pattern(2),
                                   rule.pattern(3),
                                   rule.pattern(5),
                                   rule.pattern(15),
                                   rule.pattern(16),
                                   rule.pattern(0),
                                   rule.pattern(7),
                                   rule.pattern(9),
                                   rule.pattern(17),
                                   rule.pattern(11),
                                   rule.pattern(18),
                                   rule.pattern(12),
                                   rule.pattern(19),
                                   rule.pattern(20),)) \
                  as gen_4:
                  for x_4 in gen_4:
                    flag_4 = True
                    assert x_4 is None, \
                      "compiler.bc_forall_require: got unexpected plan from when clause 4"
                    mark5 = context.mark(True)
                    if rule.pattern(21).match_data(context, context,
                            ("forall%d_worked = True" % context.lookup_data('start_lineno'),
                           context.lookup_data('fn_head1'),
                           "forall%d_worked = False" % context.lookup_data('start_lineno'),
                           context.lookup_data('fn_head2'),
                           "forall%d_worked = True" % context.lookup_data('start_lineno'),
                           context.lookup_data('fn_tail2'),
                           context.lookup_data('fn_tail1'),
                           "if forall%d_worked:" % context.lookup_data('start_lineno'),
                           ("INDENT", 2))):
                      context.end_save_all_undo()
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
                    else: context.end_save_all_undo()
                    context.undo_to_mark(mark5)
                if not flag_4:
                  raise AssertionError("compiler.bc_forall_require: 'when' clause 4 failed")
            if not flag_3:
              raise AssertionError("compiler.bc_forall_require: 'when' clause 3 failed")
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def bc_notany(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                "notany%d_worked" % context.lookup_data('start_lineno')):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                  "not notany%d_worked" % context.lookup_data('start_lineno')):
            context.end_save_all_undo()
            flag_3 = False
            with engine.prove(rule.rule_base.root_name, 'bc_premises1', context,
                              (rule.pattern(2),
                               rule.pattern(3),
                               rule.pattern(4),
                               rule.pattern(5),
                               rule.pattern(6),
                               rule.pattern(1),
                               rule.pattern(7),
                               rule.pattern(8),
                               rule.pattern(9),
                               rule.pattern(10),
                               rule.pattern(11),
                               rule.pattern(12),
                               rule.pattern(13),
                               rule.pattern(14),)) \
              as gen_3:
              for x_3 in gen_3:
                flag_3 = True
                assert x_3 is None, \
                  "compiler.bc_notany: got unexpected plan from when clause 3"
                mark4 = context.mark(True)
                if rule.pattern(15).match_data(context, context,
                        ("notany%d_worked = True" % context.lookup_data('start_lineno'),
                       context.lookup_data('fn_head1'),
                       "notany%d_worked = False" % context.lookup_data('start_lineno'),
                       context.lookup_data('fn_tail1'),
                       "if notany%d_worked:" % context.lookup_data('start_lineno'),
                       ("INDENT", 2))        ):
                  context.end_save_all_undo()
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
                else: context.end_save_all_undo()
                context.undo_to_mark(mark4)
            if not flag_3:
              raise AssertionError("compiler.bc_notany: 'when' clause 3 failed")
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def no_plan(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                ('assert x_%d is None, \\' % context.lookup_data('clause_num'),
               ('INDENT', 2),
               '"%(rb_name)s.%(rule_name)s: got unexpected plan from '
               'when clause %(clause_num)d"' %
               {'clause_num': context.lookup_data('clause_num'),
               'rb_name': context.lookup_data('rb_name'),
               'rule_name': context.lookup_data('rule_name')},
               'POPINDENT',)):
          context.end_save_all_undo()
          rule.rule_base.num_bc_rule_successes += 1
          yield
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def as_plan(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                \
                           helpers.merge_pattern("contexts.variable(%r)" % context.lookup_data('pat_var_name'),
               context.lookup_data('patterns_in'))):
          context.end_save_all_undo()
          flag_2 = False
          with engine.prove(rule.rule_base.root_name, 'plan_bindings', context,
                            (rule.pattern(1),
                             rule.pattern(2),
                             rule.pattern(3),
                             rule.pattern(4),
                             rule.pattern(5),
                             rule.pattern(6),
                             rule.pattern(7),)) \
            as gen_2:
            for x_2 in gen_2:
              flag_2 = True
              assert x_2 is None, \
                "compiler.as_plan: got unexpected plan from when clause 2"
              rule.rule_base.num_bc_rule_successes += 1
              yield
          if not flag_2:
            raise AssertionError("compiler.as_plan: 'when' clause 2 failed")
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def plan_spec(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                \
                           helpers.merge_pattern("contexts.variable(%r)" % context.lookup_data('plan_var_name'),
               context.lookup_data('patterns_in'))):
          context.end_save_all_undo()
          flag_2 = False
          with engine.prove(rule.rule_base.root_name, 'plan_bindings', context,
                            (rule.pattern(1),
                             rule.pattern(2),
                             rule.pattern(3),
                             rule.pattern(4),
                             rule.pattern(5),
                             rule.pattern(6),
                             rule.pattern(7),)) \
            as gen_2:
            for x_2 in gen_2:
              flag_2 = True
              assert x_2 is None, \
                "compiler.plan_spec: got unexpected plan from when clause 2"
              rule.rule_base.num_bc_rule_successes += 1
              yield
          if not flag_2:
            raise AssertionError("compiler.plan_spec: 'when' clause 2 failed")
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def illegal_plan_spec(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                helpers.syntax_error("illegal plan_spec in forall",
               context.lookup_data('lineno'), context.lookup_data('lexpos'))):
          context.end_save_all_undo()
          rule.rule_base.num_bc_rule_successes += 1
          yield
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def plan_bindings(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                ('assert x_%d is not None, \\' % context.lookup_data('clause_num'),
               ('INDENT', 2),
               '"%(rb_name)s.%(rule_name)s: expected plan from '
               'when clause %(clause_num)d"' %
               {'clause_num': context.lookup_data('clause_num'),
               'rb_name': context.lookup_data('rb_name'),
               'rule_name': context.lookup_data('rule_name')},
               'POPINDENT',
               "mark%d = context.mark(True)" % context.lookup_data('clause_num'),
               "if not rule.pattern(%d).match_data(context, context, "
               "x_%d):" % (context.lookup_data('pat_num'), context.lookup_data('clause_num')),
               ('INDENT', 2),
               'raise AssertionError("%(rb_name)s.%(rule_name)s: '
               'plan match to $%(plan_var_name)s failed in '
               'when clause %(clause_num)d")' %
               {'clause_num': context.lookup_data('clause_num'),
               'plan_var_name': context.lookup_data('plan_var_name'),
               'rb_name': context.lookup_data('rb_name'),
               'rule_name': context.lookup_data('rule_name')},
               'POPINDENT',
               "context.end_save_all_undo()")):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                  ("context.undo_to_mark(mark%d)" % context.lookup_data('clause_num'),)):
            context.end_save_all_undo()
            rule.rule_base.num_bc_rule_successes += 1
            yield
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def not_required(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        rule.rule_base.num_bc_rule_successes += 1
        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def required(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                ("flag_%d = False" % context.lookup_data('clause_num'),
               context.lookup_data('fn_head1'),
               "flag_%d = True" % context.lookup_data('clause_num'),
               )):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                  (context.lookup_data('fn_tail1'),
                 "if not flag_%d:" % context.lookup_data('clause_num'),
                 ("INDENT", 2),
                 "raise AssertionError(\"%s.%s: 'when' clause %d failed\")"
                 % (context.lookup_data('rb_name'), context.lookup_data('rule_name'), context.lookup_data('clause_num')),
                 "POPINDENT",
                 )):
            context.end_save_all_undo()
            rule.rule_base.num_bc_rule_successes += 1
            yield
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def bc_python_premise(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                context.lookup_data('clause_num') + 1):
          context.end_save_all_undo()
          with engine.prove(rule.rule_base.root_name, 'python_premise', context,
                            (rule.pattern(1),
                             rule.pattern(2),
                             rule.pattern(3),
                             rule.pattern(4),
                             rule.pattern(5),
                             rule.pattern(6),
                             rule.pattern(7),)) \
            as gen_2:
            for x_2 in gen_2:
              assert x_2 is None, \
                "compiler.bc_python_premise: got unexpected plan from when clause 2"
              rule.rule_base.num_bc_rule_successes += 1
              yield
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def python_eq(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                \
                           helpers.merge_pattern(context.lookup_data('pattern'), context.lookup_data('patterns_in'))):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                  context.lookup_data('python_code')[:-1] + (context.lookup_data('python_code')[-1] + '):',)):
            context.end_save_all_undo()
            mark3 = context.mark(True)
            if rule.pattern(2).match_data(context, context,
                    ("mark%d = context.mark(True)" % context.lookup_data('clause_num'),
                   "if rule.pattern(%d).match_data(context, context," %
                   context.lookup_data('pat_num'),
                   ('INDENT', 2),
                   ('INDENT', 5),
                   ('STARTING_LINENO', context.lookup_data('start_lineno')),
                   context.lookup_data('python_code2'),
                   ('ENDING_LINENO', context.lookup_data('end_lineno')),
                   "POPINDENT",
                   "context.end_save_all_undo()",
                   )):
              context.end_save_all_undo()
              mark4 = context.mark(True)
              if rule.pattern(3).match_data(context, context,
                      ('POPINDENT',
                     "else: context.end_save_all_undo()",
                     "context.undo_to_mark(mark%d)" % context.lookup_data('clause_num'),)):
                context.end_save_all_undo()
                rule.rule_base.num_bc_rule_successes += 1
                yield
              else: context.end_save_all_undo()
              context.undo_to_mark(mark4)
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def python_in(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                \
                           helpers.merge_pattern(context.lookup_data('pattern'), context.lookup_data('patterns_in'))):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                  context.lookup_data('python_code')[:-1] + (context.lookup_data('python_code')[-1] + ':',)):
            context.end_save_all_undo()
            mark3 = context.mark(True)
            if rule.pattern(2).match_data(context, context,
                    ("for python_ans in \\",
                   ('INDENT', 2),
                   ('INDENT', 2),
                   ('STARTING_LINENO', context.lookup_data('start_lineno')),
                   context.lookup_data('python_code2'),
                   ('ENDING_LINENO', context.lookup_data('end_lineno')),
                   'POPINDENT',
                   "mark%d = context.mark(True)" % context.lookup_data('clause_num'),
                   "if rule.pattern(%d).match_data(context, context, "
                   "python_ans):" % context.lookup_data('pat_num'),
                   ('INDENT', 2),
                   "context.end_save_all_undo()",
                   )):
              context.end_save_all_undo()
              mark4 = context.mark(True)
              if rule.pattern(3).match_data(context, context,
                      (    () if context.lookup_data('break_cond') is None
                     else ("if %s:" % context.lookup_data('break_cond'),
                     ('INDENT', 2),
                     "context.undo_to_mark(mark%d)" % context.lookup_data('clause_num'),
                     "break",
                     'POPINDENT',),
                     'POPINDENT',
                     "else: context.end_save_all_undo()",
                     "context.undo_to_mark(mark%d)" % context.lookup_data('clause_num'),
                     'POPINDENT',)):
                context.end_save_all_undo()
                rule.rule_base.num_bc_rule_successes += 1
                yield
              else: context.end_save_all_undo()
              context.undo_to_mark(mark4)
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def python_check(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                context.lookup_data('python_code')[:-1] + (context.lookup_data('python_code')[-1] + ':',)):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                  (('STARTING_LINENO', context.lookup_data('start_lineno')),
                 "if " + context.lookup_data('python_code2')[0].strip(),
                 ('INDENT', 3),
                 context.lookup_data('python_code2')[1:],
                 'POPINDENT',
                 ('ENDING_LINENO', context.lookup_data('end_lineno')),
                 ('INDENT', 2),
                 )):
            context.end_save_all_undo()
            rule.rule_base.num_bc_rule_successes += 1
            yield
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def python_block(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        rule.rule_base.num_bc_rule_successes += 1
        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('compiler')
  
  bc_rule.bc_rule('file', This_rule_base, 'compile',
                  file, None,
                  (contexts.variable('generated_root_pkg'),
                   contexts.variable('rb_name'),
                   pattern.pattern_tuple((pattern.pattern_literal('file'), contexts.variable('parent'), pattern.pattern_tuple((contexts.variable('fc_rules'), contexts.variable('fc_extra_lines'),), None), pattern.pattern_tuple((contexts.variable('bc_rules'), contexts.variable('bc_extra_lines'), contexts.variable('plan_extra_lines'),), None),), None),
                   contexts.variable('fc_lines'),
                   contexts.variable('bc_lines'),
                   contexts.variable('plan_lines'),),
                  (),
                  (contexts.variable('fc_head'),
                   contexts.variable('bc_head'),
                   contexts.variable('plan_head'),
                   contexts.variable('rb_name'),
                   contexts.variable('parent'),
                   contexts.variable('decl_line'),
                   contexts.variable('fc_rules'),
                   contexts.variable('fc_fun_lines'),
                   contexts.variable('fc_init_lines'),
                   contexts.variable('bc_rules'),
                   contexts.variable('bc_plan_lines'),
                   contexts.variable('bc_bc_fun_lines'),
                   contexts.variable('bc_bc_init_lines'),
                   contexts.variable('fc_lines'),
                   contexts.variable('plan_lines'),
                   contexts.variable('bc_lines'),))
  
  bc_rule.bc_rule('rule_decl', This_rule_base, 'rule_decl',
                  rule_decl, None,
                  (contexts.variable('rb_name'),
                   pattern.pattern_literal(None),
                   contexts.variable('decl_line'),),
                  (),
                  (contexts.variable('decl_line'),))
  
  bc_rule.bc_rule('rule_decl_with_parent', This_rule_base, 'rule_decl',
                  rule_decl_with_parent, None,
                  (contexts.variable('rb_name'),
                   pattern.pattern_tuple((pattern.pattern_literal('parent'), contexts.variable('parent'), contexts.variable('excluded_symbols'),), None),
                   contexts.variable('decl_line'),),
                  (),
                  (contexts.variable('decl_line'),))
  
  bc_rule.bc_rule('fc_rules', This_rule_base, 'fc_rules',
                  fc_rules, None,
                  (contexts.variable('fc_rules'),
                   contexts.variable('fc_funs'),
                   contexts.variable('fc_init'),),
                  (),
                  (contexts.variable('fc_rule'),
                   contexts.variable('fc_fun_1'),
                   contexts.variable('fc_init_1'),
                   contexts.variable('fc_funs'),
                   contexts.variable('fc_init'),))
  
  bc_rule.bc_rule('fc_rule_', This_rule_base, 'fc_rule',
                  fc_rule_, None,
                  (pattern.pattern_tuple((pattern.pattern_literal('fc_rule'), contexts.variable('rule_name'), contexts.variable('fc_premises'), contexts.variable('assertions'),), None),
                   contexts.variable('fc_fun'),
                   contexts.variable('fc_init'),),
                  (),
                  (contexts.variable('rule_name'),
                   pattern.pattern_literal(0),
                   contexts.anonymous('_'),
                   contexts.variable('fc_premises'),
                   pattern.pattern_literal(None),
                   pattern.pattern_literal(False),
                   contexts.variable('prem_fn_head'),
                   contexts.variable('prem_fn_tail'),
                   contexts.variable('prem_decl_lines'),
                   pattern.pattern_literal(()),
                   contexts.variable('patterns_out1'),
                   contexts.variable('assertions'),
                   contexts.variable('asserts_fn_lines'),
                   contexts.variable('patterns_out'),
                   contexts.variable('fc_fun'),
                   contexts.variable('fc_init'),))
  
  bc_rule.bc_rule('fc_premises0', This_rule_base, 'fc_premises',
                  fc_premises0, None,
                  (contexts.anonymous('_'),
                   contexts.variable('clause_num'),
                   contexts.variable('clause_num'),
                   pattern.pattern_literal(()),
                   contexts.anonymous('_'),
                   contexts.anonymous('_'),
                   pattern.pattern_literal(()),
                   pattern.pattern_literal(()),
                   contexts.variable('decl_num_in'),
                   contexts.variable('decl_num_in'),
                   pattern.pattern_literal(()),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_in'),),
                  (),
                  ())
  
  bc_rule.bc_rule('fc_premises1', This_rule_base, 'fc_premises',
                  fc_premises1, None,
                  (contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   contexts.variable('next_clause_num'),
                   pattern.pattern_tuple((contexts.variable('first_prem'),), contexts.variable('rest_prems')),
                   contexts.variable('break_cond'),
                   contexts.variable('multi_match'),
                   pattern.pattern_tuple((contexts.variable('fn_head1'),), contexts.variable('fn_head2')),
                   pattern.pattern_tuple((contexts.variable('fn_tail2'),), contexts.variable('fn_tail1')),
                   contexts.variable('decl_num_in'),
                   contexts.variable('decl_num_out'),
                   contexts.variable('decl_lines'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out'),),
                  (),
                  (contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   contexts.variable('next_clause_num1'),
                   contexts.variable('first_prem'),
                   contexts.variable('break_cond'),
                   contexts.variable('multi_match'),
                   contexts.variable('fn_head1'),
                   contexts.variable('fn_tail1'),
                   contexts.variable('decl_num_in'),
                   contexts.variable('decl_num_out1'),
                   contexts.variable('decl_lines1'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out1'),
                   contexts.variable('next_clause_num'),
                   contexts.variable('rest_prems'),
                   contexts.variable('fn_head2'),
                   contexts.variable('fn_tail2'),
                   contexts.variable('decl_num_out'),
                   contexts.variable('decl_lines2'),
                   contexts.variable('patterns_out'),
                   contexts.variable('decl_lines'),))
  
  bc_rule.bc_rule('fc_premise', This_rule_base, 'fc_premise',
                  fc_premise, None,
                  (contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   contexts.variable('next_clause_num'),
                   pattern.pattern_tuple((pattern.pattern_literal('fc_premise'), contexts.variable('kb_name'), contexts.variable('entity_name'), contexts.variable('arg_patterns'), contexts.variable('start_lineno'), contexts.variable('end_lineno'),), None),
                   contexts.variable('break_cond'),
                   contexts.variable('multi_match'),
                   contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),
                   contexts.variable('decl_num_in'),
                   contexts.variable('decl_num_out'),
                   contexts.variable('decl_lines'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_in'),),
                  (),
                  (contexts.variable('kb_name'),
                   contexts.variable('entity_name'),
                   contexts.variable('start_lineno'),
                   contexts.variable('end_lineno'),
                   contexts.variable('multi_match'),
                   contexts.variable('decl_num_in'),
                   contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),
                   contexts.variable('next_clause_num'),
                   contexts.variable('decl_num_out'),
                   contexts.variable('decl_lines'),))
  
  bc_rule.bc_rule('gen_fc_for_false', This_rule_base, 'gen_fc_for',
                  gen_fc_for_false, None,
                  (contexts.variable('kb_name'),
                   contexts.variable('entity_name'),
                   contexts.variable('start_lineno'),
                   contexts.variable('end_lineno'),
                   pattern.pattern_literal(False),
                   contexts.variable('decl_num'),
                   contexts.variable('fn_head'),),
                  (),
                  (contexts.variable('fn_head'),))
  
  bc_rule.bc_rule('gen_fc_for_true', This_rule_base, 'gen_fc_for',
                  gen_fc_for_true, None,
                  (contexts.variable('kb_name'),
                   contexts.variable('entity_name'),
                   contexts.variable('start_lineno'),
                   contexts.variable('end_lineno'),
                   pattern.pattern_literal(True),
                   contexts.variable('decl_num'),
                   contexts.variable('fn_head'),),
                  (),
                  (contexts.variable('fn_head'),))
  
  bc_rule.bc_rule('fc_first', This_rule_base, 'fc_premise',
                  fc_first, None,
                  (contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   contexts.variable('next_clause_num'),
                   pattern.pattern_tuple((pattern.pattern_literal('fc_first'), contexts.variable('premises1'), contexts.anonymous('_'),), None),
                   contexts.anonymous('_'),
                   contexts.anonymous('_'),
                   pattern.pattern_tuple((contexts.variable('init_worked'), contexts.variable('fn_head'), contexts.variable('set_worked'),), None),
                   contexts.variable('fn_tail'),
                   contexts.variable('decl_num_in'),
                   contexts.variable('decl_num_out'),
                   contexts.variable('decl_lines'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out'),),
                  (),
                  (contexts.variable('break_cond'),
                   contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   contexts.variable('next_clause_num'),
                   contexts.variable('premises1'),
                   pattern.pattern_literal(True),
                   contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),
                   contexts.variable('decl_num_in'),
                   contexts.variable('decl_num_out'),
                   contexts.variable('decl_lines'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out'),
                   contexts.variable('init_worked'),
                   contexts.variable('set_worked'),))
  
  bc_rule.bc_rule('fc_forall_None', This_rule_base, 'fc_premise',
                  fc_forall_None, None,
                  (contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   contexts.variable('next_clause_num'),
                   pattern.pattern_tuple((pattern.pattern_literal('fc_forall'), contexts.variable('premises1'), pattern.pattern_literal(None), contexts.anonymous('_'), contexts.anonymous('_'),), None),
                   contexts.anonymous('_'),
                   contexts.anonymous('_'),
                   contexts.variable('fn_head'),
                   pattern.pattern_literal(()),
                   contexts.variable('decl_num_in'),
                   contexts.variable('decl_num_out'),
                   contexts.variable('decl_lines'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out'),),
                  (),
                  (contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   contexts.variable('next_clause_num'),
                   contexts.variable('premises1'),
                   pattern.pattern_literal(None),
                   pattern.pattern_literal(True),
                   contexts.variable('fn_head1'),
                   contexts.variable('fn_tail1'),
                   contexts.variable('decl_num_in'),
                   contexts.variable('decl_num_out'),
                   contexts.variable('decl_lines'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out'),
                   contexts.variable('fn_head'),))
  
  bc_rule.bc_rule('fc_forall_require', This_rule_base, 'fc_premise',
                  fc_forall_require, None,
                  (contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   contexts.variable('next_clause_num'),
                   pattern.pattern_tuple((pattern.pattern_literal('fc_forall'), contexts.variable('premises1'), contexts.variable('require'), contexts.variable('start_lineno'), contexts.anonymous('_'),), None),
                   contexts.anonymous('_'),
                   contexts.anonymous('_'),
                   contexts.variable('fn_head'),
                   pattern.pattern_literal(("POPINDENT",)),
                   contexts.variable('decl_num_in'),
                   contexts.variable('decl_num_out'),
                   contexts.variable('decl_lines'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out'),),
                  (),
                  (contexts.variable('break_true'),
                   contexts.variable('break_false'),
                   contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   contexts.variable('next_clause_num1'),
                   contexts.variable('premises1'),
                   pattern.pattern_literal(True),
                   contexts.variable('fn_head1'),
                   contexts.variable('fn_tail1'),
                   contexts.variable('decl_num_in'),
                   contexts.variable('decl_num_out1'),
                   contexts.variable('decl_lines1'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out1'),
                   contexts.variable('next_clause_num'),
                   contexts.variable('require'),
                   contexts.variable('fn_head2'),
                   contexts.variable('fn_tail2'),
                   contexts.variable('decl_num_out'),
                   contexts.variable('decl_lines2'),
                   contexts.variable('patterns_out'),
                   contexts.variable('fn_head'),
                   contexts.variable('decl_lines'),))
  
  bc_rule.bc_rule('fc_notany', This_rule_base, 'fc_premise',
                  fc_notany, None,
                  (contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   contexts.variable('next_clause_num'),
                   pattern.pattern_tuple((pattern.pattern_literal('fc_notany'), contexts.variable('premises'), contexts.variable('start_lineno'),), None),
                   contexts.anonymous('_'),
                   contexts.anonymous('_'),
                   contexts.variable('fn_head'),
                   pattern.pattern_literal(("POPINDENT",)),
                   contexts.variable('decl_num_in'),
                   contexts.variable('decl_num_out'),
                   contexts.variable('decl_lines'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out'),),
                  (),
                  (contexts.variable('break_true'),
                   contexts.variable('break_false'),
                   contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   contexts.variable('next_clause_num'),
                   contexts.variable('premises'),
                   pattern.pattern_literal(True),
                   contexts.variable('fn_head1'),
                   contexts.variable('fn_tail1'),
                   contexts.variable('decl_num_in'),
                   contexts.variable('decl_num_out'),
                   contexts.variable('decl_lines'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out'),
                   contexts.variable('fn_head'),))
  
  bc_rule.bc_rule('fc_python_premise', This_rule_base, 'fc_premise',
                  fc_python_premise, None,
                  (contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   contexts.variable('next_clause_num'),
                   contexts.variable('python_premise'),
                   contexts.variable('break_cond'),
                   contexts.anonymous('_'),
                   contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),
                   contexts.variable('decl_num_in'),
                   contexts.variable('decl_num_in'),
                   pattern.pattern_literal(()),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out'),),
                  (),
                  (contexts.variable('next_clause_num'),
                   contexts.variable('clause_num'),
                   contexts.variable('python_premise'),
                   contexts.variable('break_cond'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out'),
                   contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),))
  
  bc_rule.bc_rule('assertions_0', This_rule_base, 'assertions',
                  assertions_0, None,
                  (pattern.pattern_literal(()),
                   pattern.pattern_literal(()),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_in'),),
                  (),
                  ())
  
  bc_rule.bc_rule('assertions_n', This_rule_base, 'assertions',
                  assertions_n, None,
                  (pattern.pattern_tuple((contexts.variable('first_assertion'),), contexts.variable('rest_assertions')),
                   pattern.pattern_tuple((contexts.variable('fn_lines1'),), contexts.variable('fn_lines2')),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out'),),
                  (),
                  (contexts.variable('first_assertion'),
                   contexts.variable('fn_lines1'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out1'),
                   contexts.variable('rest_assertions'),
                   contexts.variable('fn_lines2'),
                   contexts.variable('patterns_out'),))
  
  bc_rule.bc_rule('assertion', This_rule_base, 'assertion',
                  assertion, None,
                  (pattern.pattern_tuple((pattern.pattern_literal('assert'), contexts.variable('kb_name'), contexts.variable('entity_name'), contexts.variable('patterns'), contexts.variable('start_lineno'), contexts.variable('end_lineno'),), None),
                   contexts.variable('fn_lines'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out'),),
                  (),
                  (pattern.pattern_tuple((contexts.variable('pat_nums'), contexts.variable('patterns_out'),), None),
                   contexts.variable('fn_lines'),))
  
  bc_rule.bc_rule('python_assertion', This_rule_base, 'assertion',
                  python_assertion, None,
                  (pattern.pattern_tuple((pattern.pattern_literal('python_assertion'), pattern.pattern_tuple((contexts.variable('python_code'), contexts.anonymous('_'), contexts.anonymous('_'), contexts.anonymous('_'),), None), contexts.variable('start_lineno'), contexts.variable('end_lineno'),), None),
                   pattern.pattern_tuple((pattern.pattern_tuple((pattern.pattern_literal('STARTING_LINENO'), contexts.variable('start_lineno'),), None), contexts.variable('python_code'), pattern.pattern_tuple((pattern.pattern_literal('ENDING_LINENO'), contexts.variable('end_lineno'),), None),), None),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_in'),),
                  (),
                  ())
  
  bc_rule.bc_rule('bc_rules', This_rule_base, 'bc_rules',
                  bc_rules, None,
                  (contexts.variable('rb_name'),
                   contexts.variable('bc_rules'),
                   contexts.variable('bc_plan_lines'),
                   contexts.variable('bc_bc_funs'),
                   contexts.variable('bc_bc_init'),),
                  (),
                  (contexts.variable('bc_rule'),
                   contexts.variable('rb_name'),
                   contexts.variable('bc_plan1'),
                   contexts.variable('bc_bc_fun1'),
                   contexts.variable('bc_bc_init1'),
                   contexts.variable('bc_plan_lines'),
                   contexts.variable('bc_bc_funs'),
                   contexts.variable('bc_bc_init'),))
  
  bc_rule.bc_rule('bc_rule_', This_rule_base, 'bc_rule',
                  bc_rule_, None,
                  (contexts.variable('rb_name'),
                   pattern.pattern_tuple((pattern.pattern_literal('bc_rule'), contexts.variable('name'), contexts.variable('goal'), contexts.variable('bc_premises'), contexts.variable('python_lines'), contexts.variable('plan_vars_needed'),), None),
                   contexts.variable('plan_lines'),
                   contexts.variable('bc_fun_lines'),
                   contexts.variable('bc_init_lines'),),
                  (),
                  (contexts.variable('rb_name'),
                   contexts.variable('name'),
                   contexts.variable('bc_premises'),
                   contexts.variable('plan_vars_needed'),
                   contexts.variable('prem_plan_lines'),
                   contexts.variable('prem_fn_head'),
                   contexts.variable('prem_fn_tail'),
                   contexts.variable('prem_decl_lines'),
                   pattern.pattern_tuple((contexts.variable('plan_lines'), contexts.variable('goal_fn_head'), contexts.variable('goal_fn_tail'), contexts.variable('goal_decl_lines'),), None),
                   contexts.variable('bc_fun_lines'),
                   contexts.variable('bc_init_lines'),))
  
  bc_rule.bc_rule('bc_premises', This_rule_base, 'bc_premises',
                  bc_premises, None,
                  (contexts.variable('rb_name'),
                   contexts.variable('rule_name'),
                   contexts.variable('bc_premises'),
                   contexts.variable('plan_vars_needed'),
                   contexts.variable('plan_lines'),
                   contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),
                   contexts.variable('decl_lines'),),
                  (),
                  (contexts.variable('rb_name'),
                   contexts.variable('rule_name'),
                   pattern.pattern_literal(1),
                   contexts.anonymous('_'),
                   contexts.variable('bc_premises'),
                   pattern.pattern_literal(None),
                   pattern.pattern_literal(True),
                   pattern.pattern_literal(()),
                   contexts.variable('patterns'),
                   contexts.variable('plan_vars_needed'),
                   contexts.variable('plan_var_names'),
                   contexts.variable('plan_lines1'),
                   contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),
                   contexts.variable('pat_lines'),
                   contexts.variable('decl_lines'),
                   contexts.variable('plan_lines'),))
  
  bc_rule.bc_rule('bc_premises1_0', This_rule_base, 'bc_premises1',
                  bc_premises1_0, None,
                  (contexts.anonymous('_'),
                   contexts.anonymous('_'),
                   contexts.variable('clause_num'),
                   contexts.variable('clause_num'),
                   pattern.pattern_literal(()),
                   contexts.anonymous('_'),
                   contexts.anonymous('_'),
                   contexts.variable('patterns'),
                   contexts.variable('patterns'),
                   contexts.variable('plan_var_names'),
                   contexts.variable('plan_var_names'),
                   pattern.pattern_literal(()),
                   pattern.pattern_literal(()),
                   pattern.pattern_literal(()),),
                  (),
                  ())
  
  bc_rule.bc_rule('bc_premises1_n', This_rule_base, 'bc_premises1',
                  bc_premises1_n, None,
                  (contexts.variable('rb_name'),
                   contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   contexts.variable('next_clause_num'),
                   pattern.pattern_tuple((contexts.variable('first_prem'),), contexts.variable('rest_prems')),
                   contexts.variable('break_cond'),
                   contexts.variable('allow_plan'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out'),
                   contexts.variable('plan_var_names_in'),
                   contexts.variable('plan_var_names_out'),
                   contexts.variable('plan_lines'),
                   contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),),
                  (),
                  (contexts.variable('rb_name'),
                   contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   contexts.variable('next_clause_num1'),
                   contexts.variable('first_prem'),
                   contexts.variable('break_cond'),
                   contexts.variable('allow_plan'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out1'),
                   contexts.variable('plan_var_names_in'),
                   contexts.variable('plan_var_names_out1'),
                   contexts.variable('plan_lines1'),
                   contexts.variable('fn_head1'),
                   contexts.variable('fn_tail1'),
                   contexts.variable('next_clause_num'),
                   contexts.variable('rest_prems'),
                   contexts.variable('patterns_out'),
                   contexts.variable('plan_var_names_out'),
                   contexts.variable('plan_lines2'),
                   contexts.variable('fn_head2'),
                   contexts.variable('fn_tail2'),
                   contexts.variable('plan_lines'),
                   contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),))
  
  bc_rule.bc_rule('bc_premise', This_rule_base, 'bc_premise',
                  bc_premise, None,
                  (contexts.variable('rb_name'),
                   contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   contexts.variable('next_clause_num'),
                   pattern.pattern_tuple((pattern.pattern_literal('bc_premise'), contexts.variable('required'), contexts.variable('kb_name'), contexts.variable('entity_name'), contexts.variable('arg_patterns'), contexts.variable('plan_spec'), contexts.variable('start_lineno'), contexts.variable('end_lineno'),), None),
                   contexts.variable('break_cond'),
                   contexts.variable('allow_plan'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out'),
                   contexts.variable('plan_var_names_in'),
                   contexts.variable('plan_var_names_out'),
                   contexts.variable('plan_lines'),
                   contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),),
                  (),
                  (contexts.variable('next_clause_num'),
                   contexts.variable('kb_name2'),
                   pattern.pattern_tuple((contexts.variable('pat_nums'), contexts.variable('patterns_out1'),), None),
                   contexts.variable('fn_head1'),
                   contexts.variable('required'),
                   contexts.variable('rb_name'),
                   contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   pattern.pattern_literal(('POPINDENT', 'POPINDENT',)),
                   contexts.variable('fn_head2'),
                   contexts.variable('fn_tail2'),
                   contexts.variable('plan_spec'),
                   contexts.variable('allow_plan'),
                   contexts.variable('patterns_out1'),
                   contexts.variable('patterns_out'),
                   contexts.variable('fn_head3'),
                   contexts.variable('fn_tail3'),
                   contexts.variable('plan_lines'),
                   contexts.variable('plan_vars_needed'),
                   pattern.pattern_tuple((contexts.anonymous('_'), contexts.variable('plan_var_names_out'),), None),
                   contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),))
  
  bc_rule.bc_rule('bc_first', This_rule_base, 'bc_premise',
                  bc_first, None,
                  (contexts.variable('rb_name'),
                   contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   contexts.variable('next_clause_num'),
                   pattern.pattern_tuple((pattern.pattern_literal('bc_first'), contexts.variable('required'), contexts.variable('bc_premises'), contexts.anonymous('_'),), None),
                   contexts.anonymous('_'),
                   contexts.variable('allow_plan'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out'),
                   contexts.variable('plan_var_names_in'),
                   contexts.variable('plan_var_names_out'),
                   contexts.variable('plan_lines'),
                   pattern.pattern_tuple((contexts.variable('init_worked'), contexts.variable('fn_head'), contexts.variable('set_worked'),), None),
                   contexts.variable('fn_tail'),),
                  (),
                  (contexts.variable('break_cond'),
                   contexts.variable('rb_name'),
                   contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   contexts.variable('next_clause_num'),
                   contexts.variable('bc_premises'),
                   contexts.variable('allow_plan'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out'),
                   contexts.variable('plan_var_names_in'),
                   contexts.variable('plan_var_names_out'),
                   contexts.variable('plan_lines'),
                   contexts.variable('fn_head1'),
                   contexts.variable('fn_tail1'),
                   contexts.variable('required'),
                   contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),
                   contexts.variable('init_worked'),
                   contexts.variable('set_worked'),))
  
  bc_rule.bc_rule('bc_forall_None', This_rule_base, 'bc_premise',
                  bc_forall_None, None,
                  (contexts.variable('rb_name'),
                   contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   contexts.variable('next_clause_num'),
                   pattern.pattern_tuple((pattern.pattern_literal('bc_forall'), contexts.variable('bc_premises'), pattern.pattern_literal(None), contexts.anonymous('_'), contexts.anonymous('_'),), None),
                   contexts.anonymous('_'),
                   contexts.anonymous('_'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out'),
                   contexts.variable('plan_var_names_in'),
                   contexts.variable('plan_var_names_out'),
                   contexts.variable('plan_lines'),
                   contexts.variable('fn_head'),
                   pattern.pattern_literal(()),),
                  (),
                  (contexts.variable('rb_name'),
                   contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   contexts.variable('next_clause_num'),
                   contexts.variable('bc_premises'),
                   pattern.pattern_literal(None),
                   pattern.pattern_literal(False),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out'),
                   contexts.variable('plan_var_names_in'),
                   contexts.variable('plan_var_names_out'),
                   contexts.variable('plan_lines'),
                   contexts.variable('fn_head1'),
                   contexts.variable('fn_tail'),
                   contexts.variable('fn_head'),))
  
  bc_rule.bc_rule('bc_forall_require', This_rule_base, 'bc_premise',
                  bc_forall_require, None,
                  (contexts.variable('rb_name'),
                   contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   contexts.variable('next_clause_num'),
                   pattern.pattern_tuple((pattern.pattern_literal('bc_forall'), contexts.variable('premises1'), contexts.variable('require'), contexts.variable('start_lineno'), contexts.anonymous('_'),), None),
                   contexts.anonymous('_'),
                   contexts.anonymous('_'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out'),
                   contexts.variable('plan_var_names_in'),
                   contexts.variable('plan_var_names_out'),
                   pattern.pattern_literal(()),
                   contexts.variable('fn_head'),
                   pattern.pattern_literal(("POPINDENT",)),),
                  (),
                  (contexts.variable('break_true'),
                   contexts.variable('break_false'),
                   contexts.variable('rb_name'),
                   contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   contexts.variable('next_clause_num1'),
                   contexts.variable('premises1'),
                   pattern.pattern_literal(False),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out1'),
                   contexts.variable('plan_var_names_in'),
                   contexts.variable('plan_var_names_out1'),
                   pattern.pattern_literal(()),
                   contexts.variable('fn_head1'),
                   contexts.variable('fn_tail1'),
                   contexts.variable('next_clause_num'),
                   contexts.variable('require'),
                   contexts.variable('patterns_out'),
                   contexts.variable('plan_var_names_out'),
                   contexts.variable('fn_head2'),
                   contexts.variable('fn_tail2'),
                   contexts.variable('fn_head'),))
  
  bc_rule.bc_rule('bc_notany', This_rule_base, 'bc_premise',
                  bc_notany, None,
                  (contexts.variable('rb_name'),
                   contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   contexts.variable('next_clause_num'),
                   pattern.pattern_tuple((pattern.pattern_literal('bc_notany'), contexts.variable('bc_premises'), contexts.variable('start_lineno'),), None),
                   contexts.anonymous('_'),
                   contexts.anonymous('_'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out'),
                   contexts.variable('plan_var_in'),
                   contexts.variable('plan_var_out'),
                   pattern.pattern_literal(()),
                   contexts.variable('fn_head'),
                   pattern.pattern_literal(("POPINDENT",)),),
                  (),
                  (contexts.variable('break_true'),
                   contexts.variable('break_false'),
                   contexts.variable('rb_name'),
                   contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   contexts.variable('next_clause_num'),
                   contexts.variable('bc_premises'),
                   pattern.pattern_literal(False),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out'),
                   contexts.variable('plan_var_in'),
                   contexts.variable('plan_var_out'),
                   pattern.pattern_literal(()),
                   contexts.variable('fn_head1'),
                   contexts.variable('fn_tail1'),
                   contexts.variable('fn_head'),))
  
  bc_rule.bc_rule('no_plan', This_rule_base, 'gen_plan_lines',
                  no_plan, None,
                  (contexts.variable('rb_name'),
                   contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   pattern.pattern_literal(None),
                   contexts.anonymous('_'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_in'),
                   contexts.variable('fn_head'),
                   pattern.pattern_literal(()),
                   pattern.pattern_literal(()),
                   pattern.pattern_literal(()),),
                  (),
                  (contexts.variable('fn_head'),))
  
  bc_rule.bc_rule('as_plan', This_rule_base, 'gen_plan_lines',
                  as_plan, None,
                  (contexts.variable('rb_name'),
                   contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   pattern.pattern_tuple((pattern.pattern_literal('as'), contexts.variable('pat_var_name'),), None),
                   contexts.anonymous('_'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out'),
                   contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),
                   pattern.pattern_literal(()),
                   pattern.pattern_literal(()),),
                  (),
                  (pattern.pattern_tuple((contexts.variable('pat_num'), contexts.variable('patterns_out'),), None),
                   contexts.variable('rb_name'),
                   contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   contexts.variable('pat_var_name'),
                   contexts.variable('pat_num'),
                   contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),))
  
  bc_rule.bc_rule('plan_spec', This_rule_base, 'gen_plan_lines',
                  plan_spec, None,
                  (contexts.variable('rb_name'),
                   contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   pattern.pattern_tuple((pattern.pattern_literal('plan_spec'), contexts.variable('step_num'), contexts.variable('plan_var_name'), contexts.variable('python_code'), contexts.variable('plan_vars_needed'), contexts.anonymous('_'), contexts.anonymous('_'),), None),
                   pattern.pattern_literal(True),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out'),
                   contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),
                   pattern.pattern_tuple((pattern.pattern_tuple((contexts.variable('step_num'), contexts.variable('python_code'),), None),), None),
                   contexts.variable('plan_vars_needed'),),
                  (),
                  (pattern.pattern_tuple((contexts.variable('pat_num'), contexts.variable('patterns_out'),), None),
                   contexts.variable('rb_name'),
                   contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   contexts.variable('plan_var_name'),
                   contexts.variable('pat_num'),
                   contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),))
  
  bc_rule.bc_rule('illegal_plan_spec', This_rule_base, 'gen_plan_lines',
                  illegal_plan_spec, None,
                  (contexts.anonymous('_'),
                   contexts.anonymous('_'),
                   contexts.anonymous('_'),
                   pattern.pattern_tuple((pattern.pattern_literal('plan_spec'), contexts.anonymous('_'), contexts.anonymous('_'), contexts.anonymous('_'), contexts.anonymous('_'), contexts.variable('lineno'), contexts.variable('lexpos'),), None),
                   pattern.pattern_literal(False),
                   contexts.anonymous('_'),
                   contexts.anonymous('_'),
                   contexts.anonymous('_'),
                   contexts.anonymous('_'),
                   contexts.anonymous('_'),
                   contexts.anonymous('_'),),
                  (),
                  (contexts.anonymous('_'),))
  
  bc_rule.bc_rule('plan_bindings', This_rule_base, 'plan_bindings',
                  plan_bindings, None,
                  (contexts.variable('rb_name'),
                   contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   contexts.variable('plan_var_name'),
                   contexts.variable('pat_num'),
                   contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),),
                  (),
                  (contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),))
  
  bc_rule.bc_rule('not_required', This_rule_base, 'add_required',
                  not_required, None,
                  (pattern.pattern_literal(False),
                   contexts.anonymous('_'),
                   contexts.anonymous('_'),
                   contexts.anonymous('_'),
                   contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),
                   contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),),
                  (),
                  ())
  
  bc_rule.bc_rule('required', This_rule_base, 'add_required',
                  required, None,
                  (pattern.pattern_literal(True),
                   contexts.variable('rb_name'),
                   contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   contexts.variable('fn_head1'),
                   contexts.variable('fn_tail1'),
                   contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),),
                  (),
                  (contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),))
  
  bc_rule.bc_rule('bc_python_premise', This_rule_base, 'bc_premise',
                  bc_python_premise, None,
                  (contexts.variable('rb_name'),
                   contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   contexts.variable('next_clause_num'),
                   contexts.variable('python_premise'),
                   contexts.variable('break_cond'),
                   contexts.anonymous('_'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out'),
                   contexts.variable('plan_var_names'),
                   contexts.variable('plan_var_names'),
                   pattern.pattern_literal(()),
                   contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),),
                  (),
                  (contexts.variable('next_clause_num'),
                   contexts.variable('clause_num'),
                   contexts.variable('python_premise'),
                   contexts.variable('break_cond'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out'),
                   contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),))
  
  bc_rule.bc_rule('python_eq', This_rule_base, 'python_premise',
                  python_eq, None,
                  (contexts.variable('clause_num'),
                   pattern.pattern_tuple((pattern.pattern_literal('python_eq'), contexts.variable('pattern'), pattern.pattern_tuple((contexts.variable('python_code'), contexts.anonymous('_'), contexts.anonymous('_'), contexts.anonymous('_'),), None), contexts.variable('start_lineno'), contexts.variable('end_lineno'),), None),
                   contexts.anonymous('_'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out'),
                   contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),),
                  (),
                  (pattern.pattern_tuple((contexts.variable('pat_num'), contexts.variable('patterns_out'),), None),
                   contexts.variable('python_code2'),
                   contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),))
  
  bc_rule.bc_rule('python_in', This_rule_base, 'python_premise',
                  python_in, None,
                  (contexts.variable('clause_num'),
                   pattern.pattern_tuple((pattern.pattern_literal('python_in'), contexts.variable('pattern'), pattern.pattern_tuple((contexts.variable('python_code'), contexts.anonymous('_'), contexts.anonymous('_'), contexts.anonymous('_'),), None), contexts.variable('start_lineno'), contexts.variable('end_lineno'),), None),
                   contexts.variable('break_cond'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out'),
                   contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),),
                  (),
                  (pattern.pattern_tuple((contexts.variable('pat_num'), contexts.variable('patterns_out'),), None),
                   contexts.variable('python_code2'),
                   contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),))
  
  bc_rule.bc_rule('python_check', This_rule_base, 'python_premise',
                  python_check, None,
                  (contexts.variable('clause_num'),
                   pattern.pattern_tuple((pattern.pattern_literal('python_check'), pattern.pattern_tuple((contexts.variable('python_code'), contexts.anonymous('_'), contexts.anonymous('_'), contexts.anonymous('_'),), None), contexts.variable('start_lineno'), contexts.variable('end_lineno'),), None),
                   contexts.anonymous('_'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_in'),
                   contexts.variable('fn_head'),
                   pattern.pattern_literal(('POPINDENT',)),),
                  (),
                  (contexts.variable('python_code2'),
                   contexts.variable('fn_head'),))
  
  bc_rule.bc_rule('python_block', This_rule_base, 'python_premise',
                  python_block, None,
                  (contexts.variable('clause_num'),
                   pattern.pattern_tuple((pattern.pattern_literal('python_block'), pattern.pattern_tuple((contexts.variable('python_code'), contexts.anonymous('_'), contexts.anonymous('_'), contexts.anonymous('_'),), None), contexts.variable('start_lineno'), contexts.variable('end_lineno'),), None),
                   contexts.anonymous('_'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_in'),
                   pattern.pattern_tuple((pattern.pattern_tuple((pattern.pattern_literal('STARTING_LINENO'), contexts.variable('start_lineno'),), None), contexts.variable('python_code'), pattern.pattern_tuple((pattern.pattern_literal('ENDING_LINENO'), contexts.variable('end_lineno'),), None),), None),
                   pattern.pattern_literal(()),),
                  (),
                  ())

from pyke.krb_compiler import helpers

Krb_filename = '../compiler.krb'
Krb_lineno_map = (
    ((16, 20), (24, 28)),
    ((24, 24), (30, 30)),
    ((28, 28), (31, 31)),
    ((32, 32), (32, 32)),
    ((35, 43), (33, 33)),
    ((45, 53), (34, 34)),
    ((55, 65), (35, 36)),
    ((68, 80), (37, 49)),
    ((84, 89), (50, 55)),
    ((93, 108), (56, 71)),
    ((140, 144), (74, 74)),
    ((148, 148), (76, 76)),
    ((164, 168), (79, 79)),
    ((172, 174), (81, 83)),
    ((190, 194), (86, 86)),
    ((196, 197), (88, 90)),
    ((200, 200), (92, 92)),
    ((206, 214), (94, 94)),
    ((215, 216), (95, 97)),
    ((229, 229), (98, 98)),
    ((233, 233), (99, 99)),
    ((251, 255), (102, 103)),
    ((258, 276), (105, 107)),
    ((278, 287), (108, 109)),
    ((290, 307), (110, 127)),
    ((311, 318), (128, 135)),
    ((340, 344), (138, 139)),
    ((358, 362), (142, 146)),
    ((365, 383), (148, 152)),
    ((385, 403), (153, 157)),
    ((406, 406), (158, 158)),
    ((426, 430), (161, 167)),
    ((432, 443), (169, 170)),
    ((446, 449), (171, 174)),
    ((453, 453), (175, 175)),
    ((457, 457), (176, 176)),
    ((461, 466), (177, 182)),
    ((488, 492), (185, 186)),
    ((496, 511), (188, 203)),
    ((527, 531), (207, 208)),
    ((535, 545), (210, 220)),
    ((561, 565), (223, 227)),
    ((569, 569), (229, 229)),
    ((572, 590), (230, 234)),
    ((593, 593), (235, 235)),
    ((597, 597), (236, 236)),
    ((619, 623), (239, 242)),
    ((626, 644), (244, 248)),
    ((647, 647), (249, 249)),
    ((665, 669), (252, 256)),
    ((673, 673), (258, 258)),
    ((677, 677), (259, 259)),
    ((680, 698), (260, 264)),
    ((700, 718), (265, 269)),
    ((721, 729), (270, 278)),
    ((733, 733), (279, 279)),
    ((759, 763), (282, 286)),
    ((767, 767), (288, 288)),
    ((771, 771), (289, 289)),
    ((774, 792), (290, 294)),
    ((795, 800), (295, 300)),
    ((822, 826), (303, 306)),
    ((830, 830), (308, 308)),
    ((832, 843), (309, 311)),
    ((858, 862), (314, 314)),
    ((876, 880), (317, 318)),
    ((883, 892), (320, 320)),
    ((894, 903), (321, 321)),
    ((920, 924), (324, 326)),
    ((928, 929), (328, 329)),
    ((933, 942), (330, 339)),
    ((960, 964), (342, 347)),
    ((978, 982), (350, 350)),
    ((984, 986), (352, 355)),
    ((989, 989), (357, 357)),
    ((995, 1005), (359, 359)),
    ((1006, 1008), (360, 363)),
    ((1021, 1021), (364, 364)),
    ((1025, 1025), (365, 365)),
    ((1029, 1029), (366, 366)),
    ((1049, 1053), (369, 371)),
    ((1056, 1069), (373, 375)),
    ((1072, 1074), (376, 378)),
    ((1078, 1085), (379, 386)),
    ((1089, 1092), (387, 390)),
    ((1114, 1118), (393, 395)),
    ((1121, 1140), (397, 400)),
    ((1143, 1143), (401, 401)),
    ((1147, 1150), (402, 405)),
    ((1154, 1159), (406, 411)),
    ((1181, 1185), (414, 416)),
    ((1199, 1203), (419, 423)),
    ((1206, 1225), (425, 429)),
    ((1227, 1246), (430, 434)),
    ((1249, 1249), (435, 435)),
    ((1253, 1253), (436, 436)),
    ((1257, 1257), (437, 437)),
    ((1281, 1285), (440, 446)),
    ((1289, 1289), (448, 448)),
    ((1293, 1293), (449, 449)),
    ((1297, 1298), (450, 451)),
    ((1302, 1314), (452, 464)),
    ((1317, 1330), (465, 466)),
    ((1332, 1348), (467, 470)),
    ((1351, 1352), (471, 472)),
    ((1356, 1356), (473, 473)),
    ((1360, 1363), (474, 477)),
    ((1395, 1399), (480, 484)),
    ((1403, 1403), (486, 486)),
    ((1406, 1425), (487, 491)),
    ((1427, 1440), (492, 493)),
    ((1443, 1443), (494, 494)),
    ((1447, 1447), (495, 495)),
    ((1471, 1475), (498, 502)),
    ((1478, 1497), (504, 508)),
    ((1500, 1500), (509, 509)),
    ((1518, 1522), (512, 516)),
    ((1526, 1526), (518, 518)),
    ((1530, 1530), (519, 519)),
    ((1533, 1552), (520, 524)),
    ((1554, 1573), (525, 529)),
    ((1576, 1584), (530, 538)),
    ((1608, 1612), (541, 545)),
    ((1616, 1616), (548, 548)),
    ((1620, 1620), (549, 549)),
    ((1623, 1642), (550, 554)),
    ((1645, 1650), (555, 560)),
    ((1672, 1676), (563, 565)),
    ((1680, 1687), (567, 574)),
    ((1703, 1707), (577, 581)),
    ((1711, 1713), (583, 585)),
    ((1716, 1728), (586, 587)),
    ((1745, 1749), (590, 595)),
    ((1753, 1755), (597, 599)),
    ((1758, 1770), (600, 601)),
    ((1787, 1791), (604, 606)),
    ((1795, 1796), (608, 609)),
    ((1812, 1816), (612, 613)),
    ((1820, 1840), (615, 635)),
    ((1844, 1844), (636, 636)),
    ((1862, 1866), (639, 640)),
    ((1880, 1884), (643, 644)),
    ((1888, 1891), (646, 649)),
    ((1895, 1901), (650, 656)),
    ((1919, 1923), (659, 663)),
    ((1927, 1927), (665, 665)),
    ((1929, 1940), (666, 668)),
    ((1955, 1959), (671, 675)),
    ((1963, 1964), (677, 678)),
    ((1968, 1968), (679, 679)),
    ((1972, 1982), (680, 690)),
    ((1986, 1988), (691, 693)),
    ((2010, 2014), (696, 700)),
    ((2018, 2019), (702, 703)),
    ((2023, 2023), (704, 704)),
    ((2027, 2039), (705, 717)),
    ((2043, 2052), (718, 727)),
    ((2074, 2078), (730, 735)),
    ((2082, 2082), (737, 737)),
    ((2086, 2093), (738, 745)),
    ((2111, 2115), (748, 756)),
)
