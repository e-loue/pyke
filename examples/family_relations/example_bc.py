# example_bc.py

from __future__ import with_statement, absolute_import, division
from pyke import tmp_itertools as itertools
from pyke import contexts, pattern, bc_rule
from pyke.knowledge_base import prove
import example

def niece_or_nephew_and_aunt_or_uncle(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    if all(itertools.imap(lambda pat, arg:
                            pat.match_pattern(context, context,
                                              arg, arg_context),
                          patterns,
                          arg_patterns)):
      for x_1 in prove('family', 'siblings', context,
                     (rule.pattern(0),
                      rule.pattern(1),
                      rule.pattern(2),
                      rule.pattern(3),)):
        assert x_1 is None, \
          "%(rule_name)s: got unexpected plan from when clause 1"
        for x_2 in prove('family', 'child_parent', context,
                       (rule.pattern(4),
                        rule.pattern(1),
                        rule.pattern(2),
                        rule.pattern(5),)):
          assert x_2 is None, \
            "%(rule_name)s: got unexpected plan from when clause 2"
          for x_3 in prove('family', 'as_au', context,
                         (rule.pattern(3),
                          rule.pattern(6),)):
            assert x_3 is None, \
              "%(rule_name)s: got unexpected plan from when clause 3"
            for x_4 in prove('family', 'as_nn', context,
                           (rule.pattern(5),
                            rule.pattern(7),)):
              assert x_4 is None, \
                "%(rule_name)s: got unexpected plan from when clause 4"
              yield
    context.done()

bc_rule.bc_rule('niece_or_nephew_and_aunt_or_uncle', example.This_rule_base, 'nn_au',
                niece_or_nephew_and_aunt_or_uncle, None,
                (contexts.variable('younger'),
                 contexts.variable('elder'),
                 pattern.pattern_literal(()),
                 contexts.variable('au_type'),
                 contexts.variable('nn_type'),),
                (),
                (contexts.variable('elder'),
                 contexts.variable('parent'),
                 contexts.anonymous(),
                 contexts.variable('elder_type'),
                 contexts.variable('younger'),
                 contexts.variable('younger_type'),
                 contexts.variable('au_type'),
                 contexts.variable('nn_type'),))

def parent_and_child(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    if all(itertools.imap(lambda pat, arg:
                            pat.match_pattern(context, context,
                                              arg, arg_context),
                          patterns,
                          arg_patterns)):
      for x_1 in prove('family', 'child_parent', context,
                     (rule.pattern(0),
                      rule.pattern(1),
                      rule.pattern(2),
                      rule.pattern(3),)):
        assert x_1 is None, \
          "%(rule_name)s: got unexpected plan from when clause 1"
        yield
    context.done()

bc_rule.bc_rule('parent_and_child', example.This_rule_base, 'child_parent',
                parent_and_child, None,
                (contexts.variable('child'),
                 contexts.variable('parent'),
                 pattern.pattern_literal(()),
                 contexts.variable('parent_type'),
                 contexts.variable('child_type'),),
                (),
                (contexts.variable('child'),
                 contexts.variable('parent'),
                 contexts.variable('parent_type'),
                 contexts.variable('child_type'),))

def grand_parent_and_child(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    if all(itertools.imap(lambda pat, arg:
                            pat.match_pattern(context, context,
                                              arg, arg_context),
                          patterns,
                          arg_patterns)):
      for x_1 in prove('family', 'child_parent', context,
                     (rule.pattern(0),
                      rule.pattern(1),
                      rule.pattern(2),
                      rule.pattern(3),)):
        assert x_1 is None, \
          "%(rule_name)s: got unexpected plan from when clause 1"
        for x_2 in prove('family', 'child_parent', context,
                       (rule.pattern(1),
                        rule.pattern(4),
                        rule.pattern(5),
                        rule.pattern(2),)):
          assert x_2 is None, \
            "%(rule_name)s: got unexpected plan from when clause 2"
          yield
    context.done()

bc_rule.bc_rule('grand_parent_and_child', example.This_rule_base, 'child_parent',
                grand_parent_and_child, None,
                (contexts.variable('child'),
                 contexts.variable('grand_parent'),
                 pattern.pattern_literal(('grand',)),
                 contexts.variable('parent_type'),
                 contexts.variable('child_type'),),
                (),
                (contexts.variable('child'),
                 contexts.variable('parent'),
                 contexts.anonymous(),
                 contexts.variable('child_type'),
                 contexts.variable('grand_parent'),
                 contexts.variable('parent_type'),))

def great_grand_parent_and_child(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    if all(itertools.imap(lambda pat, arg:
                            pat.match_pattern(context, context,
                                              arg, arg_context),
                          patterns,
                          arg_patterns)):
      for x_1 in prove('family', 'child_parent', context,
                     (rule.pattern(0),
                      rule.pattern(1),
                      rule.pattern(2),
                      rule.pattern(3),)):
        assert x_1 is None, \
          "%(rule_name)s: got unexpected plan from when clause 1"
        for x_2 in prove('example', 'child_parent', context,
                       (rule.pattern(1),
                        rule.pattern(4),
                        rule.pattern(5),
                        rule.pattern(6),
                        rule.pattern(2),)):
          assert x_2 is None, \
            "%(rule_name)s: got unexpected plan from when clause 2"
          yield
    context.done()

bc_rule.bc_rule('great_grand_parent_and_child', example.This_rule_base, 'child_parent',
                great_grand_parent_and_child, None,
                (contexts.variable('child'),
                 contexts.variable('grand_parent'),
                 pattern.pattern_tuple((pattern.pattern_literal('great'), contexts.variable('a'),), contexts.variable('b')),
                 contexts.variable('parent_type'),
                 contexts.variable('child_type'),),
                (),
                (contexts.variable('child'),
                 contexts.variable('grand_child'),
                 contexts.anonymous(),
                 contexts.variable('child_type'),
                 contexts.variable('grand_parent'),
                 pattern.pattern_tuple((contexts.variable('a'),), contexts.variable('b')),
                 contexts.variable('parent_type'),))

def great_niece_or_nephew_and_aunt_or_uncle(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    if all(itertools.imap(lambda pat, arg:
                            pat.match_pattern(context, context,
                                              arg, arg_context),
                          patterns,
                          arg_patterns)):
      for x_1 in prove('family', 'child_parent', context,
                     (rule.pattern(0),
                      rule.pattern(1),
                      rule.pattern(2),
                      rule.pattern(3),)):
        assert x_1 is None, \
          "%(rule_name)s: got unexpected plan from when clause 1"
        for x_2 in prove('example', 'nn_au', context,
                       (rule.pattern(1),
                        rule.pattern(4),
                        rule.pattern(5),
                        rule.pattern(6),
                        rule.pattern(2),)):
          assert x_2 is None, \
            "%(rule_name)s: got unexpected plan from when clause 2"
          for x_3 in prove('family', 'as_nn', context,
                         (rule.pattern(3),
                          rule.pattern(7),)):
            assert x_3 is None, \
              "%(rule_name)s: got unexpected plan from when clause 3"
            yield
    context.done()

bc_rule.bc_rule('great_niece_or_nephew_and_aunt_or_uncle', example.This_rule_base, 'nn_au',
                great_niece_or_nephew_and_aunt_or_uncle, None,
                (contexts.variable('younger'),
                 contexts.variable('elder'),
                 pattern.pattern_tuple((pattern.pattern_literal('great'),), contexts.variable('greats')),
                 contexts.variable('au_type'),
                 contexts.variable('nn_type'),),
                (),
                (contexts.variable('younger'),
                 contexts.variable('parent'),
                 contexts.anonymous(),
                 contexts.variable('younger_type'),
                 contexts.variable('elder'),
                 contexts.variable('greats'),
                 contexts.variable('au_type'),
                 contexts.variable('nn_type'),))

def first_cousins(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    if all(itertools.imap(lambda pat, arg:
                            pat.match_pattern(context, context,
                                              arg, arg_context),
                          patterns,
                          arg_patterns)):
      for x_1 in prove('family', 'child_parent', context,
                     (rule.pattern(0),
                      rule.pattern(1),
                      rule.pattern(2),
                      rule.pattern(2),)):
        assert x_1 is None, \
          "%(rule_name)s: got unexpected plan from when clause 1"
        for x_2 in prove('family', 'siblings', context,
                       (rule.pattern(1),
                        rule.pattern(3),
                        rule.pattern(2),
                        rule.pattern(2),)):
          assert x_2 is None, \
            "%(rule_name)s: got unexpected plan from when clause 2"
          for x_3 in prove('family', 'child_parent', context,
                         (rule.pattern(4),
                          rule.pattern(3),
                          rule.pattern(2),
                          rule.pattern(2),)):
            assert x_3 is None, \
              "%(rule_name)s: got unexpected plan from when clause 3"
            yield
    context.done()

bc_rule.bc_rule('first_cousins', example.This_rule_base, 'cousins',
                first_cousins, None,
                (contexts.variable('cousin1'),
                 contexts.variable('cousin2'),
                 pattern.pattern_literal(1),),
                (),
                (contexts.variable('cousin1'),
                 contexts.variable('sibling1'),
                 contexts.anonymous(),
                 contexts.variable('sibling2'),
                 contexts.variable('cousin2'),))

def nth_cousins(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    if all(itertools.imap(lambda pat, arg:
                            pat.match_pattern(context, context,
                                              arg, arg_context),
                          patterns,
                          arg_patterns)):
      for x_1 in prove('family', 'child_parent', context,
                     (rule.pattern(0),
                      rule.pattern(1),
                      rule.pattern(2),
                      rule.pattern(2),)):
        assert x_1 is None, \
          "%(rule_name)s: got unexpected plan from when clause 1"
        for x_2 in prove('family', 'siblings', context,
                       (rule.pattern(1),
                        rule.pattern(3),
                        rule.pattern(4),)):
          assert x_2 is None, \
            "%(rule_name)s: got unexpected plan from when clause 2"
          for x_3 in prove('family', 'child_parent', context,
                         (rule.pattern(5),
                          rule.pattern(3),
                          rule.pattern(2),
                          rule.pattern(2),)):
            assert x_3 is None, \
              "%(rule_name)s: got unexpected plan from when clause 3"
            mark4 = context.mark(True)
            if rule.pattern(6).match_data(context, context,
                    context.lookup_data('n') + 1):
              context.end_save_all_undo()
              yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark4)
    context.done()

bc_rule.bc_rule('nth_cousins', example.This_rule_base, 'cousins',
                nth_cousins, None,
                (contexts.variable('next_cousin1'),
                 contexts.variable('next_cousin2'),
                 contexts.variable('next_n'),),
                (),
                (contexts.variable('next_cousin1'),
                 contexts.variable('cousin1'),
                 contexts.anonymous(),
                 contexts.variable('cousin2'),
                 contexts.variable('n'),
                 contexts.variable('next_cousin2'),
                 contexts.variable('next_n'),))

def how_related_child_parent(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    if all(itertools.imap(lambda pat, arg:
                            pat.match_pattern(context, context,
                                              arg, arg_context),
                          patterns,
                          arg_patterns)):
      for x_1 in prove('example', 'child_parent', context,
                     (rule.pattern(0),
                      rule.pattern(1),
                      rule.pattern(2),
                      rule.pattern(3),
                      rule.pattern(4),)):
        assert x_1 is None, \
          "%(rule_name)s: got unexpected plan from when clause 1"
        for x_2 in prove('example', 'add_prefix', context,
                       (rule.pattern(2),)):
          assert x_2 is not None, \
            "%(rule_name)s: expected plan from when clause 2"
          mark2 = context.mark(True)
          if not rule.pattern(5).match_data(context, context, x_2):
            raise AssertionError("%(rule_name)s: plan match to $plan#2 failed in when clause 2")
          context.end_save_all_undo()
          yield context
          context.undo_to_mark(mark2)
    context.done()

bc_rule.bc_rule('how_related_child_parent', example.This_rule_base, 'how_related',
                how_related_child_parent, example.how_related_child_parent,
                (contexts.variable('person1'),
                 contexts.variable('person2'),),
                ('plan#2', 'p2_type', 'p1_type',),
                (contexts.variable('person1'),
                 contexts.variable('person2'),
                 contexts.variable('prefix'),
                 contexts.variable('p2_type'),
                 contexts.variable('p1_type'),
                 contexts.variable('plan#2'),))

def how_related_parent_child(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    if all(itertools.imap(lambda pat, arg:
                            pat.match_pattern(context, context,
                                              arg, arg_context),
                          patterns,
                          arg_patterns)):
      for x_1 in prove('example', 'child_parent', context,
                     (rule.pattern(0),
                      rule.pattern(1),
                      rule.pattern(2),
                      rule.pattern(3),
                      rule.pattern(4),)):
        assert x_1 is None, \
          "%(rule_name)s: got unexpected plan from when clause 1"
        for x_2 in prove('example', 'add_prefix', context,
                       (rule.pattern(2),)):
          assert x_2 is not None, \
            "%(rule_name)s: expected plan from when clause 2"
          mark2 = context.mark(True)
          if not rule.pattern(5).match_data(context, context, x_2):
            raise AssertionError("%(rule_name)s: plan match to $plan#2 failed in when clause 2")
          context.end_save_all_undo()
          yield context
          context.undo_to_mark(mark2)
    context.done()

bc_rule.bc_rule('how_related_parent_child', example.This_rule_base, 'how_related',
                how_related_parent_child, example.how_related_parent_child,
                (contexts.variable('person1'),
                 contexts.variable('person2'),),
                ('plan#2', 'p2_type', 'p1_type',),
                (contexts.variable('person2'),
                 contexts.variable('person1'),
                 contexts.variable('prefix'),
                 contexts.variable('p1_type'),
                 contexts.variable('p2_type'),
                 contexts.variable('plan#2'),))

def how_related_siblings(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    if all(itertools.imap(lambda pat, arg:
                            pat.match_pattern(context, context,
                                              arg, arg_context),
                          patterns,
                          arg_patterns)):
      for x_1 in prove('family', 'siblings', context,
                     (rule.pattern(0),
                      rule.pattern(1),
                      rule.pattern(2),
                      rule.pattern(3),)):
        assert x_1 is None, \
          "%(rule_name)s: got unexpected plan from when clause 1"
        yield context
    context.done()

bc_rule.bc_rule('how_related_siblings', example.This_rule_base, 'how_related',
                how_related_siblings, example.how_related_siblings,
                (contexts.variable('person1'),
                 contexts.variable('person2'),),
                ('p2_type', 'p1_type',),
                (contexts.variable('person1'),
                 contexts.variable('person2'),
                 contexts.variable('p2_type'),
                 contexts.variable('p1_type'),))

def how_related_nn_au(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    if all(itertools.imap(lambda pat, arg:
                            pat.match_pattern(context, context,
                                              arg, arg_context),
                          patterns,
                          arg_patterns)):
      for x_1 in prove('example', 'nn_au', context,
                     (rule.pattern(0),
                      rule.pattern(1),
                      rule.pattern(2),
                      rule.pattern(3),
                      rule.pattern(4),)):
        assert x_1 is None, \
          "%(rule_name)s: got unexpected plan from when clause 1"
        for x_2 in prove('example', 'add_prefix', context,
                       (rule.pattern(2),)):
          assert x_2 is not None, \
            "%(rule_name)s: expected plan from when clause 2"
          mark2 = context.mark(True)
          if not rule.pattern(5).match_data(context, context, x_2):
            raise AssertionError("%(rule_name)s: plan match to $plan#2 failed in when clause 2")
          context.end_save_all_undo()
          yield context
          context.undo_to_mark(mark2)
    context.done()

bc_rule.bc_rule('how_related_nn_au', example.This_rule_base, 'how_related',
                how_related_nn_au, example.how_related_nn_au,
                (contexts.variable('person1'),
                 contexts.variable('person2'),),
                ('plan#2', 'p2_type', 'p1_type',),
                (contexts.variable('person1'),
                 contexts.variable('person2'),
                 contexts.variable('prefix'),
                 contexts.variable('p2_type'),
                 contexts.variable('p1_type'),
                 contexts.variable('plan#2'),))

def how_related_au_nn(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    if all(itertools.imap(lambda pat, arg:
                            pat.match_pattern(context, context,
                                              arg, arg_context),
                          patterns,
                          arg_patterns)):
      for x_1 in prove('example', 'nn_au', context,
                     (rule.pattern(0),
                      rule.pattern(1),
                      rule.pattern(2),
                      rule.pattern(3),
                      rule.pattern(4),)):
        assert x_1 is None, \
          "%(rule_name)s: got unexpected plan from when clause 1"
        for x_2 in prove('example', 'add_prefix', context,
                       (rule.pattern(2),)):
          assert x_2 is not None, \
            "%(rule_name)s: expected plan from when clause 2"
          mark2 = context.mark(True)
          if not rule.pattern(5).match_data(context, context, x_2):
            raise AssertionError("%(rule_name)s: plan match to $plan#2 failed in when clause 2")
          context.end_save_all_undo()
          yield context
          context.undo_to_mark(mark2)
    context.done()

bc_rule.bc_rule('how_related_au_nn', example.This_rule_base, 'how_related',
                how_related_au_nn, example.how_related_au_nn,
                (contexts.variable('person1'),
                 contexts.variable('person2'),),
                ('plan#2', 'p2_type', 'p1_type',),
                (contexts.variable('person2'),
                 contexts.variable('person1'),
                 contexts.variable('prefix'),
                 contexts.variable('p1_type'),
                 contexts.variable('p2_type'),
                 contexts.variable('plan#2'),))

def how_related_cousins(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    if all(itertools.imap(lambda pat, arg:
                            pat.match_pattern(context, context,
                                              arg, arg_context),
                          patterns,
                          arg_patterns)):
      for x_1 in prove('example', 'cousins', context,
                     (rule.pattern(0),
                      rule.pattern(1),
                      rule.pattern(2),)):
        assert x_1 is None, \
          "%(rule_name)s: got unexpected plan from when clause 1"
        for x_2 in prove('example', 'nth_cousin', context,
                       (rule.pattern(2),)):
          assert x_2 is not None, \
            "%(rule_name)s: expected plan from when clause 2"
          mark2 = context.mark(True)
          if not rule.pattern(3).match_data(context, context, x_2):
            raise AssertionError("%(rule_name)s: plan match to $plan#2 failed in when clause 2")
          context.end_save_all_undo()
          yield context
          context.undo_to_mark(mark2)
    context.done()

bc_rule.bc_rule('how_related_cousins', example.This_rule_base, 'how_related',
                how_related_cousins, example.how_related_cousins,
                (contexts.variable('cousin1'),
                 contexts.variable('cousin2'),),
                ('plan#2',),
                (contexts.variable('cousin1'),
                 contexts.variable('cousin2'),
                 contexts.variable('n'),
                 contexts.variable('plan#2'),))

def how_related_removed_cousins(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    if all(itertools.imap(lambda pat, arg:
                            pat.match_pattern(context, context,
                                              arg, arg_context),
                          patterns,
                          arg_patterns)):
      for x_1 in prove('example', 'child_parent', context,
                     (rule.pattern(0),
                      rule.pattern(1),
                      rule.pattern(2),
                      rule.pattern(3),
                      rule.pattern(3),)):
        assert x_1 is None, \
          "%(rule_name)s: got unexpected plan from when clause 1"
        for x_2 in prove('example', 'cousins', context,
                       (rule.pattern(1),
                        rule.pattern(4),
                        rule.pattern(5),)):
          assert x_2 is None, \
            "%(rule_name)s: got unexpected plan from when clause 2"
          for x_3 in prove('example', 'nth_cousin', context,
                         (rule.pattern(5),)):
            assert x_3 is not None, \
              "%(rule_name)s: expected plan from when clause 3"
            mark3 = context.mark(True)
            if not rule.pattern(6).match_data(context, context, x_3):
              raise AssertionError("%(rule_name)s: plan match to $plan#3 failed in when clause 3")
            context.end_save_all_undo()
            mark4 = context.mark(True)
            if rule.pattern(7).match_data(context, context,
                    len(context.lookup_data('grand')) + 1):
              context.end_save_all_undo()
              yield context
            else: context.end_save_all_undo()
            context.undo_to_mark(mark4)
            context.undo_to_mark(mark3)
    context.done()

bc_rule.bc_rule('how_related_removed_cousins', example.This_rule_base, 'how_related',
                how_related_removed_cousins, example.how_related_removed_cousins,
                (contexts.variable('removed_cousin1'),
                 contexts.variable('cousin2'),),
                ('r1', 'plan#3',),
                (contexts.variable('removed_cousin1'),
                 contexts.variable('cousin1'),
                 contexts.variable('grand'),
                 contexts.anonymous(),
                 contexts.variable('cousin2'),
                 contexts.variable('n'),
                 contexts.variable('plan#3'),
                 contexts.variable('r1'),))

def how_related_cousins_removed(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    if all(itertools.imap(lambda pat, arg:
                            pat.match_pattern(context, context,
                                              arg, arg_context),
                          patterns,
                          arg_patterns)):
      for x_1 in prove('example', 'cousins', context,
                     (rule.pattern(0),
                      rule.pattern(1),
                      rule.pattern(2),)):
        assert x_1 is None, \
          "%(rule_name)s: got unexpected plan from when clause 1"
        for x_2 in prove('example', 'child_parent', context,
                       (rule.pattern(3),
                        rule.pattern(1),
                        rule.pattern(4),
                        rule.pattern(5),
                        rule.pattern(5),)):
          assert x_2 is None, \
            "%(rule_name)s: got unexpected plan from when clause 2"
          for x_3 in prove('example', 'nth_cousin', context,
                         (rule.pattern(2),)):
            assert x_3 is not None, \
              "%(rule_name)s: expected plan from when clause 3"
            mark3 = context.mark(True)
            if not rule.pattern(6).match_data(context, context, x_3):
              raise AssertionError("%(rule_name)s: plan match to $plan#3 failed in when clause 3")
            context.end_save_all_undo()
            mark4 = context.mark(True)
            if rule.pattern(7).match_data(context, context,
                    len(context.lookup_data('grand')) + 1):
              context.end_save_all_undo()
              yield context
            else: context.end_save_all_undo()
            context.undo_to_mark(mark4)
            context.undo_to_mark(mark3)
    context.done()

bc_rule.bc_rule('how_related_cousins_removed', example.This_rule_base, 'how_related',
                how_related_cousins_removed, example.how_related_cousins_removed,
                (contexts.variable('cousin1'),
                 contexts.variable('removed_cousin2'),),
                ('r1', 'plan#3',),
                (contexts.variable('cousin1'),
                 contexts.variable('cousin2'),
                 contexts.variable('n'),
                 contexts.variable('removed_cousin2'),
                 contexts.variable('grand'),
                 contexts.anonymous(),
                 contexts.variable('plan#3'),
                 contexts.variable('r1'),))

def nth_cousin_1(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    if all(itertools.imap(lambda pat, arg:
                            pat.match_pattern(context, context,
                                              arg, arg_context),
                          patterns,
                          arg_patterns)):
      for x_1 in prove('special', 'cut', context,
                     ()):
        assert x_1 is None, \
          "%(rule_name)s: got unexpected plan from when clause 1"
        yield context
    context.done()

bc_rule.bc_rule('nth_cousin_1', example.This_rule_base, 'nth_cousin',
                nth_cousin_1, example.nth_cousin_1,
                (pattern.pattern_literal(1),),
                (),
                ())

def nth_cousin_2(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    if all(itertools.imap(lambda pat, arg:
                            pat.match_pattern(context, context,
                                              arg, arg_context),
                          patterns,
                          arg_patterns)):
      for x_1 in prove('special', 'cut', context,
                     ()):
        assert x_1 is None, \
          "%(rule_name)s: got unexpected plan from when clause 1"
        yield context
    context.done()

bc_rule.bc_rule('nth_cousin_2', example.This_rule_base, 'nth_cousin',
                nth_cousin_2, example.nth_cousin_2,
                (pattern.pattern_literal(2),),
                (),
                ())

def nth_cousin_3(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    if all(itertools.imap(lambda pat, arg:
                            pat.match_pattern(context, context,
                                              arg, arg_context),
                          patterns,
                          arg_patterns)):
      for x_1 in prove('special', 'cut', context,
                     ()):
        assert x_1 is None, \
          "%(rule_name)s: got unexpected plan from when clause 1"
        yield context
    context.done()

bc_rule.bc_rule('nth_cousin_3', example.This_rule_base, 'nth_cousin',
                nth_cousin_3, example.nth_cousin_3,
                (pattern.pattern_literal(3),),
                (),
                ())

def nth_cousin_rest(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    if all(itertools.imap(lambda pat, arg:
                            pat.match_pattern(context, context,
                                              arg, arg_context),
                          patterns,
                          arg_patterns)):
      yield context
    context.done()

bc_rule.bc_rule('nth_cousin_rest', example.This_rule_base, 'nth_cousin',
                nth_cousin_rest, example.nth_cousin_rest,
                (contexts.variable('n'),),
                ('n',),
                ())

def add_empty_prefix(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    if all(itertools.imap(lambda pat, arg:
                            pat.match_pattern(context, context,
                                              arg, arg_context),
                          patterns,
                          arg_patterns)):
      for x_1 in prove('special', 'cut', context,
                     ()):
        assert x_1 is None, \
          "%(rule_name)s: got unexpected plan from when clause 1"
        yield context
    context.done()

bc_rule.bc_rule('add_empty_prefix', example.This_rule_base, 'add_prefix',
                add_empty_prefix, example.add_empty_prefix,
                (pattern.pattern_literal(()),),
                (),
                ())

def add_prefix(rule, arg_patterns, arg_context):
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    if all(itertools.imap(lambda pat, arg:
                            pat.match_pattern(context, context,
                                              arg, arg_context),
                          patterns,
                          arg_patterns)):
      yield context
    context.done()

bc_rule.bc_rule('add_prefix', example.This_rule_base, 'add_prefix',
                add_prefix, example.add_prefix,
                (contexts.variable('prefix'),),
                ('prefix',),
                ())
