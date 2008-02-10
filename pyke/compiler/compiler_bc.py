# compiler_bc.py

from pyke import tmp_itertools as itertools
from pyke import rule_base, contexts, pattern, bc_rule
from pyke import prove

def file(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                helpers.fc_head(context.lookup_data('rb_name'))):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                  helpers.bc_head(context.lookup_data('rb_name'))):
            context.end_save_all_undo()
            flag_3 = False
            for x_3 in prove(rule.rule_base.root_name, 'rule_decl', context,
                           (rule.pattern(2),
                            rule.pattern(3),
                            rule.pattern(4),)):
              flag_3 = True
              assert x_3 is None, \
                "compiler.file: got unexpected plan from when clause 3"
              flag_4 = False
              for x_4 in prove(rule.rule_base.root_name, 'fc_rules', context,
                             (rule.pattern(5),
                              rule.pattern(6),
                              rule.pattern(7),)):
                flag_4 = True
                assert x_4 is None, \
                  "compiler.file: got unexpected plan from when clause 4"
                flag_5 = False
                for x_5 in prove(rule.rule_base.root_name, 'bc_rules', context,
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
                         context.lookup_data('decl_line'),
                         context.lookup_data('fc_init_lines'),
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
                             context.lookup_data('decl_line'),
                             context.lookup_data('bc_bc_init_lines'),
                             "",
                             context.lookup_data('bc_extra_lines')) \
                                                     if context.lookup_data('bc_bc_fun_lines') \
                                                     else ()):
                        context.end_save_all_undo()
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
    finally:
      context.done()

def rule_decl(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                "This_rule_base = rule_base.get_create('%s')" % context.lookup_data('rb_name')):
          context.end_save_all_undo()
          yield
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
    finally:
      context.done()

def rule_decl_with_parent(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                "This_rule_base = rule_base.get_create('%s', '%s', %s)" % \
                                        (context.lookup_data('rb_name'), context.lookup_data('parent'),
               tuple(repr(sym) for sym in context.lookup_data('excluded_symbols')))):
          context.end_save_all_undo()
          yield
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
    finally:
      context.done()

def fc_rules0(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        yield
    finally:
      context.done()

def fc_rules1(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        flag_1 = False
        for x_1 in prove(rule.rule_base.root_name, 'fc_rule', context,
                       (rule.pattern(0),
                        rule.pattern(1),
                        rule.pattern(2),)):
          flag_1 = True
          assert x_1 is None, \
            "compiler.fc_rules1: got unexpected plan from when clause 1"
          flag_2 = False
          for x_2 in prove(rule.rule_base.root_name, 'fc_rules', context,
                         (rule.pattern(3),
                          rule.pattern(4),
                          rule.pattern(5),)):
            flag_2 = True
            assert x_2 is None, \
              "compiler.fc_rules1: got unexpected plan from when clause 2"
            yield
          if not flag_2:
            raise AssertionError("compiler.fc_rules1: 'when' clause 2 failed")
        if not flag_1:
          raise AssertionError("compiler.fc_rules1: 'when' clause 1 failed")
    finally:
      context.done()

def fc_rule_(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        flag_1 = False
        for x_1 in prove(rule.rule_base.root_name, 'fc_premises', context,
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
            "compiler.fc_rule_: got unexpected plan from when clause 1"
          flag_2 = False
          for x_2 in prove(rule.rule_base.root_name, 'assertions', context,
                         (rule.pattern(8),
                          rule.pattern(9),
                          rule.pattern(7),
                          rule.pattern(10),)):
            flag_2 = True
            assert x_2 is None, \
              "compiler.fc_rule_: got unexpected plan from when clause 2"
            mark3 = context.mark(True)
            if rule.pattern(11).match_data(context, context,
                    ("",
                   "def %s(rule, context = None, index = None):" % context.lookup_data('rule_name'),
                   ("INDENT", 2),
                   "if context is None: context = contexts.simple_context()",
                   "try:",
                   ("INDENT", 2),
                   context.lookup_data('prem_fn_head'),
                   context.lookup_data('asserts_fn_lines'),
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
              if rule.pattern(12).match_data(context, context,
                      ("",
                     "fc_rule.fc_rule('%(name)s', This_rule_base, %(name)s," %
                     {'name': context.lookup_data('rule_name')},
                     ("INDENT", 2),
                     helpers.add_brackets(context.lookup_data('prem_decl_lines'), '(', '),'),
                     helpers.list_format(context.lookup_data('patterns_out'), '(', '))'),
                     "POPINDENT",
                     )):
                context.end_save_all_undo()
                yield
              else: context.end_save_all_undo()
              context.undo_to_mark(mark4)
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          if not flag_2:
            raise AssertionError("compiler.fc_rule_: 'when' clause 2 failed")
        if not flag_1:
          raise AssertionError("compiler.fc_rule_: 'when' clause 1 failed")
    finally:
      context.done()

def fc_premises0(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        yield
    finally:
      context.done()

def fc_premises1(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        flag_1 = False
        for x_1 in prove(rule.rule_base.root_name, 'fc_premise', context,
                       (rule.pattern(0),
                        rule.pattern(1),
                        rule.pattern(2),
                        rule.pattern(3),
                        rule.pattern(4),
                        rule.pattern(5),
                        rule.pattern(6),
                        rule.pattern(7),
                        rule.pattern(8),)):
          flag_1 = True
          assert x_1 is None, \
            "compiler.fc_premises1: got unexpected plan from when clause 1"
          flag_2 = False
          for x_2 in prove(rule.rule_base.root_name, 'fc_premises', context,
                         (rule.pattern(0),
                          rule.pattern(2),
                          rule.pattern(9),
                          rule.pattern(10),
                          rule.pattern(11),
                          rule.pattern(12),
                          rule.pattern(8),
                          rule.pattern(13),)):
            flag_2 = True
            assert x_2 is None, \
              "compiler.fc_premises1: got unexpected plan from when clause 2"
            mark3 = context.mark(True)
            if rule.pattern(14).match_data(context, context,
                    context.lookup_data('decl_lines1') + context.lookup_data('decl_lines2')):
              context.end_save_all_undo()
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          if not flag_2:
            raise AssertionError("compiler.fc_premises1: 'when' clause 2 failed")
        if not flag_1:
          raise AssertionError("compiler.fc_premises1: 'when' clause 1 failed")
    finally:
      context.done()

def fc_premise(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                ("for dummy in (None,) if index == %d else \\" % context.lookup_data('clause_num'),
               ('INDENT', 2),
               ('INDENT', 11),
               ('STARTING_LINENO', context.lookup_data('start_lineno')),
               "lookup('%s', '%s', context, rule.foreach_patterns(%d)):" %
               (context.lookup_data('kb_name'), context.lookup_data('entity_name'), context.lookup_data('clause_num')),
               ('ENDING_LINENO', context.lookup_data('end_lineno')),
               'POPINDENT',)):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                  context.lookup_data('clause_num') + 1):
            context.end_save_all_undo()
            mark3 = context.mark(True)
            if rule.pattern(2).match_data(context, context,
                    ("('%s', '%s'," % (context.lookup_data('kb_name'), context.lookup_data('entity_name')),
                   ('INDENT', 1),
                   helpers.list_format(context.lookup_data('arg_patterns'), '(', ')),'),
                   "POPINDENT",
                   )):
              context.end_save_all_undo()
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
    finally:
      context.done()

def fc_python_premise(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        for x_1 in prove(rule.rule_base.root_name, 'python_premise', context,
                       (rule.pattern(0),
                        rule.pattern(1),
                        rule.pattern(2),
                        rule.pattern(3),
                        rule.pattern(4),
                        rule.pattern(5),)):
          assert x_1 is None, \
            "compiler.fc_python_premise: got unexpected plan from when clause 1"
          yield
    finally:
      context.done()

def assertions_0(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        yield
    finally:
      context.done()

def assertions_n(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        flag_1 = False
        for x_1 in prove(rule.rule_base.root_name, 'assertion', context,
                       (rule.pattern(0),
                        rule.pattern(1),
                        rule.pattern(2),
                        rule.pattern(3),)):
          flag_1 = True
          assert x_1 is None, \
            "compiler.assertions_n: got unexpected plan from when clause 1"
          flag_2 = False
          for x_2 in prove(rule.rule_base.root_name, 'assertions', context,
                         (rule.pattern(4),
                          rule.pattern(5),
                          rule.pattern(3),
                          rule.pattern(6),)):
            flag_2 = True
            assert x_2 is None, \
              "compiler.assertions_n: got unexpected plan from when clause 2"
            yield
          if not flag_2:
            raise AssertionError("compiler.assertions_n: 'when' clause 2 failed")
        if not flag_1:
          raise AssertionError("compiler.assertions_n: 'when' clause 1 failed")
    finally:
      context.done()

def assertion(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                \
                           helpers.merge_patterns(context.lookup_data('patterns'), context.lookup_data('patterns_in'))):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                  (('STARTING_LINENO', context.lookup_data('start_lineno')),
                 "assert_('%s', '%s'," % (context.lookup_data('kb_name'), context.lookup_data('entity_name')),
                 ('INDENT', 8),
                 helpers.list_format(
                 ("rule.pattern(%d).as_data(context)" % pat_num
                 for pat_num in context.lookup_data('pat_nums')),
                 '(', ')),'),
                 ('ENDING_LINENO', context.lookup_data('end_lineno')),
                 "POPINDENT",
                 )):
            context.end_save_all_undo()
            yield
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
    finally:
      context.done()

def python_assertion(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        yield
    finally:
      context.done()

def bc_rules0(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        yield
    finally:
      context.done()

def bc_rules1(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        flag_1 = False
        for x_1 in prove(rule.rule_base.root_name, 'bc_rule', context,
                       (rule.pattern(0),
                        rule.pattern(1),
                        rule.pattern(2),
                        rule.pattern(3),
                        rule.pattern(4),)):
          flag_1 = True
          assert x_1 is None, \
            "compiler.bc_rules1: got unexpected plan from when clause 1"
          flag_2 = False
          for x_2 in prove(rule.rule_base.root_name, 'bc_rules', context,
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
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          if not flag_2:
            raise AssertionError("compiler.bc_rules1: 'when' clause 2 failed")
        if not flag_1:
          raise AssertionError("compiler.bc_rules1: 'when' clause 1 failed")
    finally:
      context.done()

def bc_rule_(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        flag_1 = False
        for x_1 in prove(rule.rule_base.root_name, 'bc_premises', context,
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
                   'yield context' if context.lookup_data('plan_lines') else 'yield',
                   context.lookup_data('prem_fn_tail'),
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
                yield
              else: context.end_save_all_undo()
              context.undo_to_mark(mark4)
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        if not flag_1:
          raise AssertionError("compiler.bc_rule_: 'when' clause 1 failed")
    finally:
      context.done()

def bc_premises(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        flag_1 = False
        for x_1 in prove(rule.rule_base.root_name, 'bc_premises1', context,
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
            "compiler.bc_premises: got unexpected plan from when clause 1"
          mark2 = context.mark(True)
          if rule.pattern(11).match_data(context, context,
                  helpers.list_format(context.lookup_data('patterns'), '(', '))')):
            context.end_save_all_undo()
            mark3 = context.mark(True)
            if rule.pattern(12).match_data(context, context,
                    ('(' + ' '.join(tuple(repr(plan_var_name) + ','
                   for plan_var_name
                   in context.lookup_data('plan_var_names'))) +
                   '),',) + context.lookup_data('pat_lines')):
              context.end_save_all_undo()
              mark4 = context.mark(True)
              if rule.pattern(13).match_data(context, context,
                      tuple(itertools.chain(itertools.chain(
                     ((lines for step, lines in context.lookup_data('plan_lines1') if step is None),
                     (lines for step, lines
                     in sorted(((step, lines) for step, lines in context.lookup_data('plan_lines1')
                     if step is not None),
                     key=lambda (step, lines): step))))))):
                context.end_save_all_undo()
                yield
              else: context.end_save_all_undo()
              context.undo_to_mark(mark4)
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        if not flag_1:
          raise AssertionError("compiler.bc_premises: 'when' clause 1 failed")
    finally:
      context.done()

def bc_premises1_0(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        yield
    finally:
      context.done()

def bc_premises1_n(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        flag_1 = False
        for x_1 in prove(rule.rule_base.root_name, 'bc_premise', context,
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
            "compiler.bc_premises1_n: got unexpected plan from when clause 1"
          mark2 = context.mark(True)
          if rule.pattern(11).match_data(context, context,
                  context.lookup_data('clause_num') + 1):
            context.end_save_all_undo()
            flag_3 = False
            for x_3 in prove(rule.rule_base.root_name, 'bc_premises1', context,
                           (rule.pattern(0),
                            rule.pattern(1),
                            rule.pattern(11),
                            rule.pattern(12),
                            rule.pattern(5),
                            rule.pattern(13),
                            rule.pattern(7),
                            rule.pattern(14),
                            rule.pattern(15),
                            rule.pattern(16),
                            rule.pattern(17),)):
              flag_3 = True
              assert x_3 is None, \
                "compiler.bc_premises1_n: got unexpected plan from when clause 3"
              mark4 = context.mark(True)
              if rule.pattern(18).match_data(context, context,
                      context.lookup_data('plan_lines1') + context.lookup_data('plan_lines2')):
                context.end_save_all_undo()
                mark5 = context.mark(True)
                if rule.pattern(19).match_data(context, context,
                        context.lookup_data('fn_head1') + context.lookup_data('fn_head2')):
                  context.end_save_all_undo()
                  mark6 = context.mark(True)
                  if rule.pattern(20).match_data(context, context,
                          context.lookup_data('fn_tail2') + context.lookup_data('fn_tail1')):
                    context.end_save_all_undo()
                    yield
                  else: context.end_save_all_undo()
                  context.undo_to_mark(mark6)
                else: context.end_save_all_undo()
                context.undo_to_mark(mark5)
              else: context.end_save_all_undo()
              context.undo_to_mark(mark4)
            if not flag_3:
              raise AssertionError("compiler.bc_premises1_n: 'when' clause 3 failed")
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        if not flag_1:
          raise AssertionError("compiler.bc_premises1_n: 'when' clause 1 failed")
    finally:
      context.done()

def bc_premise(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                context.lookup_data('kb_name') or "rule.rule_base.root_name"):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                  \
                             helpers.merge_patterns(context.lookup_data('arg_patterns'), context.lookup_data('patterns_in'))):
            context.end_save_all_undo()
            mark3 = context.mark(True)
            if rule.pattern(2).match_data(context, context,
                    (('STARTING_LINENO', context.lookup_data('start_lineno')),
                   "for x_%(clause_num)d in "
                   "prove(%(kb_name)s, %(entity_name)s, context," %
                   {'clause_num': context.lookup_data('clause_num'),
                   'kb_name': context.lookup_data('kb_name2'),
                   'entity_name': context.lookup_data('entity_name')},
                   ('INDENT', 2),
                   ('INDENT', 13),
                   helpers.list_format(('rule.pattern(%d)' % pat_num
                   for pat_num in context.lookup_data('pat_nums')),
                   '(', ')):'),
                   "POPINDENT",
                   )):
              context.end_save_all_undo()
              flag_4 = False
              for x_4 in prove(rule.rule_base.root_name, 'add_required', context,
                             (rule.pattern(3),
                              rule.pattern(4),
                              rule.pattern(5),
                              rule.pattern(6),
                              rule.pattern(2),
                              rule.pattern(7),
                              rule.pattern(8),
                              rule.pattern(9),)):
                flag_4 = True
                assert x_4 is None, \
                  "compiler.bc_premise: got unexpected plan from when clause 4"
                flag_5 = False
                for x_5 in prove(rule.rule_base.root_name, 'gen_plan_lines', context,
                               (rule.pattern(4),
                                rule.pattern(5),
                                rule.pattern(6),
                                rule.pattern(10),
                                rule.pattern(11),
                                rule.pattern(12),
                                rule.pattern(13),
                                rule.pattern(14),
                                rule.pattern(15),
                                rule.pattern(16),)):
                  flag_5 = True
                  assert x_5 is None, \
                    "compiler.bc_premise: got unexpected plan from when clause 5"
                  mark6 = context.mark(True)
                  if rule.pattern(17).match_data(context, context,
                          helpers.merge_patterns(context.lookup_data('plan_vars_needed'),
                         context.lookup_data('plan_var_names_in'))):
                    context.end_save_all_undo()
                    mark7 = context.mark(True)
                    if rule.pattern(18).match_data(context, context,
                            context.lookup_data('fn_head2') + context.lookup_data('fn_head3') + (('ENDING_LINENO', context.lookup_data('end_lineno')),)):
                      context.end_save_all_undo()
                      mark8 = context.mark(True)
                      if rule.pattern(19).match_data(context, context,
                              context.lookup_data('fn_tail3') + context.lookup_data('fn_tail2')):
                        context.end_save_all_undo()
                        yield
                      else: context.end_save_all_undo()
                      context.undo_to_mark(mark8)
                    else: context.end_save_all_undo()
                    context.undo_to_mark(mark7)
                  else: context.end_save_all_undo()
                  context.undo_to_mark(mark6)
                if not flag_5:
                  raise AssertionError("compiler.bc_premise: 'when' clause 5 failed")
              if not flag_4:
                raise AssertionError("compiler.bc_premise: 'when' clause 4 failed")
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
    finally:
      context.done()

def no_plan(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
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
          yield
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
    finally:
      context.done()

def as_plan(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                \
                           helpers.merge_pattern("contexts.variable('%s')" % context.lookup_data('pat_var_name'),
               context.lookup_data('patterns_in'))):
          context.end_save_all_undo()
          flag_2 = False
          for x_2 in prove(rule.rule_base.root_name, 'plan_bindings', context,
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
            yield
          if not flag_2:
            raise AssertionError("compiler.as_plan: 'when' clause 2 failed")
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
    finally:
      context.done()

def plan_spec(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
                \
                           helpers.merge_pattern("contexts.variable('%s')" % context.lookup_data('plan_var_name'),
               context.lookup_data('patterns_in'))):
          context.end_save_all_undo()
          flag_2 = False
          for x_2 in prove(rule.rule_base.root_name, 'plan_bindings', context,
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
            yield
          if not flag_2:
            raise AssertionError("compiler.plan_spec: 'when' clause 2 failed")
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
    finally:
      context.done()

def plan_bindings(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
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
            yield
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
    finally:
      context.done()

def not_required(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        yield
    finally:
      context.done()

def required(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
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
            yield
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
    finally:
      context.done()

def bc_python_premise(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        for x_1 in prove(rule.rule_base.root_name, 'python_premise', context,
                       (rule.pattern(0),
                        rule.pattern(1),
                        rule.pattern(2),
                        rule.pattern(3),
                        rule.pattern(4),
                        rule.pattern(5),)):
          assert x_1 is None, \
            "compiler.bc_python_premise: got unexpected plan from when clause 1"
          yield
    finally:
      context.done()

def python_eq(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
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
                yield
              else: context.end_save_all_undo()
              context.undo_to_mark(mark4)
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
    finally:
      context.done()

def python_in(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
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
                      ('POPINDENT',
                     "else: context.end_save_all_undo()",
                     "context.undo_to_mark(mark%d)" % context.lookup_data('clause_num'),
                     'POPINDENT',)):
                context.end_save_all_undo()
                yield
              else: context.end_save_all_undo()
              context.undo_to_mark(mark4)
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
    finally:
      context.done()

def python_check(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
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
            yield
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
    finally:
      context.done()

This_rule_base = rule_base.get_create('compiler')

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
                 contexts.variable('fc_premises'),
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
                 contexts.anonymous(),
                 pattern.pattern_literal(()),
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
                 pattern.pattern_tuple((contexts.variable('first_prem'),), contexts.variable('rest_prems')),
                 pattern.pattern_tuple((contexts.variable('fn_head1'),), contexts.variable('fn_head2')),
                 pattern.pattern_tuple((contexts.variable('fn_tail2'), contexts.variable('fn_tail1'),), None),
                 contexts.variable('decl_lines'),
                 contexts.variable('patterns_in'),
                 contexts.variable('patterns_out'),),
                (),
                (contexts.variable('rule_name'),
                 contexts.variable('clause_num'),
                 contexts.variable('next_clause_num'),
                 contexts.variable('first_prem'),
                 contexts.variable('fn_head1'),
                 contexts.variable('fn_tail1'),
                 contexts.variable('decl_lines1'),
                 contexts.variable('patterns_in'),
                 contexts.variable('patterns_out1'),
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
                 contexts.variable('fn_head'),
                 pattern.pattern_literal(('POPINDENT',)),
                 contexts.variable('decl_lines'),
                 contexts.variable('patterns_in'),
                 contexts.variable('patterns_in'),),
                (),
                (contexts.variable('fn_head'),
                 contexts.variable('next_clause_num'),
                 contexts.variable('decl_lines'),))

bc_rule.bc_rule('fc_python_premise', This_rule_base, 'fc_premise',
                fc_python_premise, None,
                (contexts.variable('rule_name'),
                 contexts.variable('clause_num'),
                 contexts.variable('clause_num'),
                 contexts.variable('python_premise'),
                 contexts.variable('fn_head'),
                 contexts.variable('fn_tail'),
                 pattern.pattern_literal(()),
                 contexts.variable('patterns_in'),
                 contexts.variable('patterns_out'),),
                (),
                (contexts.variable('clause_num'),
                 contexts.variable('python_premise'),
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
                (pattern.pattern_tuple((pattern.pattern_literal('python_assertion'), pattern.pattern_tuple((contexts.variable('python_code'), contexts.anonymous(),), None), contexts.variable('start_lineno'), contexts.variable('end_lineno'),), None),
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
                 contexts.variable('bc_premises'),
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
                 contexts.anonymous(),
                 pattern.pattern_literal(()),
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
                 pattern.pattern_tuple((contexts.variable('first_prem'),), contexts.variable('rest_prems')),
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
                 contexts.variable('first_prem'),
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
                 pattern.pattern_tuple((pattern.pattern_literal('bc_premise'), contexts.variable('required'), contexts.variable('kb_name'), contexts.variable('entity_name'), contexts.variable('arg_patterns'), contexts.variable('plan_spec'), contexts.variable('start_lineno'), contexts.variable('end_lineno'),), None),
                 contexts.variable('patterns_in'),
                 contexts.variable('patterns_out'),
                 contexts.variable('plan_var_names_in'),
                 contexts.variable('plan_var_names_out'),
                 contexts.variable('plan_lines'),
                 contexts.variable('fn_head'),
                 contexts.variable('fn_tail'),),
                (),
                (contexts.variable('kb_name2'),
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
                 contexts.variable('patterns_out1'),
                 contexts.variable('patterns_out'),
                 contexts.variable('fn_head3'),
                 contexts.variable('fn_tail3'),
                 contexts.variable('plan_lines'),
                 contexts.variable('plan_vars_needed'),
                 pattern.pattern_tuple((contexts.anonymous(), contexts.variable('plan_var_names_out'),), None),
                 contexts.variable('fn_head'),
                 contexts.variable('fn_tail'),))

bc_rule.bc_rule('no_plan', This_rule_base, 'gen_plan_lines',
                no_plan, None,
                (contexts.variable('rb_name'),
                 contexts.variable('rule_name'),
                 contexts.variable('clause_num'),
                 pattern.pattern_literal(None),
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
                 pattern.pattern_tuple((pattern.pattern_literal('plan_spec'), contexts.variable('step_num'), contexts.variable('plan_var_name'), contexts.variable('python_code'), contexts.variable('plan_vars_needed'),), None),
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
                 contexts.variable('python_premise'),
                 contexts.variable('patterns_in'),
                 contexts.variable('patterns_out'),
                 contexts.variable('plan_var_names'),
                 contexts.variable('plan_var_names'),
                 pattern.pattern_literal(()),
                 contexts.variable('fn_head'),
                 contexts.variable('fn_tail'),),
                (),
                (contexts.variable('clause_num'),
                 contexts.variable('python_premise'),
                 contexts.variable('patterns_in'),
                 contexts.variable('patterns_out'),
                 contexts.variable('fn_head'),
                 contexts.variable('fn_tail'),))

bc_rule.bc_rule('python_eq', This_rule_base, 'python_premise',
                python_eq, None,
                (contexts.variable('clause_num'),
                 pattern.pattern_tuple((pattern.pattern_literal('python_eq'), contexts.variable('pattern'), pattern.pattern_tuple((contexts.variable('python_code'), contexts.anonymous(),), None), contexts.variable('start_lineno'), contexts.variable('end_lineno'),), None),
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
                 pattern.pattern_tuple((pattern.pattern_literal('python_in'), contexts.variable('pattern'), pattern.pattern_tuple((contexts.variable('python_code'), contexts.anonymous(),), None), contexts.variable('start_lineno'), contexts.variable('end_lineno'),), None),
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
                 pattern.pattern_tuple((pattern.pattern_literal('python_check'), pattern.pattern_tuple((contexts.variable('python_code'), contexts.anonymous(),), None), contexts.variable('start_lineno'), contexts.variable('end_lineno'),), None),
                 contexts.variable('patterns_in'),
                 contexts.variable('patterns_in'),
                 contexts.variable('fn_head'),
                 pattern.pattern_literal(('POPINDENT',)),),
                (),
                (contexts.variable('python_code2'),
                 contexts.variable('fn_head'),))

from pyke.compiler import helpers
Krb_filename = 'compiler.krb'
Krb_lineno_map = (
    ((12, 16), (24, 28)),
    ((19, 19), (30, 30)),
    ((23, 23), (31, 31)),
    ((26, 32), (32, 32)),
    ((34, 40), (33, 33)),
    ((42, 50), (34, 35)),
    ((53, 62), (36, 45)),
    ((66, 69), (46, 49)),
    ((73, 84), (50, 61)),
    ((111, 115), (64, 64)),
    ((118, 118), (66, 66)),
    ((131, 135), (69, 69)),
    ((138, 140), (71, 73)),
    ((153, 157), (76, 76)),
    ((167, 171), (79, 81)),
    ((173, 179), (83, 83)),
    ((181, 187), (84, 84)),
    ((201, 205), (87, 88)),
    ((207, 218), (90, 92)),
    ((220, 227), (93, 94)),
    ((230, 245), (95, 110)),
    ((249, 256), (111, 118)),
    ((275, 279), (121, 121)),
    ((289, 293), (124, 126)),
    ((295, 307), (128, 130)),
    ((309, 320), (131, 133)),
    ((323, 323), (134, 134)),
    ((340, 344), (137, 141)),
    ((347, 354), (143, 150)),
    ((358, 358), (151, 151)),
    ((362, 366), (152, 156)),
    ((383, 387), (159, 162)),
    ((388, 396), (164, 166)),
    ((406, 410), (169, 169)),
    ((420, 424), (172, 173)),
    ((426, 433), (175, 175)),
    ((435, 442), (176, 176)),
    ((456, 460), (179, 181)),
    ((463, 464), (183, 184)),
    ((468, 477), (185, 194)),
    ((492, 496), (197, 202)),
    ((506, 510), (205, 205)),
    ((520, 524), (208, 211)),
    ((526, 534), (213, 213)),
    ((536, 544), (214, 215)),
    ((547, 547), (216, 216)),
    ((564, 568), (219, 221)),
    ((570, 581), (223, 225)),
    ((584, 586), (226, 228)),
    ((590, 595), (229, 234)),
    ((599, 602), (235, 238)),
    ((621, 625), (241, 243)),
    ((627, 641), (245, 247)),
    ((644, 644), (248, 248)),
    ((648, 651), (249, 252)),
    ((655, 660), (253, 258)),
    ((679, 683), (261, 263)),
    ((693, 697), (266, 270)),
    ((699, 713), (272, 275)),
    ((716, 716), (276, 276)),
    ((719, 733), (277, 280)),
    ((736, 736), (281, 281)),
    ((740, 740), (282, 282)),
    ((744, 744), (283, 283)),
    ((767, 771), (286, 292)),
    ((774, 774), (294, 294)),
    ((778, 779), (295, 296)),
    ((783, 795), (297, 309)),
    ((798, 809), (310, 311)),
    ((811, 824), (312, 314)),
    ((827, 828), (315, 316)),
    ((832, 832), (317, 317)),
    ((836, 836), (318, 318)),
    ((863, 867), (321, 323)),
    ((870, 877), (325, 332)),
    ((890, 894), (335, 339)),
    ((897, 899), (341, 343)),
    ((902, 912), (344, 345)),
    ((926, 930), (348, 353)),
    ((933, 935), (355, 357)),
    ((938, 948), (358, 359)),
    ((962, 966), (362, 363)),
    ((969, 989), (365, 385)),
    ((993, 993), (386, 386)),
    ((1008, 1012), (389, 390)),
    ((1022, 1026), (393, 394)),
    ((1029, 1032), (396, 399)),
    ((1036, 1042), (400, 406)),
    ((1057, 1061), (409, 413)),
    ((1062, 1070), (415, 417)),
    ((1080, 1084), (420, 423)),
    ((1087, 1088), (425, 426)),
    ((1092, 1092), (427, 427)),
    ((1096, 1106), (428, 438)),
    ((1110, 1112), (439, 441)),
    ((1131, 1135), (444, 447)),
    ((1138, 1139), (449, 450)),
    ((1143, 1143), (451, 451)),
    ((1147, 1159), (452, 464)),
    ((1163, 1166), (465, 468)),
    ((1185, 1189), (471, 475)),
    ((1192, 1192), (477, 477)),
    ((1196, 1203), (478, 485)),
)
