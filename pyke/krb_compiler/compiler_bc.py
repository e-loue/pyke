# compiler_bc.py

from __future__ import with_statement
import itertools
from pyke import contexts, pattern, bc_rule

version = '0.7'

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

def fc_rules0(rule, arg_patterns, arg_context):
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

def fc_rules1(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'fc_rule', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),)) \
          as gen_1:
          for x_1 in gen_1:
            flag_1 = True
            assert x_1 is None, \
              "compiler.fc_rules1: got unexpected plan from when clause 1"
            flag_2 = False
            with engine.prove(rule.rule_base.root_name, 'fc_rules', context,
                              (rule.pattern(3),
                               rule.pattern(4),
                               rule.pattern(5),)) \
              as gen_2:
              for x_2 in gen_2:
                flag_2 = True
                assert x_2 is None, \
                  "compiler.fc_rules1: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
            if not flag_2:
              raise AssertionError("compiler.fc_rules1: 'when' clause 2 failed")
        if not flag_1:
          raise AssertionError("compiler.fc_rules1: 'when' clause 1 failed")
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
                           rule.pattern(10),)) \
          as gen_1:
          for x_1 in gen_1:
            flag_1 = True
            assert x_1 is None, \
              "compiler.fc_premises1: got unexpected plan from when clause 1"
            flag_2 = False
            with engine.prove(rule.rule_base.root_name, 'fc_premises', context,
                              (rule.pattern(0),
                               rule.pattern(2),
                               rule.pattern(11),
                               rule.pattern(12),
                               rule.pattern(4),
                               rule.pattern(5),
                               rule.pattern(13),
                               rule.pattern(14),
                               rule.pattern(15),
                               rule.pattern(10),
                               rule.pattern(16),)) \
              as gen_2:
              for x_2 in gen_2:
                flag_2 = True
                assert x_2 is None, \
                  "compiler.fc_premises1: got unexpected plan from when clause 2"
                mark3 = context.mark(True)
                if rule.pattern(17).match_data(context, context,
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
                                       context.lookup_data('clause_num'),
               ('INDENT', 9),
               "else engine.lookup(%r, %r, context," % \
                                         (context.lookup_data('kb_name'), context.lookup_data('entity_name')),
               ('INDENT', 19),
               "rule.foreach_patterns(%d)) \\" % context.lookup_data('clause_num'),
               'POPINDENT',
               'POPINDENT',
               ('INDENT', 2),
               "as gen_%d:" % context.lookup_data('clause_num'),
               "for dummy in gen_%d:" % context.lookup_data('clause_num'),
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
               "rule.foreach_patterns(%d)) \\" % context.lookup_data('clause_num'),
               'POPINDENT',
               ('INDENT', 2),
               "as gen_%d:" % context.lookup_data('clause_num'),
               "for dummy in gen_%d:" % context.lookup_data('clause_num'),
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
                             rule.pattern(10),)) \
            as gen_2:
            for x_2 in gen_2:
              flag_2 = True
              assert x_2 is None, \
                "compiler.fc_first: got unexpected plan from when clause 2"
              mark3 = context.mark(True)
              if rule.pattern(11).match_data(context, context,
                      "%s = False" % context.lookup_data('break_cond')):
                context.end_save_all_undo()
                mark4 = context.mark(True)
                if rule.pattern(12).match_data(context, context,
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
                           rule.pattern(10),)) \
          as gen_1:
          for x_1 in gen_1:
            flag_1 = True
            assert x_1 is None, \
              "compiler.fc_forall_None: got unexpected plan from when clause 1"
            mark2 = context.mark(True)
            if rule.pattern(11).match_data(context, context,
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
                               rule.pattern(11),)) \
              as gen_3:
              for x_3 in gen_3:
                flag_3 = True
                assert x_3 is None, \
                  "compiler.fc_forall_require: got unexpected plan from when clause 3"
                flag_4 = False
                with engine.prove(rule.rule_base.root_name, 'fc_premises', context,
                                  (rule.pattern(2),
                                   rule.pattern(4),
                                   rule.pattern(12),
                                   rule.pattern(13),
                                   rule.pattern(0),
                                   rule.pattern(6),
                                   rule.pattern(14),
                                   rule.pattern(15),
                                   rule.pattern(16),
                                   rule.pattern(11),
                                   rule.pattern(17),)) \
                  as gen_4:
                  for x_4 in gen_4:
                    flag_4 = True
                    assert x_4 is None, \
                      "compiler.fc_forall_require: got unexpected plan from when clause 4"
                    mark5 = context.mark(True)
                    if rule.pattern(18).match_data(context, context,
                            ("forall%d_worked = True" % context.lookup_data('start_lineno'),
                           context.lookup_data('fn_head1'),
                           "forall%d_worked = False" % context.lookup_data('start_lineno'),
                           context.lookup_data('fn_head2'),
                           ('INDENT', 2),
                           "forall%d_worked = True" % context.lookup_data('start_lineno'),
                           'POPINDENT',
                           context.lookup_data('fn_tail2'),
                           context.lookup_data('fn_tail1'),
                           "if forall%d_worked:" % context.lookup_data('start_lineno'),
                           ("INDENT", 2))):
                      context.end_save_all_undo()
                      mark6 = context.mark(True)
                      if rule.pattern(19).match_data(context, context,
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
                               rule.pattern(11),)) \
              as gen_3:
              for x_3 in gen_3:
                flag_3 = True
                assert x_3 is None, \
                  "compiler.fc_notany: got unexpected plan from when clause 3"
                mark4 = context.mark(True)
                if rule.pattern(12).match_data(context, context,
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
        with engine.prove(rule.rule_base.root_name, 'python_premise', context,
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
              "compiler.fc_python_premise: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
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

def bc_rules0(rule, arg_patterns, arg_context):
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

def bc_rules1(rule, arg_patterns, arg_context):
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
        with engine.prove(rule.rule_base.root_name, 'bc_rule', context,
                          (rule.pattern(0),
                           rule.pattern(1),
                           rule.pattern(2),
                           rule.pattern(3),
                           rule.pattern(4),)) \
          as gen_1:
          for x_1 in gen_1:
            flag_1 = True
            assert x_1 is None, \
              "compiler.bc_rules1: got unexpected plan from when clause 1"
            flag_2 = False
            with engine.prove(rule.rule_base.root_name, 'bc_rules', context,
                              (rule.pattern(0),
                               rule.pattern(5),
                               rule.pattern(6),
                               rule.pattern(7),
                               rule.pattern(8),)) \
              as gen_2:
              for x_2 in gen_2:
                flag_2 = True
                assert x_2 is None, \
                  "compiler.bc_rules1: got unexpected plan from when clause 2"
                mark3 = context.mark(True)
                if rule.pattern(9).match_data(context, context,
                        context.lookup_data('bc_plan1') + context.lookup_data('plan_rest')):
                  context.end_save_all_undo()
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
                else: context.end_save_all_undo()
                context.undo_to_mark(mark3)
            if not flag_2:
              raise AssertionError("compiler.bc_rules1: 'when' clause 2 failed")
        if not flag_1:
          raise AssertionError("compiler.bc_rules1: 'when' clause 1 failed")
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
                       key=lambda (step, lines): step)))))):
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
  
  bc_rule.bc_rule('fc_rules0', This_rule_base, 'fc_rules',
                  fc_rules0, None,
                  (pattern.pattern_literal(()),
                   pattern.pattern_literal(()),
                   pattern.pattern_literal(()),),
                  (),
                  ())
  
  bc_rule.bc_rule('fc_rules1', This_rule_base, 'fc_rules',
                  fc_rules1, None,
                  (pattern.pattern_tuple((contexts.variable('fc_rule'),), contexts.variable('fc_rest')),
                   pattern.pattern_tuple((contexts.variable('fc_fun_1'), contexts.variable('fc_funs_rest'),), None),
                   pattern.pattern_tuple((contexts.variable('fc_init_1'), contexts.variable('fc_init_rest'),), None),),
                  (),
                  (contexts.variable('fc_rule'),
                   contexts.variable('fc_fun_1'),
                   contexts.variable('fc_init_1'),
                   contexts.variable('fc_rest'),
                   contexts.variable('fc_funs_rest'),
                   contexts.variable('fc_init_rest'),))
  
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
                   contexts.variable('decl_lines1'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out1'),
                   contexts.variable('next_clause_num'),
                   contexts.variable('rest_prems'),
                   contexts.variable('fn_head2'),
                   contexts.variable('fn_tail2'),
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
                   contexts.variable('decl_lines'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_in'),),
                  (),
                  (contexts.variable('kb_name'),
                   contexts.variable('entity_name'),
                   contexts.variable('start_lineno'),
                   contexts.variable('end_lineno'),
                   contexts.variable('multi_match'),
                   contexts.variable('clause_num'),
                   contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),
                   contexts.variable('next_clause_num'),
                   contexts.variable('decl_lines'),))
  
  bc_rule.bc_rule('gen_fc_for_false', This_rule_base, 'gen_fc_for',
                  gen_fc_for_false, None,
                  (contexts.variable('kb_name'),
                   contexts.variable('entity_name'),
                   contexts.variable('start_lineno'),
                   contexts.variable('end_lineno'),
                   pattern.pattern_literal(False),
                   contexts.variable('clause_num'),
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
                   contexts.variable('clause_num'),
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
                   contexts.variable('decl_lines1'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out1'),
                   contexts.variable('next_clause_num'),
                   contexts.variable('require'),
                   contexts.variable('fn_head2'),
                   contexts.variable('fn_tail2'),
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
                   contexts.variable('decl_lines'),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out'),
                   contexts.variable('fn_head'),))
  
  bc_rule.bc_rule('fc_python_premise', This_rule_base, 'fc_premise',
                  fc_python_premise, None,
                  (contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   contexts.variable('clause_num'),
                   contexts.variable('python_premise'),
                   contexts.variable('break_cond'),
                   contexts.anonymous('_'),
                   contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),
                   pattern.pattern_literal(()),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_out'),),
                  (),
                  (contexts.variable('clause_num'),
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
  
  bc_rule.bc_rule('bc_rules0', This_rule_base, 'bc_rules',
                  bc_rules0, None,
                  (contexts.anonymous('_'),
                   pattern.pattern_literal(()),
                   pattern.pattern_literal(()),
                   pattern.pattern_literal(()),
                   pattern.pattern_literal(()),),
                  (),
                  ())
  
  bc_rule.bc_rule('bc_rules1', This_rule_base, 'bc_rules',
                  bc_rules1, None,
                  (contexts.variable('rb_name'),
                   pattern.pattern_tuple((contexts.variable('bc_rule'),), contexts.variable('bc_rest')),
                   contexts.variable('bc_plan_lines'),
                   pattern.pattern_tuple((contexts.variable('bc_bc_fun1'),), contexts.variable('bc_bc_funs_rest')),
                   pattern.pattern_tuple((contexts.variable('bc_bc_init1'),), contexts.variable('bc_bc_init_rest')),),
                  (),
                  (contexts.variable('rb_name'),
                   contexts.variable('bc_rule'),
                   contexts.variable('bc_plan1'),
                   contexts.variable('bc_bc_fun1'),
                   contexts.variable('bc_bc_init1'),
                   contexts.variable('bc_rest'),
                   contexts.variable('plan_rest'),
                   contexts.variable('bc_bc_funs_rest'),
                   contexts.variable('bc_bc_init_rest'),
                   contexts.variable('bc_plan_lines'),))
  
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
    ((15, 19), (24, 28)),
    ((23, 23), (30, 30)),
    ((27, 27), (31, 31)),
    ((31, 31), (32, 32)),
    ((34, 42), (33, 33)),
    ((44, 52), (34, 34)),
    ((54, 64), (35, 36)),
    ((67, 79), (37, 49)),
    ((83, 88), (50, 55)),
    ((92, 107), (56, 71)),
    ((139, 143), (74, 74)),
    ((147, 147), (76, 76)),
    ((163, 167), (79, 79)),
    ((171, 173), (81, 83)),
    ((189, 193), (86, 86)),
    ((207, 211), (89, 91)),
    ((214, 222), (93, 93)),
    ((224, 232), (94, 94)),
    ((249, 253), (97, 98)),
    ((256, 272), (100, 102)),
    ((274, 283), (103, 104)),
    ((286, 303), (105, 122)),
    ((307, 314), (123, 130)),
    ((336, 340), (133, 134)),
    ((354, 358), (137, 140)),
    ((361, 377), (142, 145)),
    ((379, 395), (146, 149)),
    ((398, 398), (150, 150)),
    ((418, 422), (153, 158)),
    ((424, 435), (160, 161)),
    ((438, 441), (162, 165)),
    ((445, 445), (166, 166)),
    ((449, 454), (167, 172)),
    ((474, 478), (175, 176)),
    ((482, 497), (178, 193)),
    ((513, 517), (197, 198)),
    ((521, 531), (200, 210)),
    ((547, 551), (213, 216)),
    ((555, 555), (218, 218)),
    ((558, 574), (219, 222)),
    ((577, 577), (223, 223)),
    ((581, 581), (224, 224)),
    ((603, 607), (227, 230)),
    ((610, 626), (232, 235)),
    ((629, 629), (236, 236)),
    ((647, 651), (239, 242)),
    ((655, 655), (244, 244)),
    ((659, 659), (245, 245)),
    ((662, 678), (246, 249)),
    ((680, 696), (250, 253)),
    ((699, 709), (254, 264)),
    ((713, 713), (265, 265)),
    ((739, 743), (268, 271)),
    ((747, 747), (273, 273)),
    ((751, 751), (274, 274)),
    ((754, 770), (275, 278)),
    ((773, 778), (279, 284)),
    ((800, 804), (287, 290)),
    ((806, 817), (292, 294)),
    ((830, 834), (297, 297)),
    ((848, 852), (300, 301)),
    ((855, 864), (303, 303)),
    ((866, 875), (304, 304)),
    ((892, 896), (307, 309)),
    ((900, 901), (311, 312)),
    ((905, 914), (313, 322)),
    ((932, 936), (325, 330)),
    ((950, 954), (333, 333)),
    ((968, 972), (336, 339)),
    ((975, 985), (341, 341)),
    ((987, 997), (342, 343)),
    ((1000, 1000), (344, 344)),
    ((1020, 1024), (347, 349)),
    ((1027, 1040), (351, 353)),
    ((1043, 1045), (354, 356)),
    ((1049, 1056), (357, 364)),
    ((1060, 1063), (365, 368)),
    ((1085, 1089), (371, 373)),
    ((1092, 1111), (375, 378)),
    ((1114, 1114), (379, 379)),
    ((1118, 1121), (380, 383)),
    ((1125, 1130), (384, 389)),
    ((1152, 1156), (392, 394)),
    ((1170, 1174), (397, 401)),
    ((1177, 1196), (403, 407)),
    ((1198, 1217), (408, 412)),
    ((1220, 1220), (413, 413)),
    ((1224, 1224), (414, 414)),
    ((1228, 1228), (415, 415)),
    ((1252, 1256), (418, 424)),
    ((1260, 1260), (426, 426)),
    ((1264, 1264), (427, 427)),
    ((1268, 1269), (428, 429)),
    ((1273, 1285), (430, 442)),
    ((1288, 1301), (443, 444)),
    ((1303, 1319), (445, 448)),
    ((1322, 1323), (449, 450)),
    ((1327, 1327), (451, 451)),
    ((1331, 1334), (452, 455)),
    ((1366, 1370), (458, 462)),
    ((1374, 1374), (464, 464)),
    ((1377, 1396), (465, 469)),
    ((1398, 1411), (470, 471)),
    ((1414, 1414), (472, 472)),
    ((1418, 1418), (473, 473)),
    ((1442, 1446), (476, 480)),
    ((1449, 1468), (482, 486)),
    ((1471, 1471), (487, 487)),
    ((1489, 1493), (490, 494)),
    ((1497, 1497), (496, 496)),
    ((1501, 1501), (497, 497)),
    ((1504, 1523), (498, 502)),
    ((1525, 1544), (503, 507)),
    ((1547, 1555), (508, 518)),
    ((1579, 1583), (521, 525)),
    ((1587, 1587), (528, 528)),
    ((1591, 1591), (529, 529)),
    ((1594, 1613), (530, 534)),
    ((1616, 1621), (535, 540)),
    ((1643, 1647), (543, 545)),
    ((1651, 1658), (547, 554)),
    ((1674, 1678), (557, 561)),
    ((1682, 1684), (563, 565)),
    ((1687, 1699), (566, 567)),
    ((1716, 1720), (570, 575)),
    ((1724, 1726), (577, 579)),
    ((1729, 1741), (580, 581)),
    ((1758, 1762), (584, 586)),
    ((1766, 1767), (588, 589)),
    ((1783, 1787), (592, 593)),
    ((1791, 1811), (595, 615)),
    ((1815, 1815), (616, 616)),
    ((1833, 1837), (619, 620)),
    ((1851, 1855), (623, 624)),
    ((1859, 1862), (626, 629)),
    ((1866, 1872), (630, 636)),
    ((1890, 1894), (639, 643)),
    ((1898, 1898), (645, 645)),
    ((1900, 1911), (646, 648)),
    ((1926, 1930), (651, 655)),
    ((1934, 1935), (657, 658)),
    ((1939, 1939), (659, 659)),
    ((1943, 1953), (660, 670)),
    ((1957, 1959), (671, 673)),
    ((1981, 1985), (676, 680)),
    ((1989, 1990), (682, 683)),
    ((1994, 1994), (684, 684)),
    ((1998, 2010), (685, 697)),
    ((2014, 2023), (698, 707)),
    ((2045, 2049), (710, 715)),
    ((2053, 2053), (717, 717)),
    ((2057, 2064), (718, 725)),
    ((2082, 2086), (728, 736)),
)
