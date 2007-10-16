# compiler_bc.py

from __future__ import with_statement, absolute_import, division
from pyke import tmp_itertools as itertools
from pyke import rule_base, contexts, pattern, bc_rule
from pyke import prove
from pyke.compiler import helpers

This_rule_base = rule_base.get_create('compiler')

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
                helpers.plan_head1(context.lookup_data('rb_name'))):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                  helpers.bc_head(context.lookup_data('rb_name'))):
            context.end_save_all_undo()
            flag_3 = False
            for x_3 in prove('compiler', 'rule_decl', context,
                           (rule.pattern(2),
                            rule.pattern(3),
                            rule.pattern(4),)):
              flag_3 = True
              assert x_3 is None, \
                "%(rule_name)s: got unexpected plan from when clause 3"
              flag_4 = False
              for x_4 in prove('compiler', 'fc_rules', context,
                             (rule.pattern(5),
                              rule.pattern(6),)):
                flag_4 = True
                assert x_4 is None, \
                  "%(rule_name)s: got unexpected plan from when clause 4"
                flag_5 = False
                for x_5 in prove('compiler', 'bc_rules', context,
                               (rule.pattern(2),
                                rule.pattern(7),
                                rule.pattern(8),
                                rule.pattern(9),)):
                  flag_5 = True
                  assert x_5 is None, \
                    "%(rule_name)s: got unexpected plan from when clause 5"
                  mark6 = context.mark(True)
                  if rule.pattern(10).match_data(context, context,
                          (context.lookup_data('lines1') + (context.lookup_data('decl_line'),) + context.lookup_data('fc_funs_lines')) \
                                                 if context.lookup_data('fc_funs_lines') \
                                                 else ()):
                    context.end_save_all_undo()
                    mark7 = context.mark(True)
                    if rule.pattern(11).match_data(context, context,
                            context.lookup_data('bc_plan_lines')):
                      context.end_save_all_undo()
                      mark8 = context.mark(True)
                      if rule.pattern(12).match_data(context, context,
                              (context.lookup_data('bc_head') + (("import %s_plans" % context.lookup_data('rb_name'), "") 
                             if context.lookup_data('bc_plan_lines')
                             else ("",)) + 
                             (context.lookup_data('decl_line'),) + context.lookup_data('bc_bc_lines')) \
                                                     if context.lookup_data('bc_bc_lines') \
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

bc_rule.bc_rule('file', This_rule_base, 'compile',
                file, None,
                (contexts.variable('rb_name'),
                 pattern.pattern_tuple((pattern.pattern_literal('file'), contexts.variable('parent'), contexts.variable('fc_rules'), contexts.variable('bc_rules'),), None),
                 contexts.variable('fc_lines'),
                 contexts.variable('bc_lines'),
                 contexts.variable('plan_lines'),),
                (),
                (contexts.variable('lines1'),
                 contexts.variable('bc_head'),
                 contexts.variable('rb_name'),
                 contexts.variable('parent'),
                 contexts.variable('decl_line'),
                 contexts.variable('fc_rules'),
                 contexts.variable('fc_funs_lines'),
                 contexts.variable('bc_rules'),
                 contexts.variable('bc_plan_lines'),
                 contexts.variable('bc_bc_lines'),
                 contexts.variable('fc_lines'),
                 contexts.variable('plan_lines'),
                 contexts.variable('bc_lines'),))

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

bc_rule.bc_rule('rule_decl', This_rule_base, 'rule_decl',
                rule_decl, None,
                (contexts.variable('rb_name'),
                 pattern.pattern_literal(None),
                 contexts.variable('decl_line'),),
                (),
                (contexts.variable('decl_line'),))

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

bc_rule.bc_rule('rule_decl_with_parent', This_rule_base, 'rule_decl',
                rule_decl_with_parent, None,
                (contexts.variable('rb_name'),
                 pattern.pattern_tuple((pattern.pattern_literal('parent'), contexts.variable('parent'), contexts.variable('excluded_symbols'),), None),
                 contexts.variable('decl_line'),),
                (),
                (contexts.variable('decl_line'),))

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

bc_rule.bc_rule('fc_rules0', This_rule_base, 'fc_rules',
                fc_rules0, None,
                (pattern.pattern_literal(()),
                 pattern.pattern_literal(()),),
                (),
                ())

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
        for x_1 in prove('compiler', 'fc_rule', context,
                       (rule.pattern(0),
                        rule.pattern(1),)):
          flag_1 = True
          assert x_1 is None, \
            "%(rule_name)s: got unexpected plan from when clause 1"
          flag_2 = False
          for x_2 in prove('compiler', 'fc_rules', context,
                         (rule.pattern(2),
                          rule.pattern(3),)):
            flag_2 = True
            assert x_2 is None, \
              "%(rule_name)s: got unexpected plan from when clause 2"
            mark3 = context.mark(True)
            if rule.pattern(4).match_data(context, context,
                    context.lookup_data('fc_lines') + context.lookup_data('lines_rest')):
              context.end_save_all_undo()
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          if not flag_2:
            raise AssertionError("compiler.fc_rules1: 'when' clause 2 failed")
        if not flag_1:
          raise AssertionError("compiler.fc_rules1: 'when' clause 1 failed")
    finally:
      context.done()

bc_rule.bc_rule('fc_rules1', This_rule_base, 'fc_rules',
                fc_rules1, None,
                (pattern.pattern_tuple((contexts.variable('fc_rule'),), contexts.variable('fc_rest')),
                 contexts.variable('lines'),),
                (),
                (contexts.variable('fc_rule'),
                 contexts.variable('fc_lines'),
                 contexts.variable('fc_rest'),
                 contexts.variable('lines_rest'),
                 contexts.variable('lines'),))

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
        for x_1 in prove('compiler', 'fc_predicates', context,
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
            "%(rule_name)s: got unexpected plan from when clause 1"
          flag_2 = False
          for x_2 in prove('compiler', 'assertions', context,
                         (rule.pattern(8),
                          rule.pattern(9),
                          rule.pattern(7),
                          rule.pattern(10),)):
            flag_2 = True
            assert x_2 is None, \
              "%(rule_name)s: got unexpected plan from when clause 2"
            mark3 = context.mark(True)
            if rule.pattern(11).match_data(context, context,
                    helpers.splice(
                   "",
                   "def %s(rule, context = None, index = None):" %
                   context.lookup_data('rule_name'),
                   (("INDENT", 2),),
                   "if context is None: context = contexts.simple_context()",
                   "try:",
                   (("INDENT", 2),),
                   context.lookup_data('pred_fn_head'),
                   context.lookup_data('asserts_fn_lines'),
                   context.lookup_data('pred_fn_tail'),
                   "POPINDENT",
                   "finally:",
                   (("INDENT", 2),),
                   "context.done()",
                   "POPINDENT",
                   "POPINDENT",
                   "",
                   "fc_rule.fc_rule('%(name)s', This_rule_base, %(name)s," %
                   {'name': context.lookup_data('rule_name')},
                   (("INDENT", 2),),
                   helpers.add_brackets(context.lookup_data('pred_decl_lines'), '(', '),'),
                   helpers.list_format(context.lookup_data('patterns_out'), '(', '))'),
                   'POPINDENT')):
              context.end_save_all_undo()
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          if not flag_2:
            raise AssertionError("compiler.fc_rule_: 'when' clause 2 failed")
        if not flag_1:
          raise AssertionError("compiler.fc_rule_: 'when' clause 1 failed")
    finally:
      context.done()

bc_rule.bc_rule('fc_rule_', This_rule_base, 'fc_rule',
                fc_rule_, None,
                (pattern.pattern_tuple((pattern.pattern_literal('fc_rule'), contexts.variable('rule_name'), contexts.variable('fc_predicates'), contexts.variable('assertions'),), None),
                 contexts.variable('fc_lines'),),
                (),
                (contexts.variable('rule_name'),
                 pattern.pattern_literal(0),
                 contexts.variable('fc_predicates'),
                 contexts.variable('pred_fn_head'),
                 contexts.variable('pred_fn_tail'),
                 contexts.variable('pred_decl_lines'),
                 pattern.pattern_literal(()),
                 contexts.variable('patterns_out1'),
                 contexts.variable('assertions'),
                 contexts.variable('asserts_fn_lines'),
                 contexts.variable('patterns_out'),
                 contexts.variable('fc_lines'),))

def fc_predicates0(rule, arg_patterns, arg_context):
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

bc_rule.bc_rule('fc_predicates0', This_rule_base, 'fc_predicates',
                fc_predicates0, None,
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

def fc_predicates1(rule, arg_patterns, arg_context):
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
        for x_1 in prove('compiler', 'fc_predicate', context,
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
            "%(rule_name)s: got unexpected plan from when clause 1"
          flag_2 = False
          for x_2 in prove('compiler', 'fc_predicates', context,
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
              "%(rule_name)s: got unexpected plan from when clause 2"
            mark3 = context.mark(True)
            if rule.pattern(14).match_data(context, context,
                    helpers.splice(context.lookup_data('fn_head1'), context.lookup_data('fn_head2'))):
              context.end_save_all_undo()
              mark4 = context.mark(True)
              if rule.pattern(15).match_data(context, context,
                      helpers.splice(context.lookup_data('fn_tail2'), context.lookup_data('fn_tail1'))):
                context.end_save_all_undo()
                mark5 = context.mark(True)
                if rule.pattern(16).match_data(context, context,
                        helpers.splice(context.lookup_data('decl_lines1'), context.lookup_data('decl_lines2'))):
                  context.end_save_all_undo()
                  yield
                else: context.end_save_all_undo()
                context.undo_to_mark(mark5)
              else: context.end_save_all_undo()
              context.undo_to_mark(mark4)
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          if not flag_2:
            raise AssertionError("compiler.fc_predicates1: 'when' clause 2 failed")
        if not flag_1:
          raise AssertionError("compiler.fc_predicates1: 'when' clause 1 failed")
    finally:
      context.done()

bc_rule.bc_rule('fc_predicates1', This_rule_base, 'fc_predicates',
                fc_predicates1, None,
                (contexts.variable('rule_name'),
                 contexts.variable('clause_num'),
                 pattern.pattern_tuple((contexts.variable('first_pred'),), contexts.variable('rest_preds')),
                 contexts.variable('fn_head'),
                 contexts.variable('fn_tail'),
                 contexts.variable('decl_lines'),
                 contexts.variable('patterns_in'),
                 contexts.variable('patterns_out'),),
                (),
                (contexts.variable('rule_name'),
                 contexts.variable('clause_num'),
                 contexts.variable('next_clause_num'),
                 contexts.variable('first_pred'),
                 contexts.variable('fn_head1'),
                 contexts.variable('fn_tail1'),
                 contexts.variable('decl_lines1'),
                 contexts.variable('patterns_in'),
                 contexts.variable('patterns_out1'),
                 contexts.variable('rest_preds'),
                 contexts.variable('fn_head2'),
                 contexts.variable('fn_tail2'),
                 contexts.variable('decl_lines2'),
                 contexts.variable('patterns_out'),
                 contexts.variable('fn_head'),
                 contexts.variable('fn_tail'),
                 contexts.variable('decl_lines'),))

def fc_predicate(rule, arg_patterns, arg_context):
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
               "lookup('%s', '%s', context, rule.foreach_patterns(%d)):" %
               (context.lookup_data('kb_name'), context.lookup_data('entity_name'), context.lookup_data('clause_num')),
               'POPINDENT',)):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                  context.lookup_data('clause_num') + 1):
            context.end_save_all_undo()
            mark3 = context.mark(True)
            if rule.pattern(2).match_data(context, context,
                    helpers.splice("('%s', '%s'," % (context.lookup_data('kb_name'), context.lookup_data('entity_name')),
                   (('INDENT', 1),),
                   helpers.list_format(context.lookup_data('arg_patterns'),
                   '(', ')),'),
                   'POPINDENT')):
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

bc_rule.bc_rule('fc_predicate', This_rule_base, 'fc_predicate',
                fc_predicate, None,
                (contexts.variable('rule_name'),
                 contexts.variable('clause_num'),
                 contexts.variable('next_clause_num'),
                 pattern.pattern_tuple((pattern.pattern_literal('fc_predicate'), contexts.variable('kb_name'), contexts.variable('entity_name'), contexts.variable('arg_patterns'),), None),
                 contexts.variable('fn_head'),
                 pattern.pattern_literal(('POPINDENT',)),
                 contexts.variable('decl_lines'),
                 contexts.variable('patterns_in'),
                 contexts.variable('patterns_in'),),
                (),
                (contexts.variable('fn_head'),
                 contexts.variable('next_clause_num'),
                 contexts.variable('decl_lines'),))

def fc_python_predicate(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        for x_1 in prove('compiler', 'python_predicate', context,
                       (rule.pattern(0),
                        rule.pattern(1),
                        rule.pattern(2),
                        rule.pattern(3),
                        rule.pattern(4),
                        rule.pattern(5),)):
          assert x_1 is None, \
            "%(rule_name)s: got unexpected plan from when clause 1"
          yield
    finally:
      context.done()

bc_rule.bc_rule('fc_python_predicate', This_rule_base, 'fc_predicate',
                fc_python_predicate, None,
                (contexts.variable('rule_name'),
                 contexts.variable('clause_num'),
                 contexts.variable('clause_num'),
                 contexts.variable('python_predicate'),
                 contexts.variable('fn_head'),
                 contexts.variable('fn_tail'),
                 pattern.pattern_literal(()),
                 contexts.variable('patterns_in'),
                 contexts.variable('patterns_out'),),
                (),
                (contexts.variable('clause_num'),
                 contexts.variable('python_predicate'),
                 contexts.variable('patterns_in'),
                 contexts.variable('patterns_out'),
                 contexts.variable('fn_head'),
                 contexts.variable('fn_tail'),))

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

bc_rule.bc_rule('assertions_0', This_rule_base, 'assertions',
                assertions_0, None,
                (pattern.pattern_literal(()),
                 pattern.pattern_literal(()),
                 contexts.variable('patterns_in'),
                 contexts.variable('patterns_in'),),
                (),
                ())

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
        for x_1 in prove('compiler', 'assertion', context,
                       (rule.pattern(0),
                        rule.pattern(1),
                        rule.pattern(2),
                        rule.pattern(3),)):
          flag_1 = True
          assert x_1 is None, \
            "%(rule_name)s: got unexpected plan from when clause 1"
          flag_2 = False
          for x_2 in prove('compiler', 'assertions', context,
                         (rule.pattern(4),
                          rule.pattern(5),
                          rule.pattern(3),
                          rule.pattern(6),)):
            flag_2 = True
            assert x_2 is None, \
              "%(rule_name)s: got unexpected plan from when clause 2"
            mark3 = context.mark(True)
            if rule.pattern(7).match_data(context, context,
                    helpers.splice(context.lookup_data('fn_lines1'), context.lookup_data('fn_lines2'))):
              context.end_save_all_undo()
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          if not flag_2:
            raise AssertionError("compiler.assertions_n: 'when' clause 2 failed")
        if not flag_1:
          raise AssertionError("compiler.assertions_n: 'when' clause 1 failed")
    finally:
      context.done()

bc_rule.bc_rule('assertions_n', This_rule_base, 'assertions',
                assertions_n, None,
                (pattern.pattern_tuple((contexts.variable('first_assertion'),), contexts.variable('rest_assertions')),
                 contexts.variable('fn_lines'),
                 contexts.variable('patterns_in'),
                 contexts.variable('patterns_out'),),
                (),
                (contexts.variable('first_assertion'),
                 contexts.variable('fn_lines1'),
                 contexts.variable('patterns_in'),
                 contexts.variable('patterns_out1'),
                 contexts.variable('rest_assertions'),
                 contexts.variable('fn_lines2'),
                 contexts.variable('patterns_out'),
                 contexts.variable('fn_lines'),))

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
                  helpers.splice(
                 "assert_('%s', '%s'," % (context.lookup_data('kb_name'), context.lookup_data('entity_name')),
                 (('INDENT', 8),),
                 helpers.list_format(
                 ("rule.pattern(%d).as_data(context)" % pat_num
                 for pat_num in context.lookup_data('pat_nums')),
                 '(', '))'),
                 'POPINDENT')):
            context.end_save_all_undo()
            yield
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
    finally:
      context.done()

bc_rule.bc_rule('assertion', This_rule_base, 'assertion',
                assertion, None,
                (pattern.pattern_tuple((pattern.pattern_literal('assert'), contexts.variable('kb_name'), contexts.variable('entity_name'), contexts.variable('patterns'),), None),
                 contexts.variable('fn_lines'),
                 contexts.variable('patterns_in'),
                 contexts.variable('patterns_out'),),
                (),
                (pattern.pattern_tuple((contexts.variable('pat_nums'), contexts.variable('patterns_out'),), None),
                 contexts.variable('fn_lines'),))

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

bc_rule.bc_rule('python_assertion', This_rule_base, 'assertion',
                python_assertion, None,
                (pattern.pattern_tuple((pattern.pattern_literal('python_assertion'), pattern.pattern_tuple((contexts.variable('python_code'), contexts.anonymous(),), None),), None),
                 contexts.variable('python_code'),
                 contexts.variable('patterns_in'),
                 contexts.variable('patterns_in'),),
                (),
                ())

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

bc_rule.bc_rule('bc_rules0', This_rule_base, 'bc_rules',
                bc_rules0, None,
                (contexts.anonymous(),
                 pattern.pattern_literal(()),
                 pattern.pattern_literal(()),
                 pattern.pattern_literal(()),),
                (),
                ())

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
        for x_1 in prove('compiler', 'bc_rule', context,
                       (rule.pattern(0),
                        rule.pattern(1),
                        rule.pattern(2),
                        rule.pattern(3),)):
          flag_1 = True
          assert x_1 is None, \
            "%(rule_name)s: got unexpected plan from when clause 1"
          flag_2 = False
          for x_2 in prove('compiler', 'bc_rules', context,
                         (rule.pattern(0),
                          rule.pattern(4),
                          rule.pattern(5),
                          rule.pattern(6),)):
            flag_2 = True
            assert x_2 is None, \
              "%(rule_name)s: got unexpected plan from when clause 2"
            mark3 = context.mark(True)
            if rule.pattern(7).match_data(context, context,
                    context.lookup_data('bc_plan_lines') + context.lookup_data('plan_lines_rest')):
              context.end_save_all_undo()
              mark4 = context.mark(True)
              if rule.pattern(8).match_data(context, context,
                      context.lookup_data('bc_bc_lines') + context.lookup_data('bc_lines_rest')):
                context.end_save_all_undo()
                yield
              else: context.end_save_all_undo()
              context.undo_to_mark(mark4)
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          if not flag_2:
            raise AssertionError("compiler.bc_rules1: 'when' clause 2 failed")
        if not flag_1:
          raise AssertionError("compiler.bc_rules1: 'when' clause 1 failed")
    finally:
      context.done()

bc_rule.bc_rule('bc_rules1', This_rule_base, 'bc_rules',
                bc_rules1, None,
                (contexts.variable('rb_name'),
                 pattern.pattern_tuple((contexts.variable('bc_rule'),), contexts.variable('bc_rest')),
                 contexts.variable('plan_lines'),
                 contexts.variable('bc_lines'),),
                (),
                (contexts.variable('rb_name'),
                 contexts.variable('bc_rule'),
                 contexts.variable('bc_plan_lines'),
                 contexts.variable('bc_bc_lines'),
                 contexts.variable('bc_rest'),
                 contexts.variable('plan_lines_rest'),
                 contexts.variable('bc_lines_rest'),
                 contexts.variable('plan_lines'),
                 contexts.variable('bc_lines'),))

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
        for x_1 in prove('compiler', 'bc_predicates', context,
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
            "%(rule_name)s: got unexpected plan from when clause 1"
          mark2 = context.mark(True)
          if rule.pattern(8).match_data(context, context,
                  \
                             helpers.goal(context.lookup_data('rb_name'), context.lookup_data('name'), context.lookup_data('goal'),
                 context.lookup_data('pred_plan_lines'), context.lookup_data('python_lines'))):
            context.end_save_all_undo()
            mark3 = context.mark(True)
            if rule.pattern(9).match_data(context, context,
                    helpers.splice(
                   context.lookup_data('goal_fn_head'),
                   context.lookup_data('pred_fn_head'),
                   'yield context' if context.lookup_data('plan_lines') else 'yield',
                   context.lookup_data('pred_fn_tail'),
                   context.lookup_data('goal_fn_tail'),
                   context.lookup_data('goal_decl_lines'),
                   context.lookup_data('pred_decl_lines'),
                   'POPINDENT')):
              context.end_save_all_undo()
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        if not flag_1:
          raise AssertionError("compiler.bc_rule_: 'when' clause 1 failed")
    finally:
      context.done()

bc_rule.bc_rule('bc_rule_', This_rule_base, 'bc_rule',
                bc_rule_, None,
                (contexts.variable('rb_name'),
                 pattern.pattern_tuple((pattern.pattern_literal('bc_rule'), contexts.variable('name'), contexts.variable('goal'), contexts.variable('bc_predicates'), contexts.variable('python_lines'), contexts.variable('plan_vars_needed'),), None),
                 contexts.variable('plan_lines'),
                 contexts.variable('bc_lines'),),
                (),
                (contexts.variable('rb_name'),
                 contexts.variable('name'),
                 contexts.variable('bc_predicates'),
                 contexts.variable('plan_vars_needed'),
                 contexts.variable('pred_plan_lines'),
                 contexts.variable('pred_fn_head'),
                 contexts.variable('pred_fn_tail'),
                 contexts.variable('pred_decl_lines'),
                 pattern.pattern_tuple((contexts.variable('plan_lines'), contexts.variable('goal_fn_head'), contexts.variable('goal_fn_tail'), contexts.variable('goal_decl_lines'),), None),
                 contexts.variable('bc_lines'),))

def bc_predicates(rule, arg_patterns, arg_context):
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
        for x_1 in prove('compiler', 'bc_predicates1', context,
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
            "%(rule_name)s: got unexpected plan from when clause 1"
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
          raise AssertionError("compiler.bc_predicates: 'when' clause 1 failed")
    finally:
      context.done()

bc_rule.bc_rule('bc_predicates', This_rule_base, 'bc_predicates',
                bc_predicates, None,
                (contexts.variable('rb_name'),
                 contexts.variable('rule_name'),
                 contexts.variable('bc_predicates'),
                 contexts.variable('plan_vars_needed'),
                 contexts.variable('plan_lines'),
                 contexts.variable('fn_head'),
                 contexts.variable('fn_tail'),
                 contexts.variable('decl_lines'),),
                (),
                (contexts.variable('rb_name'),
                 contexts.variable('rule_name'),
                 pattern.pattern_literal(1),
                 contexts.variable('bc_predicates'),
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

def bc_predicates1_0(rule, arg_patterns, arg_context):
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

bc_rule.bc_rule('bc_predicates1_0', This_rule_base, 'bc_predicates1',
                bc_predicates1_0, None,
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

def bc_predicates1_n(rule, arg_patterns, arg_context):
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
        for x_1 in prove('compiler', 'bc_predicate', context,
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
            "%(rule_name)s: got unexpected plan from when clause 1"
          mark2 = context.mark(True)
          if rule.pattern(11).match_data(context, context,
                  context.lookup_data('clause_num') + 1):
            context.end_save_all_undo()
            flag_3 = False
            for x_3 in prove('compiler', 'bc_predicates1', context,
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
                "%(rule_name)s: got unexpected plan from when clause 3"
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
              raise AssertionError("compiler.bc_predicates1_n: 'when' clause 3 failed")
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        if not flag_1:
          raise AssertionError("compiler.bc_predicates1_n: 'when' clause 1 failed")
    finally:
      context.done()

bc_rule.bc_rule('bc_predicates1_n', This_rule_base, 'bc_predicates1',
                bc_predicates1_n, None,
                (contexts.variable('rb_name'),
                 contexts.variable('rule_name'),
                 contexts.variable('clause_num'),
                 pattern.pattern_tuple((contexts.variable('first_pred'),), contexts.variable('rest_preds')),
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
                 contexts.variable('first_pred'),
                 contexts.variable('patterns_in'),
                 contexts.variable('patterns_out1'),
                 contexts.variable('plan_var_names_in'),
                 contexts.variable('plan_var_names_out1'),
                 contexts.variable('plan_lines1'),
                 contexts.variable('fn_head1'),
                 contexts.variable('fn_tail1'),
                 contexts.variable('next_clause_num'),
                 contexts.variable('rest_preds'),
                 contexts.variable('patterns_out'),
                 contexts.variable('plan_var_names_out'),
                 contexts.variable('plan_lines2'),
                 contexts.variable('fn_head2'),
                 contexts.variable('fn_tail2'),
                 contexts.variable('plan_lines'),
                 contexts.variable('fn_head'),
                 contexts.variable('fn_tail'),))

def bc_predicate(rule, arg_patterns, arg_context):
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
                context.lookup_data('kb_name') or "'" + context.lookup_data('rb_name') + "'"):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                  \
                             helpers.merge_patterns(context.lookup_data('arg_patterns'), context.lookup_data('patterns_in'))):
            context.end_save_all_undo()
            mark3 = context.mark(True)
            if rule.pattern(2).match_data(context, context,
                    helpers.splice(
                   "for x_%(clause_num)d in "
                   "prove(%(kb_name)s, %(entity_name)s, context," %
                   {'clause_num': context.lookup_data('clause_num'),
                   'kb_name': context.lookup_data('kb_name2'),
                   'entity_name': context.lookup_data('entity_name')},
                   (('INDENT', 2),
                   ('INDENT', 13),),
                   helpers.list_format(('rule.pattern(%d)' % pat_num
                   for pat_num in context.lookup_data('pat_nums')),
                   '(', ')):'),
                   'POPINDENT',)):
              context.end_save_all_undo()
              flag_4 = False
              for x_4 in prove('compiler', 'add_required', context,
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
                  "%(rule_name)s: got unexpected plan from when clause 4"
                flag_5 = False
                for x_5 in prove('compiler', 'gen_plan_lines', context,
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
                    "%(rule_name)s: got unexpected plan from when clause 5"
                  mark6 = context.mark(True)
                  if rule.pattern(17).match_data(context, context,
                          helpers.merge_patterns(context.lookup_data('plan_vars_needed'),
                         context.lookup_data('plan_var_names_in'))):
                    context.end_save_all_undo()
                    mark7 = context.mark(True)
                    if rule.pattern(18).match_data(context, context,
                            context.lookup_data('fn_head2') + context.lookup_data('fn_head3')):
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
                  raise AssertionError("compiler.bc_predicate: 'when' clause 5 failed")
              if not flag_4:
                raise AssertionError("compiler.bc_predicate: 'when' clause 4 failed")
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
    finally:
      context.done()

bc_rule.bc_rule('bc_predicate', This_rule_base, 'bc_predicate',
                bc_predicate, None,
                (contexts.variable('rb_name'),
                 contexts.variable('rule_name'),
                 contexts.variable('clause_num'),
                 pattern.pattern_tuple((pattern.pattern_literal('bc_predicate'), contexts.variable('required'), contexts.variable('kb_name'), contexts.variable('entity_name'), contexts.variable('arg_patterns'), contexts.variable('plan_spec'),), None),
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
               '"%(rb_name).%(rule_name)s: got unexpected plan from '
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
          for x_2 in prove('compiler', 'plan_bindings', context,
                         (rule.pattern(1),
                          rule.pattern(2),
                          rule.pattern(3),
                          rule.pattern(4),
                          rule.pattern(5),
                          rule.pattern(6),
                          rule.pattern(7),)):
            flag_2 = True
            assert x_2 is None, \
              "%(rule_name)s: got unexpected plan from when clause 2"
            yield
          if not flag_2:
            raise AssertionError("compiler.as_plan: 'when' clause 2 failed")
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
    finally:
      context.done()

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
          for x_2 in prove('compiler', 'plan_bindings', context,
                         (rule.pattern(1),
                          rule.pattern(2),
                          rule.pattern(3),
                          rule.pattern(4),
                          rule.pattern(5),
                          rule.pattern(6),
                          rule.pattern(7),)):
            flag_2 = True
            assert x_2 is None, \
              "%(rule_name)s: got unexpected plan from when clause 2"
            yield
          if not flag_2:
            raise AssertionError("compiler.plan_spec: 'when' clause 2 failed")
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
    finally:
      context.done()

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
               '"%(rb_name).%(rule_name)s: expected plan from '
               'when clause %(clause_num)d"' %
               {'clause_num': context.lookup_data('clause_num'),
               'rb_name': context.lookup_data('rb_name'),
               'rule_name': context.lookup_data('rule_name')},
               'POPINDENT',
               "mark%d = context.mark(True)" % context.lookup_data('clause_num'),
               "if not rule.pattern(%d).match_data(context, context, "
               "x_%d):" % (context.lookup_data('pat_num'), context.lookup_data('clause_num')),
               ('INDENT', 2),
               'raise AssertionError("%(rb_name).%(rule_name)s: '
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
                helpers.splice(
               "flag_%d = False" % context.lookup_data('clause_num'),
               context.lookup_data('fn_head1'),
               "flag_%d = True" % context.lookup_data('clause_num'),)):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                  helpers.splice(
                 context.lookup_data('fn_tail1'),
                 "if not flag_%d:" % context.lookup_data('clause_num'),
                 (("INDENT", 2),),
                 "raise AssertionError(\"%s.%s: 'when' clause %d failed\")"
                 % (context.lookup_data('rb_name'), context.lookup_data('rule_name'), context.lookup_data('clause_num')),
                 "POPINDENT")):
            context.end_save_all_undo()
            yield
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
    finally:
      context.done()

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

def bc_python_predicate(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(itertools.imap(lambda pat, arg:
                              pat.match_pattern(context, context,
                                                arg, arg_context),
                            patterns,
                            arg_patterns)):
        for x_1 in prove('compiler', 'python_predicate', context,
                       (rule.pattern(0),
                        rule.pattern(1),
                        rule.pattern(2),
                        rule.pattern(3),
                        rule.pattern(4),
                        rule.pattern(5),)):
          assert x_1 is None, \
            "%(rule_name)s: got unexpected plan from when clause 1"
          yield
    finally:
      context.done()

bc_rule.bc_rule('bc_python_predicate', This_rule_base, 'bc_predicate',
                bc_python_predicate, None,
                (contexts.variable('rb_name'),
                 contexts.variable('rule_name'),
                 contexts.variable('clause_num'),
                 contexts.variable('python_predicate'),
                 contexts.variable('patterns_in'),
                 contexts.variable('patterns_out'),
                 contexts.variable('plan_var_names'),
                 contexts.variable('plan_var_names'),
                 pattern.pattern_literal(()),
                 contexts.variable('fn_head'),
                 contexts.variable('fn_tail'),),
                (),
                (contexts.variable('clause_num'),
                 contexts.variable('python_predicate'),
                 contexts.variable('patterns_in'),
                 contexts.variable('patterns_out'),
                 contexts.variable('fn_head'),
                 contexts.variable('fn_tail'),))

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
                    helpers.splice(
                   "mark%d = context.mark(True)" % context.lookup_data('clause_num'),
                   "if rule.pattern(%d).match_data(context, context," %
                   context.lookup_data('pat_num'),
                   (('INDENT', 2),
                   ('INDENT', 5),),
                   context.lookup_data('python_code2'),
                   'POPINDENT',
                   "context.end_save_all_undo()")):
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

bc_rule.bc_rule('python_eq', This_rule_base, 'python_predicate',
                python_eq, None,
                (contexts.variable('clause_num'),
                 pattern.pattern_tuple((pattern.pattern_literal('python_eq'), contexts.variable('pattern'), pattern.pattern_tuple((contexts.variable('python_code'), contexts.anonymous(),), None),), None),
                 contexts.variable('patterns_in'),
                 contexts.variable('patterns_out'),
                 contexts.variable('fn_head'),
                 contexts.variable('fn_tail'),),
                (),
                (pattern.pattern_tuple((contexts.variable('pat_num'), contexts.variable('patterns_out'),), None),
                 contexts.variable('python_code2'),
                 contexts.variable('fn_head'),
                 contexts.variable('fn_tail'),))

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
                    helpers.splice(
                   "for python_ans in \\",
                   (('INDENT', 2),
                   ('INDENT', 2),),
                   context.lookup_data('python_code2'),
                   'POPINDENT',
                   "mark%d = context.mark(True)" % context.lookup_data('clause_num'),
                   "if rule.pattern(%d).match_data(context, context, "
                   "python_ans):" % context.lookup_data('pat_num'),
                   (('INDENT', 2),),
                   "context.end_save_all_undo()")):
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

bc_rule.bc_rule('python_in', This_rule_base, 'python_predicate',
                python_in, None,
                (contexts.variable('clause_num'),
                 pattern.pattern_tuple((pattern.pattern_literal('python_in'), contexts.variable('pattern'), pattern.pattern_tuple((contexts.variable('python_code'), contexts.anonymous(),), None),), None),
                 contexts.variable('patterns_in'),
                 contexts.variable('patterns_out'),
                 contexts.variable('fn_head'),
                 contexts.variable('fn_tail'),),
                (),
                (pattern.pattern_tuple((contexts.variable('pat_num'), contexts.variable('patterns_out'),), None),
                 contexts.variable('python_code2'),
                 contexts.variable('fn_head'),
                 contexts.variable('fn_tail'),))

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
                  helpers.splice(
                 "if " + context.lookup_data('python_code2')[0].strip(),
                 context.lookup_data('python_code2')[1:],
                 (('INDENT', 2),),)):
            context.end_save_all_undo()
            yield
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
    finally:
      context.done()

bc_rule.bc_rule('python_check', This_rule_base, 'python_predicate',
                python_check, None,
                (contexts.variable('clause_num'),
                 pattern.pattern_tuple((pattern.pattern_literal('python_check'), pattern.pattern_tuple((contexts.variable('python_code'), contexts.anonymous(),), None),), None),
                 contexts.variable('patterns_in'),
                 contexts.variable('patterns_in'),
                 contexts.variable('fn_head'),
                 pattern.pattern_literal(('POPINDENT',)),),
                (),
                (contexts.variable('python_code2'),
                 contexts.variable('fn_head'),))
