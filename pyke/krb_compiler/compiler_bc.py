# compiler_bc.py

import itertools
from pyke import contexts, pattern, bc_rule

version = '0.4'

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
              gen_4 = engine.prove(rule.rule_base.root_name, 'rule_decl', context,
                                      (rule.pattern(3),
                                       rule.pattern(4),
                                       rule.pattern(5),))
              for x_4 in gen_4: 
                flag_4 = True
                assert x_4 is None, \
                  "compiler.file: got unexpected plan from when clause 4"
                flag_5 = False
                gen_5 = engine.prove(rule.rule_base.root_name, 'fc_rules', context,
                                        (rule.pattern(6),
                                         rule.pattern(7),
                                         rule.pattern(8),))
                for x_5 in gen_5: 
                  flag_5 = True
                  assert x_5 is None, \
                    "compiler.file: got unexpected plan from when clause 5"
                  flag_6 = False
                  gen_6 = engine.prove(rule.rule_base.root_name, 'bc_rules', context,
                                          (rule.pattern(3),
                                           rule.pattern(9),
                                           rule.pattern(10),
                                           rule.pattern(11),
                                           rule.pattern(12),))
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
                        context.undo_to_mark(mark9)
                      else: context.end_save_all_undo()
                      context.undo_to_mark(mark8)
                    else: context.end_save_all_undo()
                    context.undo_to_mark(mark7)
                  if not flag_6:
                    raise AssertionError("compiler.file: 'when' clause 6 failed")
                  if hasattr(gen_6, 'iterator'): 
                    if not gen_6.iterator == None: 
                      gen_6.iterator.close()
                  else: 
                    if hasattr(gen_6, '__iter__'): 
                      if not gen_6.__iter__ == None: 
                        gen_6.close()
                if not flag_5:
                  raise AssertionError("compiler.file: 'when' clause 5 failed")
                if hasattr(gen_5, 'iterator'): 
                  if not gen_5.iterator == None: 
                    gen_5.iterator.close()
                else: 
                  if hasattr(gen_5, '__iter__'): 
                    if not gen_5.__iter__ == None: 
                      gen_5.close()
              if not flag_4:
                raise AssertionError("compiler.file: 'when' clause 4 failed")
              if hasattr(gen_4, 'iterator'): 
                if not gen_4.iterator == None: 
                  gen_4.iterator.close()
              else: 
                if hasattr(gen_4, '__iter__'): 
                  if not gen_4.__iter__ == None: 
                    gen_4.close()
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
        gen_1 = engine.prove(rule.rule_base.root_name, 'fc_rule', context,
                                (rule.pattern(0),
                                 rule.pattern(1),
                                 rule.pattern(2),))
        for x_1 in gen_1: 
          flag_1 = True
          assert x_1 is None, \
            "compiler.fc_rules1: got unexpected plan from when clause 1"
          flag_2 = False
          gen_2 = engine.prove(rule.rule_base.root_name, 'fc_rules', context,
                                  (rule.pattern(3),
                                   rule.pattern(4),
                                   rule.pattern(5),))
          for x_2 in gen_2: 
            flag_2 = True
            assert x_2 is None, \
              "compiler.fc_rules1: got unexpected plan from when clause 2"
            rule.rule_base.num_bc_rule_successes += 1
            yield
          if not flag_2:
            raise AssertionError("compiler.fc_rules1: 'when' clause 2 failed")
          if hasattr(gen_2, 'iterator'): 
            if not gen_2.iterator == None: 
              gen_2.iterator.close()
          else: 
            if hasattr(gen_2, '__iter__'): 
              if not gen_2.__iter__ == None: 
                gen_2.close()
        if not flag_1:
          raise AssertionError("compiler.fc_rules1: 'when' clause 1 failed")
        if hasattr(gen_1, 'iterator'): 
          if not gen_1.iterator == None: 
            gen_1.iterator.close()
        else: 
          if hasattr(gen_1, '__iter__'): 
            if not gen_1.__iter__ == None: 
              gen_1.close()
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
        gen_1 = engine.prove(rule.rule_base.root_name, 'fc_premises', context,
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
                                 rule.pattern(10),))
        for x_1 in gen_1: 
          flag_1 = True
          assert x_1 is None, \
            "compiler.fc_rule_: got unexpected plan from when clause 1"
          flag_2 = False
          gen_2 = engine.prove(rule.rule_base.root_name, 'assertions', context,
                                  (rule.pattern(11),
                                   rule.pattern(12),
                                   rule.pattern(10),
                                   rule.pattern(13),))
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
          if hasattr(gen_2, 'iterator'): 
            if not gen_2.iterator == None: 
              gen_2.iterator.close()
          else: 
            if hasattr(gen_2, '__iter__'): 
              if not gen_2.__iter__ == None: 
                gen_2.close()
        if not flag_1:
          raise AssertionError("compiler.fc_rule_: 'when' clause 1 failed")
        if hasattr(gen_1, 'iterator'): 
          if not gen_1.iterator == None: 
            gen_1.iterator.close()
        else: 
          if hasattr(gen_1, '__iter__'): 
            if not gen_1.__iter__ == None: 
              gen_1.close()
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
        gen_1 = engine.prove(rule.rule_base.root_name, 'fc_premise', context,
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
                                 rule.pattern(10),))
        for x_1 in gen_1: 
          flag_1 = True
          assert x_1 is None, \
            "compiler.fc_premises1: got unexpected plan from when clause 1"
          flag_2 = False
          gen_2 = engine.prove(rule.rule_base.root_name, 'fc_premises', context,
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
                                   rule.pattern(16),))
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
          if hasattr(gen_2, 'iterator'): 
            if not gen_2.iterator == None: 
              gen_2.iterator.close()
          else: 
            if hasattr(gen_2, '__iter__'): 
              if not gen_2.__iter__ == None: 
                gen_2.close()
        if not flag_1:
          raise AssertionError("compiler.fc_premises1: 'when' clause 1 failed")
        if hasattr(gen_1, 'iterator'): 
          if not gen_1.iterator == None: 
            gen_1.iterator.close()
        else: 
          if hasattr(gen_1, '__iter__'): 
            if not gen_1.__iter__ == None: 
              gen_1.close()
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
        gen_1 = engine.prove(rule.rule_base.root_name, 'gen_fc_for', context,
                                (rule.pattern(0),
                                 rule.pattern(1),
                                 rule.pattern(2),
                                 rule.pattern(3),
                                 rule.pattern(4),
                                 rule.pattern(5),
                                 rule.pattern(6),
                                 rule.pattern(7),))
        for x_1 in gen_1: 
          assert x_1 is None, \
            "compiler.fc_premise: got unexpected plan from when clause 1"
          mark2 = context.mark(True)
          if rule.pattern(8).match_data(context, context,
                  (() if context.lookup_data('break_cond') is None
                 else "if %s: break" % context.lookup_data('break_cond'),
                 'POPINDENT',
                 context.lookup_data('fn_tail1')),):
            context.end_save_all_undo()
            mark3 = context.mark(True)
            if rule.pattern(9).match_data(context, context,
                    context.lookup_data('clause_num') + 1):
              context.end_save_all_undo()
              mark4 = context.mark(True)
              if rule.pattern(10).match_data(context, context,
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
        if hasattr(gen_1, 'iterator'): 
          if not gen_1.iterator == None: 
            gen_1.iterator.close()
        else: 
          if hasattr(gen_1, '__iter__'): 
            if not gen_1.__iter__ == None: 
              gen_1.close()
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
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                  ()):
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
               "gen_%d = "
               "engine.lookup('%s', '%s', context, "
               "rule.foreach_patterns(%d))" %
               (context.lookup_data('clause_num'), context.lookup_data('kb_name'), context.lookup_data('entity_name'), context.lookup_data('clause_num')),
               "for x_%d in gen_%d: " % (context.lookup_data('clause_num'), context.lookup_data('clause_num')),
               ('ENDING_LINENO', context.lookup_data('end_lineno')),
               ('INDENT', 2)
               )):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                  ("if hasattr(gen_%d, '__iter__'): " % context.lookup_data('clause_num'),
                 ('INDENT', 2),
                 "if not gen_%d.__iter__ == None: " % context.lookup_data('clause_num'),
                 ('INDENT', 2),
                 "gen_%d.close()" % (context.lookup_data('clause_num')),
                 "POPINDENT",
                 "POPINDENT") ):
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
          gen_2 = engine.prove(rule.rule_base.root_name, 'fc_premises', context,
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
                                   rule.pattern(10),))
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
          if hasattr(gen_2, 'iterator'): 
            if not gen_2.iterator == None: 
              gen_2.iterator.close()
          else: 
            if hasattr(gen_2, '__iter__'): 
              if not gen_2.__iter__ == None: 
                gen_2.close()
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
        gen_1 = engine.prove(rule.rule_base.root_name, 'fc_premises', context,
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
                                 rule.pattern(10),))
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
        if hasattr(gen_1, 'iterator'): 
          if not gen_1.iterator == None: 
            gen_1.iterator.close()
        else: 
          if hasattr(gen_1, '__iter__'): 
            if not gen_1.__iter__ == None: 
              gen_1.close()
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
            gen_3 = engine.prove(rule.rule_base.root_name, 'fc_premises', context,
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
                                     rule.pattern(11),))
            for x_3 in gen_3: 
              flag_3 = True
              assert x_3 is None, \
                "compiler.fc_forall_require: got unexpected plan from when clause 3"
              flag_4 = False
              gen_4 = engine.prove(rule.rule_base.root_name, 'fc_premises', context,
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
                                       rule.pattern(17),))
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
              if hasattr(gen_4, 'iterator'): 
                if not gen_4.iterator == None: 
                  gen_4.iterator.close()
              else: 
                if hasattr(gen_4, '__iter__'): 
                  if not gen_4.__iter__ == None: 
                    gen_4.close()
            if not flag_3:
              raise AssertionError("compiler.fc_forall_require: 'when' clause 3 failed")
            if hasattr(gen_3, 'iterator'): 
              if not gen_3.iterator == None: 
                gen_3.iterator.close()
            else: 
              if hasattr(gen_3, '__iter__'): 
                if not gen_3.__iter__ == None: 
                  gen_3.close()
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
            gen_3 = engine.prove(rule.rule_base.root_name, 'fc_premises', context,
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
                                     rule.pattern(11),))
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
            if hasattr(gen_3, 'iterator'): 
              if not gen_3.iterator == None: 
                gen_3.iterator.close()
            else: 
              if hasattr(gen_3, '__iter__'): 
                if not gen_3.__iter__ == None: 
                  gen_3.close()
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
        gen_1 = engine.prove(rule.rule_base.root_name, 'python_premise', context,
                                (rule.pattern(0),
                                 rule.pattern(1),
                                 rule.pattern(2),
                                 rule.pattern(3),
                                 rule.pattern(4),
                                 rule.pattern(5),
                                 rule.pattern(6),))
        for x_1 in gen_1: 
          assert x_1 is None, \
            "compiler.fc_python_premise: got unexpected plan from when clause 1"
          rule.rule_base.num_bc_rule_successes += 1
          yield
        if hasattr(gen_1, 'iterator'): 
          if not gen_1.iterator == None: 
            gen_1.iterator.close()
        else: 
          if hasattr(gen_1, '__iter__'): 
            if not gen_1.__iter__ == None: 
              gen_1.close()
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
        gen_1 = engine.prove(rule.rule_base.root_name, 'assertion', context,
                                (rule.pattern(0),
                                 rule.pattern(1),
                                 rule.pattern(2),
                                 rule.pattern(3),))
        for x_1 in gen_1: 
          flag_1 = True
          assert x_1 is None, \
            "compiler.assertions_n: got unexpected plan from when clause 1"
          flag_2 = False
          gen_2 = engine.prove(rule.rule_base.root_name, 'assertions', context,
                                  (rule.pattern(4),
                                   rule.pattern(5),
                                   rule.pattern(3),
                                   rule.pattern(6),))
          for x_2 in gen_2: 
            flag_2 = True
            assert x_2 is None, \
              "compiler.assertions_n: got unexpected plan from when clause 2"
            rule.rule_base.num_bc_rule_successes += 1
            yield
          if not flag_2:
            raise AssertionError("compiler.assertions_n: 'when' clause 2 failed")
          if hasattr(gen_2, 'iterator'): 
            if not gen_2.iterator == None: 
              gen_2.iterator.close()
          else: 
            if hasattr(gen_2, '__iter__'): 
              if not gen_2.__iter__ == None: 
                gen_2.close()
        if not flag_1:
          raise AssertionError("compiler.assertions_n: 'when' clause 1 failed")
        if hasattr(gen_1, 'iterator'): 
          if not gen_1.iterator == None: 
            gen_1.iterator.close()
        else: 
          if hasattr(gen_1, '__iter__'): 
            if not gen_1.__iter__ == None: 
              gen_1.close()
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
        gen_1 = engine.prove(rule.rule_base.root_name, 'bc_rule', context,
                                (rule.pattern(0),
                                 rule.pattern(1),
                                 rule.pattern(2),
                                 rule.pattern(3),
                                 rule.pattern(4),))
        for x_1 in gen_1: 
          flag_1 = True
          assert x_1 is None, \
            "compiler.bc_rules1: got unexpected plan from when clause 1"
          flag_2 = False
          gen_2 = engine.prove(rule.rule_base.root_name, 'bc_rules', context,
                                  (rule.pattern(0),
                                   rule.pattern(5),
                                   rule.pattern(6),
                                   rule.pattern(7),
                                   rule.pattern(8),))
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
          if hasattr(gen_2, 'iterator'): 
            if not gen_2.iterator == None: 
              gen_2.iterator.close()
          else: 
            if hasattr(gen_2, '__iter__'): 
              if not gen_2.__iter__ == None: 
                gen_2.close()
        if not flag_1:
          raise AssertionError("compiler.bc_rules1: 'when' clause 1 failed")
        if hasattr(gen_1, 'iterator'): 
          if not gen_1.iterator == None: 
            gen_1.iterator.close()
        else: 
          if hasattr(gen_1, '__iter__'): 
            if not gen_1.__iter__ == None: 
              gen_1.close()
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
        gen_1 = engine.prove(rule.rule_base.root_name, 'bc_premises', context,
                                (rule.pattern(0),
                                 rule.pattern(1),
                                 rule.pattern(2),
                                 rule.pattern(3),
                                 rule.pattern(4),
                                 rule.pattern(5),
                                 rule.pattern(6),
                                 rule.pattern(7),))
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
        if hasattr(gen_1, 'iterator'): 
          if not gen_1.iterator == None: 
            gen_1.iterator.close()
        else: 
          if hasattr(gen_1, '__iter__'): 
            if not gen_1.__iter__ == None: 
              gen_1.close()
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
        gen_1 = engine.prove(rule.rule_base.root_name, 'bc_premises1', context,
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
                                 rule.pattern(13),))
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
        if hasattr(gen_1, 'iterator'): 
          if not gen_1.iterator == None: 
            gen_1.iterator.close()
        else: 
          if hasattr(gen_1, '__iter__'): 
            if not gen_1.__iter__ == None: 
              gen_1.close()
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
        gen_1 = engine.prove(rule.rule_base.root_name, 'bc_premise', context,
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
                                 rule.pattern(13),))
        for x_1 in gen_1: 
          flag_1 = True
          assert x_1 is None, \
            "compiler.bc_premises1_n: got unexpected plan from when clause 1"
          flag_2 = False
          gen_2 = engine.prove(rule.rule_base.root_name, 'bc_premises1', context,
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
                                   rule.pattern(20),))
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
          if hasattr(gen_2, 'iterator'): 
            if not gen_2.iterator == None: 
              gen_2.iterator.close()
          else: 
            if hasattr(gen_2, '__iter__'): 
              if not gen_2.__iter__ == None: 
                gen_2.close()
        if not flag_1:
          raise AssertionError("compiler.bc_premises1_n: 'when' clause 1 failed")
        if hasattr(gen_1, 'iterator'): 
          if not gen_1.iterator == None: 
            gen_1.iterator.close()
        else: 
          if hasattr(gen_1, '__iter__'): 
            if not gen_1.__iter__ == None: 
              gen_1.close()
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
                     "gen_%(clause_num)d = "
                     "engine.prove(%(kb_name)s, %(entity_name)s, context," %
                     {'clause_num': context.lookup_data('clause_num'),
                     'kb_name': context.lookup_data('kb_name2'),
                     'entity_name': context.lookup_data('entity_name')},
                     ('INDENT', 2),
                     ('INDENT', 22),
                     helpers.list_format(('rule.pattern(%d)' % pat_num
                     for pat_num in context.lookup_data('pat_nums')),
                     '(', '))'),
                     "POPINDENT", 
                     "POPINDENT",
                     "for x_%d in gen_%d: " % (context.lookup_data('clause_num'), context.lookup_data('clause_num')),
                     ('INDENT', 2)
                     )):
                context.end_save_all_undo()
                mark5 = context.mark(True)
                if rule.pattern(4).match_data(context, context,
                        ("if hasattr(gen_%d, 'iterator'): " % context.lookup_data('clause_num'),
                       ('INDENT', 2),
                       "if not gen_%d.iterator == None: " % context.lookup_data('clause_num'),
                       ('INDENT', 2),
                       "gen_%d.iterator.close()" % context.lookup_data('clause_num'),
                       "POPINDENT",
                       "POPINDENT",
                       "else: ",
                       ('INDENT', 2),
                       "if hasattr(gen_%d, '__iter__'): " % context.lookup_data('clause_num'),
                       ('INDENT', 2),
                       "if not gen_%d.__iter__ == None: " % context.lookup_data('clause_num'),
                       ('INDENT', 2),
                       "gen_%d.close()" % (context.lookup_data('clause_num')),
                       "POPINDENT",
                       "POPINDENT",
                       "POPINDENT") ):
                  context.end_save_all_undo()
                  flag_6 = False
                  gen_6 = engine.prove(rule.rule_base.root_name, 'add_required', context,
                                          (rule.pattern(5),
                                           rule.pattern(6),
                                           rule.pattern(7),
                                           rule.pattern(8),
                                           rule.pattern(3),
                                           rule.pattern(9),
                                           rule.pattern(10),
                                           rule.pattern(11),))
                  for x_6 in gen_6: 
                    flag_6 = True
                    assert x_6 is None, \
                      "compiler.bc_premise: got unexpected plan from when clause 6"
                    flag_7 = False
                    gen_7 = engine.prove(rule.rule_base.root_name, 'gen_plan_lines', context,
                                            (rule.pattern(6),
                                             rule.pattern(7),
                                             rule.pattern(8),
                                             rule.pattern(12),
                                             rule.pattern(13),
                                             rule.pattern(14),
                                             rule.pattern(15),
                                             rule.pattern(16),
                                             rule.pattern(17),
                                             rule.pattern(18),
                                             rule.pattern(19),))
                    for x_7 in gen_7: 
                      flag_7 = True
                      assert x_7 is None, \
                        "compiler.bc_premise: got unexpected plan from when clause 7"
                      mark8 = context.mark(True)
                      if rule.pattern(20).match_data(context, context,
                              helpers.merge_patterns(context.lookup_data('plan_vars_needed'),
                             context.lookup_data('plan_var_names_in'))):
                        context.end_save_all_undo()
                        mark9 = context.mark(True)
                        if rule.pattern(21).match_data(context, context,
                                context.lookup_data('fn_head2') + context.lookup_data('fn_head3') + (('ENDING_LINENO', context.lookup_data('end_lineno')),)):
                          context.end_save_all_undo()
                          mark10 = context.mark(True)
                          if rule.pattern(22).match_data(context, context,
                                  (context.lookup_data('fn_tail3'),
                                 () if context.lookup_data('break_cond') is None
                                 else "if %s: break" % context.lookup_data('break_cond'),
                                 context.lookup_data('fn_tail2'),
                                 context.lookup_data('fn_tail1'))):
                            context.end_save_all_undo()
                            rule.rule_base.num_bc_rule_successes += 1
                            yield
                          else: context.end_save_all_undo()
                          context.undo_to_mark(mark10)
                        else: context.end_save_all_undo()
                        context.undo_to_mark(mark9)
                      else: context.end_save_all_undo()
                      context.undo_to_mark(mark8)
                    if not flag_7:
                      raise AssertionError("compiler.bc_premise: 'when' clause 7 failed")
                    if hasattr(gen_7, 'iterator'): 
                      if not gen_7.iterator == None: 
                        gen_7.iterator.close()
                    else: 
                      if hasattr(gen_7, '__iter__'): 
                        if not gen_7.__iter__ == None: 
                          gen_7.close()
                  if not flag_6:
                    raise AssertionError("compiler.bc_premise: 'when' clause 6 failed")
                  if hasattr(gen_6, 'iterator'): 
                    if not gen_6.iterator == None: 
                      gen_6.iterator.close()
                  else: 
                    if hasattr(gen_6, '__iter__'): 
                      if not gen_6.__iter__ == None: 
                        gen_6.close()
                else: context.end_save_all_undo()
                context.undo_to_mark(mark5)
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
          gen_2 = engine.prove(rule.rule_base.root_name, 'bc_premises1', context,
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
                                   rule.pattern(13),))
          for x_2 in gen_2: 
            flag_2 = True
            assert x_2 is None, \
              "compiler.bc_first: got unexpected plan from when clause 2"
            flag_3 = False
            gen_3 = engine.prove(rule.rule_base.root_name, 'add_required', context,
                                    (rule.pattern(14),
                                     rule.pattern(1),
                                     rule.pattern(2),
                                     rule.pattern(3),
                                     rule.pattern(12),
                                     rule.pattern(13),
                                     rule.pattern(15),
                                     rule.pattern(16),))
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
            if hasattr(gen_3, 'iterator'): 
              if not gen_3.iterator == None: 
                gen_3.iterator.close()
            else: 
              if hasattr(gen_3, '__iter__'): 
                if not gen_3.__iter__ == None: 
                  gen_3.close()
          if not flag_2:
            raise AssertionError("compiler.bc_first: 'when' clause 2 failed")
          if hasattr(gen_2, 'iterator'): 
            if not gen_2.iterator == None: 
              gen_2.iterator.close()
          else: 
            if hasattr(gen_2, '__iter__'): 
              if not gen_2.__iter__ == None: 
                gen_2.close()
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
        gen_1 = engine.prove(rule.rule_base.root_name, 'bc_premises1', context,
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
                                 rule.pattern(13),))
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
        if hasattr(gen_1, 'iterator'): 
          if not gen_1.iterator == None: 
            gen_1.iterator.close()
        else: 
          if hasattr(gen_1, '__iter__'): 
            if not gen_1.__iter__ == None: 
              gen_1.close()
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
            gen_3 = engine.prove(rule.rule_base.root_name, 'bc_premises1', context,
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
                                     rule.pattern(14),))
            for x_3 in gen_3: 
              flag_3 = True
              assert x_3 is None, \
                "compiler.bc_forall_require: got unexpected plan from when clause 3"
              flag_4 = False
              gen_4 = engine.prove(rule.rule_base.root_name, 'bc_premises1', context,
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
                                       rule.pattern(20),))
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
              if hasattr(gen_4, 'iterator'): 
                if not gen_4.iterator == None: 
                  gen_4.iterator.close()
              else: 
                if hasattr(gen_4, '__iter__'): 
                  if not gen_4.__iter__ == None: 
                    gen_4.close()
            if not flag_3:
              raise AssertionError("compiler.bc_forall_require: 'when' clause 3 failed")
            if hasattr(gen_3, 'iterator'): 
              if not gen_3.iterator == None: 
                gen_3.iterator.close()
            else: 
              if hasattr(gen_3, '__iter__'): 
                if not gen_3.__iter__ == None: 
                  gen_3.close()
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
            gen_3 = engine.prove(rule.rule_base.root_name, 'bc_premises1', context,
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
                                     rule.pattern(14),))
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
            if hasattr(gen_3, 'iterator'): 
              if not gen_3.iterator == None: 
                gen_3.iterator.close()
            else: 
              if hasattr(gen_3, '__iter__'): 
                if not gen_3.__iter__ == None: 
                  gen_3.close()
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
          gen_2 = engine.prove(rule.rule_base.root_name, 'plan_bindings', context,
                                  (rule.pattern(1),
                                   rule.pattern(2),
                                   rule.pattern(3),
                                   rule.pattern(4),
                                   rule.pattern(5),
                                   rule.pattern(6),
                                   rule.pattern(7),))
          for x_2 in gen_2: 
            flag_2 = True
            assert x_2 is None, \
              "compiler.as_plan: got unexpected plan from when clause 2"
            rule.rule_base.num_bc_rule_successes += 1
            yield
          if not flag_2:
            raise AssertionError("compiler.as_plan: 'when' clause 2 failed")
          if hasattr(gen_2, 'iterator'): 
            if not gen_2.iterator == None: 
              gen_2.iterator.close()
          else: 
            if hasattr(gen_2, '__iter__'): 
              if not gen_2.__iter__ == None: 
                gen_2.close()
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
          gen_2 = engine.prove(rule.rule_base.root_name, 'plan_bindings', context,
                                  (rule.pattern(1),
                                   rule.pattern(2),
                                   rule.pattern(3),
                                   rule.pattern(4),
                                   rule.pattern(5),
                                   rule.pattern(6),
                                   rule.pattern(7),))
          for x_2 in gen_2: 
            flag_2 = True
            assert x_2 is None, \
              "compiler.plan_spec: got unexpected plan from when clause 2"
            rule.rule_base.num_bc_rule_successes += 1
            yield
          if not flag_2:
            raise AssertionError("compiler.plan_spec: 'when' clause 2 failed")
          if hasattr(gen_2, 'iterator'): 
            if not gen_2.iterator == None: 
              gen_2.iterator.close()
          else: 
            if hasattr(gen_2, '__iter__'): 
              if not gen_2.__iter__ == None: 
                gen_2.close()
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
          gen_2 = engine.prove(rule.rule_base.root_name, 'python_premise', context,
                                  (rule.pattern(1),
                                   rule.pattern(2),
                                   rule.pattern(3),
                                   rule.pattern(4),
                                   rule.pattern(5),
                                   rule.pattern(6),
                                   rule.pattern(7),))
          for x_2 in gen_2: 
            assert x_2 is None, \
              "compiler.bc_python_premise: got unexpected plan from when clause 2"
            rule.rule_base.num_bc_rule_successes += 1
            yield
          if hasattr(gen_2, 'iterator'): 
            if not gen_2.iterator == None: 
              gen_2.iterator.close()
          else: 
            if hasattr(gen_2, '__iter__'): 
              if not gen_2.__iter__ == None: 
                gen_2.close()
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
                  (contexts.variable('rb_name'),
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
                   contexts.variable('fn_tail1'),
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
                   contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),),
                  (),
                  (contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),))
  
  bc_rule.bc_rule('gen_fc_for_true', This_rule_base, 'gen_fc_for',
                  gen_fc_for_true, None,
                  (contexts.variable('kb_name'),
                   contexts.variable('entity_name'),
                   contexts.variable('start_lineno'),
                   contexts.variable('end_lineno'),
                   pattern.pattern_literal(True),
                   contexts.variable('clause_num'),
                   contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),),
                  (),
                  (contexts.variable('fn_head'),
                   contexts.variable('fn_tail'),))
  
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
                   contexts.variable('fn_tail1'),
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
Krb_filename = 'D:\Projekte\Pyke\trunk\pyke\krb_compiler\compiler.krb'
Krb_lineno_map = (
    ((14, 18), (24, 28)),
    ((22, 22), (30, 30)),
    ((26, 26), (31, 31)),
    ((30, 30), (32, 32)),
    ((33, 40), (33, 33)),
    ((42, 49), (34, 34)),
    ((51, 60), (35, 36)),
    ((63, 75), (37, 49)),
    ((79, 84), (50, 55)),
    ((88, 102), (56, 70)),
    ((155, 159), (73, 73)),
    ((163, 163), (75, 75)),
    ((179, 183), (78, 78)),
    ((187, 189), (80, 82)),
    ((205, 209), (85, 85)),
    ((223, 227), (88, 90)),
    ((230, 237), (92, 92)),
    ((239, 246), (93, 93)),
    ((277, 281), (96, 97)),
    ((284, 299), (99, 101)),
    ((301, 309), (102, 103)),
    ((312, 329), (104, 121)),
    ((333, 340), (122, 129)),
    ((376, 380), (132, 133)),
    ((394, 398), (136, 139)),
    ((401, 416), (141, 144)),
    ((418, 433), (145, 148)),
    ((436, 436), (149, 149)),
    ((470, 474), (152, 157)),
    ((476, 487), (159, 160)),
    ((490, 493), (161, 164)),
    ((497, 497), (165, 165)),
    ((501, 506), (166, 171)),
    ((533, 537), (174, 175)),
    ((541, 549), (177, 185)),
    ((553, 553), (186, 186)),
    ((571, 575), (189, 190)),
    ((579, 587), (192, 200)),
    ((591, 597), (201, 207)),
    ((615, 619), (211, 214)),
    ((623, 623), (216, 216)),
    ((626, 641), (217, 220)),
    ((644, 644), (221, 221)),
    ((648, 648), (222, 222)),
    ((677, 681), (225, 228)),
    ((684, 699), (230, 233)),
    ((702, 702), (234, 234)),
    ((727, 731), (237, 240)),
    ((735, 735), (242, 242)),
    ((739, 739), (243, 243)),
    ((742, 757), (244, 247)),
    ((759, 774), (248, 251)),
    ((777, 787), (252, 262)),
    ((791, 791), (263, 263)),
    ((831, 835), (266, 269)),
    ((839, 839), (271, 271)),
    ((843, 843), (272, 272)),
    ((846, 861), (273, 276)),
    ((864, 869), (277, 282)),
    ((898, 902), (285, 288)),
    ((904, 914), (290, 292)),
    ((934, 938), (295, 295)),
    ((952, 956), (298, 299)),
    ((959, 967), (301, 301)),
    ((969, 977), (302, 302)),
    ((1008, 1012), (305, 307)),
    ((1016, 1017), (309, 310)),
    ((1021, 1030), (311, 320)),
    ((1048, 1052), (323, 328)),
    ((1066, 1070), (331, 331)),
    ((1084, 1088), (334, 337)),
    ((1091, 1100), (339, 339)),
    ((1102, 1111), (340, 341)),
    ((1114, 1114), (342, 342)),
    ((1148, 1152), (345, 347)),
    ((1155, 1167), (349, 351)),
    ((1170, 1172), (352, 354)),
    ((1176, 1183), (355, 362)),
    ((1187, 1190), (363, 366)),
    ((1219, 1223), (369, 371)),
    ((1226, 1244), (373, 376)),
    ((1247, 1247), (377, 377)),
    ((1251, 1254), (378, 381)),
    ((1258, 1263), (382, 387)),
    ((1292, 1296), (390, 392)),
    ((1310, 1314), (395, 399)),
    ((1317, 1335), (401, 405)),
    ((1337, 1355), (406, 410)),
    ((1358, 1358), (411, 411)),
    ((1362, 1362), (412, 412)),
    ((1366, 1366), (413, 413)),
    ((1404, 1408), (416, 422)),
    ((1412, 1412), (424, 424)),
    ((1416, 1416), (425, 425)),
    ((1420, 1421), (426, 427)),
    ((1425, 1440), (428, 443)),
    ((1444, 1460), (444, 462)),
    ((1463, 1475), (463, 464)),
    ((1477, 1492), (465, 468)),
    ((1495, 1496), (469, 470)),
    ((1500, 1500), (471, 471)),
    ((1504, 1508), (472, 476)),
    ((1556, 1560), (479, 483)),
    ((1564, 1564), (485, 485)),
    ((1567, 1585), (486, 490)),
    ((1587, 1599), (491, 492)),
    ((1602, 1602), (493, 493)),
    ((1606, 1606), (494, 494)),
    ((1644, 1648), (497, 501)),
    ((1651, 1669), (503, 507)),
    ((1672, 1672), (508, 508)),
    ((1697, 1701), (511, 515)),
    ((1705, 1705), (517, 517)),
    ((1709, 1709), (518, 518)),
    ((1712, 1730), (519, 523)),
    ((1732, 1750), (524, 528)),
    ((1753, 1761), (529, 539)),
    ((1799, 1803), (542, 546)),
    ((1807, 1807), (549, 549)),
    ((1811, 1811), (550, 550)),
    ((1814, 1832), (551, 555)),
    ((1835, 1840), (556, 561)),
    ((1869, 1873), (564, 566)),
    ((1877, 1884), (568, 575)),
    ((1900, 1904), (578, 582)),
    ((1908, 1910), (584, 586)),
    ((1913, 1924), (587, 588)),
    ((1948, 1952), (591, 596)),
    ((1956, 1958), (598, 600)),
    ((1961, 1972), (601, 602)),
    ((1996, 2000), (605, 607)),
    ((2004, 2005), (609, 610)),
    ((2021, 2025), (613, 614)),
    ((2029, 2049), (616, 636)),
    ((2053, 2053), (637, 637)),
    ((2071, 2075), (640, 641)),
    ((2089, 2093), (644, 645)),
    ((2097, 2100), (647, 650)),
    ((2104, 2110), (651, 657)),
    ((2128, 2132), (660, 664)),
    ((2136, 2136), (666, 666)),
    ((2138, 2148), (667, 669)),
    ((2170, 2174), (672, 676)),
    ((2178, 2179), (678, 679)),
    ((2183, 2183), (680, 680)),
    ((2187, 2197), (681, 691)),
    ((2201, 2203), (692, 694)),
    ((2225, 2229), (697, 701)),
    ((2233, 2234), (703, 704)),
    ((2238, 2238), (705, 705)),
    ((2242, 2254), (706, 718)),
    ((2258, 2267), (719, 728)),
    ((2289, 2293), (731, 736)),
    ((2297, 2297), (738, 738)),
    ((2301, 2308), (739, 746)),
    ((2326, 2330), (749, 757)),
)
