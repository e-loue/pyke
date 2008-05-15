# compiler_bc.py

import itertools
from pyke import contexts, pattern, bc_rule

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
            flag_3 = False
            for x_3 in engine.prove(rule.rule_base.root_name, 'rule_decl', context,
                                    (rule.pattern(2),
                                     rule.pattern(3),
                                     rule.pattern(4),)):
              flag_3 = True
              assert x_3 is None, \
                "compiler.file: got unexpected plan from when clause 3"
              flag_4 = False
              for x_4 in engine.prove(rule.rule_base.root_name, 'fc_rules', context,
                                      (rule.pattern(5),
                                       rule.pattern(6),
                                       rule.pattern(7),)):
                flag_4 = True
                assert x_4 is None, \
                  "compiler.file: got unexpected plan from when clause 4"
                flag_5 = False
                for x_5 in engine.prove(rule.rule_base.root_name, 'bc_rules', context,
                                        (rule.pattern(2),
                                         rule.pattern(8),
                                         rule.pattern(9),
                                         rule.pattern(10),
                                         rule.pattern(11),)):
                  flag_5 = True
                  assert x_5 is None, \
                    "compiler.file: got unexpected plan from when clause 5"
                  mark6 = context.mark(True)
                  if rule.pattern(12).match_data(context, context,
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
                    mark7 = context.mark(True)
                    if rule.pattern(13).match_data(context, context,
                            (("# %s_plans.py" % context.lookup_data('rb_name'),) +
                           context.lookup_data('bc_plan_lines') + ("",) + context.lookup_data('plan_extra_lines')) \
                                                   if context.lookup_data('bc_plan_lines') \
                                                   else ()):
                      context.end_save_all_undo()
                      mark8 = context.mark(True)
                      if rule.pattern(14).match_data(context, context,
                              (context.lookup_data('bc_head'),
                             ("import %s_plans" % context.lookup_data('rb_name')
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
                      context.undo_to_mark(mark8)
                    else: context.end_save_all_undo()
                    context.undo_to_mark(mark7)
                  else: context.end_save_all_undo()
                  context.undo_to_mark(mark6)
                if not flag_5:
                  raise AssertionError("compiler.file: 'when' clause 5 failed")
              if not flag_4:
                raise AssertionError("compiler.file: 'when' clause 4 failed")
            if not flag_3:
              raise AssertionError("compiler.file: 'when' clause 3 failed")
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
                "This_rule_base = engine.get_create('%s')" % context.lookup_data('rb_name')):
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
                "This_rule_base = engine.get_create('%s', '%s', %s)" % \
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
        for x_1 in engine.prove(rule.rule_base.root_name, 'fc_rule', context,
                                (rule.pattern(0),
                                 rule.pattern(1),
                                 rule.pattern(2),)):
          flag_1 = True
          assert x_1 is None, \
            "compiler.fc_rules1: got unexpected plan from when clause 1"
          flag_2 = False
          for x_2 in engine.prove(rule.rule_base.root_name, 'fc_rules', context,
                                  (rule.pattern(3),
                                   rule.pattern(4),
                                   rule.pattern(5),)):
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
        for x_1 in engine.prove(rule.rule_base.root_name, 'fc_premises', context,
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
                                 rule.pattern(10),)):
          flag_1 = True
          assert x_1 is None, \
            "compiler.fc_rule_: got unexpected plan from when clause 1"
          flag_2 = False
          for x_2 in engine.prove(rule.rule_base.root_name, 'assertions', context,
                                  (rule.pattern(11),
                                   rule.pattern(12),
                                   rule.pattern(10),
                                   rule.pattern(13),)):
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
        for x_1 in engine.prove(rule.rule_base.root_name, 'fc_premise', context,
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
                                 rule.pattern(10),)):
          flag_1 = True
          assert x_1 is None, \
            "compiler.fc_premises1: got unexpected plan from when clause 1"
          flag_2 = False
          for x_2 in engine.prove(rule.rule_base.root_name, 'fc_premises', context,
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
                                   rule.pattern(16),)):
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
        for x_1 in engine.prove(rule.rule_base.root_name, 'gen_fc_for', context,
                                (rule.pattern(0),
                                 rule.pattern(1),
                                 rule.pattern(2),
                                 rule.pattern(3),
                                 rule.pattern(4),
                                 rule.pattern(5),
                                 rule.pattern(6),)):
          assert x_1 is None, \
            "compiler.fc_premise: got unexpected plan from when clause 1"
          mark2 = context.mark(True)
          if rule.pattern(7).match_data(context, context,
                  (() if context.lookup_data('break_cond') is None
                 else "if %s: break" % context.lookup_data('break_cond'),
                 'POPINDENT',),):
            context.end_save_all_undo()
            mark3 = context.mark(True)
            if rule.pattern(8).match_data(context, context,
                    context.lookup_data('clause_num') + 1):
              context.end_save_all_undo()
              mark4 = context.mark(True)
              if rule.pattern(9).match_data(context, context,
                      ("('%s', '%s'," % (context.lookup_data('kb_name'), context.lookup_data('entity_name')),
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
                ("for dummy in (None,) if index == %d else \\" % context.lookup_data('clause_num'),
               ('INDENT', 2),
               ('INDENT', 11),
               ('STARTING_LINENO', context.lookup_data('start_lineno')),
               "engine.lookup('%s', '%s', context, "
               "rule.foreach_patterns(%d)):" %
               (context.lookup_data('kb_name'), context.lookup_data('entity_name'), context.lookup_data('clause_num')),
               ('ENDING_LINENO', context.lookup_data('end_lineno')),
               'POPINDENT',)):
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
               "for dummy in engine.lookup('%s', '%s', context, "
               "rule.foreach_patterns(%d)):" %
               (context.lookup_data('kb_name'), context.lookup_data('entity_name'), context.lookup_data('clause_num')),
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
        for x_1 in engine.prove(rule.rule_base.root_name, 'fc_premises', context,
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
                                 rule.pattern(10),)):
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
            for x_3 in engine.prove(rule.rule_base.root_name, 'fc_premises', context,
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
                                     rule.pattern(11),)):
              flag_3 = True
              assert x_3 is None, \
                "compiler.fc_forall_require: got unexpected plan from when clause 3"
              flag_4 = False
              for x_4 in engine.prove(rule.rule_base.root_name, 'fc_premises', context,
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
                                       rule.pattern(17),)):
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
            for x_3 in engine.prove(rule.rule_base.root_name, 'fc_premises', context,
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
                                     rule.pattern(11),)):
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
        for x_1 in engine.prove(rule.rule_base.root_name, 'python_premise', context,
                                (rule.pattern(0),
                                 rule.pattern(1),
                                 rule.pattern(2),
                                 rule.pattern(3),
                                 rule.pattern(4),
                                 rule.pattern(5),
                                 rule.pattern(6),)):
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
        for x_1 in engine.prove(rule.rule_base.root_name, 'assertion', context,
                                (rule.pattern(0),
                                 rule.pattern(1),
                                 rule.pattern(2),
                                 rule.pattern(3),)):
          flag_1 = True
          assert x_1 is None, \
            "compiler.assertions_n: got unexpected plan from when clause 1"
          flag_2 = False
          for x_2 in engine.prove(rule.rule_base.root_name, 'assertions', context,
                                  (rule.pattern(4),
                                   rule.pattern(5),
                                   rule.pattern(3),
                                   rule.pattern(6),)):
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
                 "engine.assert_('%s', '%s'," % (context.lookup_data('kb_name'), context.lookup_data('entity_name')),
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
        for x_1 in engine.prove(rule.rule_base.root_name, 'bc_rule', context,
                                (rule.pattern(0),
                                 rule.pattern(1),
                                 rule.pattern(2),
                                 rule.pattern(3),
                                 rule.pattern(4),)):
          flag_1 = True
          assert x_1 is None, \
            "compiler.bc_rules1: got unexpected plan from when clause 1"
          flag_2 = False
          for x_2 in engine.prove(rule.rule_base.root_name, 'bc_rules', context,
                                  (rule.pattern(0),
                                   rule.pattern(5),
                                   rule.pattern(6),
                                   rule.pattern(7),
                                   rule.pattern(8),)):
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
        for x_1 in engine.prove(rule.rule_base.root_name, 'bc_premises', context,
                                (rule.pattern(0),
                                 rule.pattern(1),
                                 rule.pattern(2),
                                 rule.pattern(3),
                                 rule.pattern(4),
                                 rule.pattern(5),
                                 rule.pattern(6),
                                 rule.pattern(7),)):
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
        for x_1 in engine.prove(rule.rule_base.root_name, 'bc_premises1', context,
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
                                 rule.pattern(13),)):
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
        for x_1 in engine.prove(rule.rule_base.root_name, 'bc_premise', context,
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
                                 rule.pattern(13),)):
          flag_1 = True
          assert x_1 is None, \
            "compiler.bc_premises1_n: got unexpected plan from when clause 1"
          flag_2 = False
          for x_2 in engine.prove(rule.rule_base.root_name, 'bc_premises1', context,
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
                                   rule.pattern(20),)):
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
                     "for x_%(clause_num)d in "
                     "engine.prove(%(kb_name)s, %(entity_name)s, context," %
                     {'clause_num': context.lookup_data('clause_num'),
                     'kb_name': context.lookup_data('kb_name2'),
                     'entity_name': context.lookup_data('entity_name')},
                     ('INDENT', 2),
                     ('INDENT', 22),
                     helpers.list_format(('rule.pattern(%d)' % pat_num
                     for pat_num in context.lookup_data('pat_nums')),
                     '(', ')):'),
                     "POPINDENT",
                     )):
                context.end_save_all_undo()
                flag_5 = False
                for x_5 in engine.prove(rule.rule_base.root_name, 'add_required', context,
                                        (rule.pattern(4),
                                         rule.pattern(5),
                                         rule.pattern(6),
                                         rule.pattern(7),
                                         rule.pattern(3),
                                         rule.pattern(8),
                                         rule.pattern(9),
                                         rule.pattern(10),)):
                  flag_5 = True
                  assert x_5 is None, \
                    "compiler.bc_premise: got unexpected plan from when clause 5"
                  flag_6 = False
                  for x_6 in engine.prove(rule.rule_base.root_name, 'gen_plan_lines', context,
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
                                           rule.pattern(18),)):
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
        for x_1 in engine.prove(rule.rule_base.root_name, 'bc_premises1', context,
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
                                 rule.pattern(13),)):
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
            for x_3 in engine.prove(rule.rule_base.root_name, 'bc_premises1', context,
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
                                     rule.pattern(14),)):
              flag_3 = True
              assert x_3 is None, \
                "compiler.bc_forall_require: got unexpected plan from when clause 3"
              flag_4 = False
              for x_4 in engine.prove(rule.rule_base.root_name, 'bc_premises1', context,
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
                                       rule.pattern(20),)):
                flag_4 = True
                assert x_4 is None, \
                  "compiler.bc_forall_require: got unexpected plan from when clause 4"
                mark5 = context.mark(True)
                if rule.pattern(21).match_data(context, context,
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
            for x_3 in engine.prove(rule.rule_base.root_name, 'bc_premises1', context,
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
                                     rule.pattern(14),)):
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
                           helpers.merge_pattern("contexts.variable('%s')" % context.lookup_data('pat_var_name'),
               context.lookup_data('patterns_in'))):
          context.end_save_all_undo()
          flag_2 = False
          for x_2 in engine.prove(rule.rule_base.root_name, 'plan_bindings', context,
                                  (rule.pattern(1),
                                   rule.pattern(2),
                                   rule.pattern(3),
                                   rule.pattern(4),
                                   rule.pattern(5),
                                   rule.pattern(6),
                                   rule.pattern(7),)):
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
                           helpers.merge_pattern("contexts.variable('%s')" % context.lookup_data('plan_var_name'),
               context.lookup_data('patterns_in'))):
          context.end_save_all_undo()
          flag_2 = False
          for x_2 in engine.prove(rule.rule_base.root_name, 'plan_bindings', context,
                                  (rule.pattern(1),
                                   rule.pattern(2),
                                   rule.pattern(3),
                                   rule.pattern(4),
                                   rule.pattern(5),
                                   rule.pattern(6),
                                   rule.pattern(7),)):
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
          for x_2 in engine.prove(rule.rule_base.root_name, 'python_premise', context,
                                  (rule.pattern(1),
                                   rule.pattern(2),
                                   rule.pattern(3),
                                   rule.pattern(4),
                                   rule.pattern(5),
                                   rule.pattern(6),
                                   rule.pattern(7),)):
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

def populate(engine):
  This_rule_base = engine.get_create('compiler')
  
  bc_rule.bc_rule('file', This_rule_base, 'compile',
                  file, None,
                  (contexts.variable('rb_name'),
                   pattern.pattern_tuple((pattern.pattern_literal('file'), contexts.variable('parent'), pattern.pattern_tuple((contexts.variable('fc_rules'), contexts.variable('fc_extra_lines'),), None), pattern.pattern_tuple((contexts.variable('bc_rules'), contexts.variable('bc_extra_lines'), contexts.variable('plan_extra_lines'),), None),), None),
                   contexts.variable('fc_lines'),
                   contexts.variable('bc_lines'),
                   contexts.variable('plan_lines'),),
                  (),
                  (contexts.variable('fc_head'),
                   contexts.variable('bc_head'),
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
                   contexts.anonymous(),
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
                  (contexts.anonymous(),
                   contexts.variable('clause_num'),
                   contexts.variable('clause_num'),
                   pattern.pattern_literal(()),
                   contexts.anonymous(),
                   contexts.anonymous(),
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
  
  bc_rule.bc_rule('fc_forall_None', This_rule_base, 'fc_premise',
                  fc_forall_None, None,
                  (contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   contexts.variable('next_clause_num'),
                   pattern.pattern_tuple((pattern.pattern_literal('fc_forall'), contexts.variable('premises1'), pattern.pattern_literal(None), contexts.anonymous(), contexts.anonymous(),), None),
                   contexts.anonymous(),
                   contexts.anonymous(),
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
                   pattern.pattern_tuple((pattern.pattern_literal('fc_forall'), contexts.variable('premises1'), contexts.variable('require'), contexts.variable('start_lineno'), contexts.anonymous(),), None),
                   contexts.anonymous(),
                   contexts.anonymous(),
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
                   contexts.anonymous(),
                   contexts.anonymous(),
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
                   contexts.anonymous(),
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
                  (pattern.pattern_tuple((pattern.pattern_literal('python_assertion'), pattern.pattern_tuple((contexts.variable('python_code'), contexts.anonymous(), contexts.anonymous(), contexts.anonymous(),), None), contexts.variable('start_lineno'), contexts.variable('end_lineno'),), None),
                   pattern.pattern_tuple((pattern.pattern_tuple((pattern.pattern_literal('STARTING_LINENO'), contexts.variable('start_lineno'),), None), contexts.variable('python_code'), pattern.pattern_tuple((pattern.pattern_literal('ENDING_LINENO'), contexts.variable('end_lineno'),), None),), None),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_in'),),
                  (),
                  ())
  
  bc_rule.bc_rule('bc_rules0', This_rule_base, 'bc_rules',
                  bc_rules0, None,
                  (contexts.anonymous(),
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
                   contexts.anonymous(),
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
                  (contexts.anonymous(),
                   contexts.anonymous(),
                   contexts.variable('clause_num'),
                   contexts.variable('clause_num'),
                   pattern.pattern_literal(()),
                   contexts.anonymous(),
                   contexts.anonymous(),
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
                   pattern.pattern_literal(('POPINDENT',)),
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
                   pattern.pattern_tuple((contexts.anonymous(), contexts.variable('plan_var_names_out'),), None),
                   contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),))
  
  bc_rule.bc_rule('bc_forall_None', This_rule_base, 'bc_premise',
                  bc_forall_None, None,
                  (contexts.variable('rb_name'),
                   contexts.variable('rule_name'),
                   contexts.variable('clause_num'),
                   contexts.variable('next_clause_num'),
                   pattern.pattern_tuple((pattern.pattern_literal('bc_forall'), contexts.variable('bc_premises'), pattern.pattern_literal(None), contexts.anonymous(), contexts.anonymous(),), None),
                   contexts.anonymous(),
                   contexts.anonymous(),
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
                   pattern.pattern_tuple((pattern.pattern_literal('bc_forall'), contexts.variable('premises1'), contexts.variable('require'), contexts.variable('start_lineno'), contexts.anonymous(),), None),
                   contexts.anonymous(),
                   contexts.anonymous(),
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
                   contexts.anonymous(),
                   contexts.anonymous(),
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
                   contexts.anonymous(),
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
                   contexts.anonymous(),
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
                   pattern.pattern_tuple((pattern.pattern_literal('plan_spec'), contexts.variable('step_num'), contexts.variable('plan_var_name'), contexts.variable('python_code'), contexts.variable('plan_vars_needed'), contexts.anonymous(), contexts.anonymous(),), None),
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
                  (contexts.anonymous(),
                   contexts.anonymous(),
                   contexts.anonymous(),
                   pattern.pattern_tuple((pattern.pattern_literal('plan_spec'), contexts.anonymous(), contexts.anonymous(), contexts.anonymous(), contexts.anonymous(), contexts.variable('lineno'), contexts.variable('lexpos'),), None),
                   pattern.pattern_literal(False),
                   contexts.anonymous(),
                   contexts.anonymous(),
                   contexts.anonymous(),
                   contexts.anonymous(),
                   contexts.anonymous(),
                   contexts.anonymous(),),
                  (),
                  (contexts.anonymous(),))
  
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
                   contexts.anonymous(),
                   contexts.anonymous(),
                   contexts.anonymous(),
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
                   contexts.anonymous(),
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
                   pattern.pattern_tuple((pattern.pattern_literal('python_eq'), contexts.variable('pattern'), pattern.pattern_tuple((contexts.variable('python_code'), contexts.anonymous(), contexts.anonymous(), contexts.anonymous(),), None), contexts.variable('start_lineno'), contexts.variable('end_lineno'),), None),
                   contexts.anonymous(),
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
                   pattern.pattern_tuple((pattern.pattern_literal('python_in'), contexts.variable('pattern'), pattern.pattern_tuple((contexts.variable('python_code'), contexts.anonymous(), contexts.anonymous(), contexts.anonymous(),), None), contexts.variable('start_lineno'), contexts.variable('end_lineno'),), None),
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
                   pattern.pattern_tuple((pattern.pattern_literal('python_check'), pattern.pattern_tuple((contexts.variable('python_code'), contexts.anonymous(), contexts.anonymous(), contexts.anonymous(),), None), contexts.variable('start_lineno'), contexts.variable('end_lineno'),), None),
                   contexts.anonymous(),
                   contexts.variable('patterns_in'),
                   contexts.variable('patterns_in'),
                   contexts.variable('fn_head'),
                   pattern.pattern_literal(('POPINDENT',)),),
                  (),
                  (contexts.variable('python_code2'),
                   contexts.variable('fn_head'),))

from pyke.krb_compiler import helpers
Krb_filename = 'D:\Projekte\Pyke\trunk\pyke\krb_compiler\compiler.krb'
Krb_lineno_map = (
    ((12, 16), (24, 28)),
    ((20, 20), (30, 30)),
    ((24, 24), (31, 31)),
    ((27, 33), (32, 32)),
    ((35, 41), (33, 33)),
    ((43, 51), (34, 35)),
    ((54, 66), (36, 48)),
    ((70, 73), (49, 52)),
    ((77, 91), (53, 67)),
    ((121, 125), (70, 70)),
    ((129, 129), (72, 72)),
    ((145, 149), (75, 75)),
    ((153, 155), (77, 79)),
    ((171, 175), (82, 82)),
    ((189, 193), (85, 87)),
    ((196, 202), (89, 89)),
    ((204, 210), (90, 90)),
    ((227, 231), (93, 94)),
    ((234, 248), (96, 98)),
    ((250, 257), (99, 100)),
    ((260, 277), (101, 118)),
    ((281, 288), (119, 126)),
    ((310, 314), (129, 130)),
    ((328, 332), (133, 136)),
    ((335, 349), (138, 141)),
    ((351, 365), (142, 145)),
    ((368, 368), (146, 146)),
    ((388, 392), (149, 154)),
    ((394, 403), (156, 157)),
    ((406, 408), (158, 160)),
    ((412, 412), (161, 161)),
    ((416, 421), (162, 167)),
    ((441, 445), (170, 171)),
    ((449, 457), (173, 181)),
    ((473, 477), (184, 185)),
    ((481, 486), (187, 192)),
    ((502, 506), (195, 198)),
    ((509, 523), (200, 203)),
    ((526, 526), (204, 204)),
    ((544, 548), (207, 210)),
    ((552, 552), (212, 212)),
    ((556, 556), (213, 213)),
    ((559, 573), (214, 217)),
    ((575, 589), (218, 221)),
    ((592, 602), (222, 232)),
    ((606, 606), (233, 233)),
    ((632, 636), (236, 239)),
    ((640, 640), (241, 241)),
    ((644, 644), (242, 242)),
    ((647, 661), (243, 246)),
    ((664, 669), (247, 252)),
    ((691, 695), (255, 258)),
    ((697, 706), (260, 262)),
    ((719, 723), (265, 265)),
    ((737, 741), (268, 269)),
    ((744, 751), (271, 271)),
    ((753, 760), (272, 272)),
    ((777, 781), (275, 277)),
    ((785, 786), (279, 280)),
    ((790, 799), (281, 290)),
    ((817, 821), (293, 298)),
    ((835, 839), (301, 301)),
    ((853, 857), (304, 307)),
    ((860, 868), (309, 309)),
    ((870, 878), (310, 311)),
    ((881, 881), (312, 312)),
    ((901, 905), (315, 317)),
    ((908, 919), (319, 321)),
    ((922, 924), (322, 324)),
    ((928, 935), (325, 332)),
    ((939, 942), (333, 336)),
    ((964, 968), (339, 341)),
    ((971, 988), (343, 346)),
    ((991, 991), (347, 347)),
    ((995, 998), (348, 351)),
    ((1002, 1007), (352, 357)),
    ((1029, 1033), (360, 362)),
    ((1047, 1051), (365, 369)),
    ((1054, 1071), (371, 375)),
    ((1073, 1090), (376, 380)),
    ((1093, 1093), (381, 381)),
    ((1097, 1097), (382, 382)),
    ((1101, 1101), (383, 383)),
    ((1125, 1129), (386, 392)),
    ((1133, 1133), (394, 394)),
    ((1137, 1137), (395, 395)),
    ((1141, 1142), (396, 397)),
    ((1146, 1158), (398, 410)),
    ((1161, 1172), (411, 412)),
    ((1174, 1188), (413, 416)),
    ((1191, 1192), (417, 418)),
    ((1196, 1196), (419, 419)),
    ((1200, 1203), (420, 423)),
    ((1235, 1239), (426, 430)),
    ((1242, 1259), (432, 436)),
    ((1262, 1262), (437, 437)),
    ((1280, 1284), (440, 444)),
    ((1288, 1288), (446, 446)),
    ((1292, 1292), (447, 447)),
    ((1295, 1312), (448, 452)),
    ((1314, 1331), (453, 457)),
    ((1334, 1344), (458, 468)),
    ((1368, 1372), (471, 475)),
    ((1376, 1376), (478, 478)),
    ((1380, 1380), (479, 479)),
    ((1383, 1400), (480, 484)),
    ((1403, 1408), (485, 490)),
    ((1430, 1434), (493, 495)),
    ((1438, 1445), (497, 504)),
    ((1461, 1465), (507, 511)),
    ((1469, 1471), (513, 515)),
    ((1474, 1484), (516, 517)),
    ((1501, 1505), (520, 525)),
    ((1509, 1511), (527, 529)),
    ((1514, 1524), (530, 531)),
    ((1541, 1545), (534, 536)),
    ((1549, 1550), (538, 539)),
    ((1566, 1570), (542, 543)),
    ((1574, 1594), (545, 565)),
    ((1598, 1598), (566, 566)),
    ((1616, 1620), (569, 570)),
    ((1634, 1638), (573, 574)),
    ((1642, 1645), (576, 579)),
    ((1649, 1655), (580, 586)),
    ((1673, 1677), (589, 593)),
    ((1681, 1681), (595, 595)),
    ((1683, 1692), (596, 598)),
    ((1707, 1711), (601, 605)),
    ((1715, 1716), (607, 608)),
    ((1720, 1720), (609, 609)),
    ((1724, 1734), (610, 620)),
    ((1738, 1740), (621, 623)),
    ((1762, 1766), (626, 630)),
    ((1770, 1771), (632, 633)),
    ((1775, 1775), (634, 634)),
    ((1779, 1791), (635, 647)),
    ((1795, 1804), (648, 657)),
    ((1826, 1830), (660, 665)),
    ((1834, 1834), (667, 667)),
    ((1838, 1845), (668, 675)),
)
