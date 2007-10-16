# example.py

from __future__ import with_statement, absolute_import, division
from pyke import contexts, pattern, fc_rule, rule_base
from pyke import lookup, assert_

This_rule_base = rule_base.rule_base('example')

def son_of(rule, context = None, index = None):
  if context is None: context = contexts.simple_context()
  for dummy in (None,) if index == 0 else \
               lookup('family', 'son_of', context, rule.foreach_patterns(0)):
    assert_('family', 'child_parent',
            (rule.pattern(0).as_data(context),
             rule.pattern(1).as_data(context),
             rule.pattern(2).as_data(context),
             rule.pattern(3).as_data(context),))
    assert_('family', 'child_parent',
            (rule.pattern(0).as_data(context),
             rule.pattern(4).as_data(context),
             rule.pattern(5).as_data(context),
             rule.pattern(3).as_data(context),))
  context.done()

fc_rule.fc_rule('son_of', This_rule_base, son_of,
  (('family', 'son_of',
    (contexts.variable('child'),
     contexts.variable('father'),
     contexts.variable('mother'),)),),
  (contexts.variable('child'),
   contexts.variable('father'),
   pattern.pattern_literal('father'),
   pattern.pattern_literal('son'),
   contexts.variable('mother'),
   pattern.pattern_literal('mother'),))

def daughter_of(rule, context = None, index = None):
  if context is None: context = contexts.simple_context()
  for dummy in (None,) if index == 0 else \
               lookup('family', 'daughter_of', context, rule.foreach_patterns(0)):
    assert_('family', 'child_parent',
            (rule.pattern(0).as_data(context),
             rule.pattern(1).as_data(context),
             rule.pattern(2).as_data(context),
             rule.pattern(3).as_data(context),))
    assert_('family', 'child_parent',
            (rule.pattern(0).as_data(context),
             rule.pattern(4).as_data(context),
             rule.pattern(5).as_data(context),
             rule.pattern(3).as_data(context),))
  context.done()

fc_rule.fc_rule('daughter_of', This_rule_base, daughter_of,
  (('family', 'daughter_of',
    (contexts.variable('child'),
     contexts.variable('father'),
     contexts.variable('mother'),)),),
  (contexts.variable('child'),
   contexts.variable('father'),
   pattern.pattern_literal('father'),
   pattern.pattern_literal('daughter'),
   contexts.variable('mother'),
   pattern.pattern_literal('mother'),))

def brothers(rule, context = None, index = None):
  if context is None: context = contexts.simple_context()
  for dummy in (None,) if index == 0 else \
               lookup('family', 'son_of', context, rule.foreach_patterns(0)):
    for dummy in (None,) if index == 1 else \
                 lookup('family', 'son_of', context, rule.foreach_patterns(1)):
      if context.lookup_data('brother1') != context.lookup_data('brother2'):
        assert_('family', 'siblings',
                (rule.pattern(0).as_data(context),
                 rule.pattern(1).as_data(context),
                 rule.pattern(2).as_data(context),
                 rule.pattern(2).as_data(context),))
  context.done()

fc_rule.fc_rule('brothers', This_rule_base, brothers,
  (('family', 'son_of',
    (contexts.variable('brother1'),
     contexts.variable('father'),
     contexts.variable('mother'),)),
   ('family', 'son_of',
    (contexts.variable('brother2'),
     contexts.variable('father'),
     contexts.variable('mother'),)),),
  (contexts.variable('brother1'),
   contexts.variable('brother2'),
   pattern.pattern_literal('brother'),))

def sisters(rule, context = None, index = None):
  if context is None: context = contexts.simple_context()
  for dummy in (None,) if index == 0 else \
               lookup('family', 'daughter_of', context, rule.foreach_patterns(0)):
    for dummy in (None,) if index == 1 else \
                 lookup('family', 'daughter_of', context, rule.foreach_patterns(1)):
      if context.lookup_data('sister1') != context.lookup_data('sister2'):
        assert_('family', 'siblings',
                (rule.pattern(0).as_data(context),
                 rule.pattern(1).as_data(context),
                 rule.pattern(2).as_data(context),
                 rule.pattern(2).as_data(context),))
  context.done()

fc_rule.fc_rule('sisters', This_rule_base, sisters,
  (('family', 'daughter_of',
    (contexts.variable('sister1'),
     contexts.variable('father'),
     contexts.variable('mother'),)),
   ('family', 'daughter_of',
    (contexts.variable('sister2'),
     contexts.variable('father'),
     contexts.variable('mother'),)),),
  (contexts.variable('sister1'),
   contexts.variable('sister2'),
   pattern.pattern_literal('sister'),))

def brother_and_sister(rule, context = None, index = None):
  if context is None: context = contexts.simple_context()
  for dummy in (None,) if index == 0 else \
               lookup('family', 'son_of', context, rule.foreach_patterns(0)):
    for dummy in (None,) if index == 1 else \
                 lookup('family', 'daughter_of', context, rule.foreach_patterns(1)):
      assert_('family', 'siblings',
              (rule.pattern(0).as_data(context),
               rule.pattern(1).as_data(context),
               rule.pattern(2).as_data(context),
               rule.pattern(3).as_data(context),))
      assert_('family', 'siblings',
              (rule.pattern(1).as_data(context),
               rule.pattern(0).as_data(context),
               rule.pattern(3).as_data(context),
               rule.pattern(2).as_data(context),))
  context.done()

fc_rule.fc_rule('brother_and_sister', This_rule_base, brother_and_sister,
  (('family', 'son_of',
    (contexts.variable('brother'),
     contexts.variable('father'),
     contexts.variable('mother'),)),
   ('family', 'daughter_of',
    (contexts.variable('sister'),
     contexts.variable('father'),
     contexts.variable('mother'),)),),
  (contexts.variable('brother'),
   contexts.variable('sister'),
   pattern.pattern_literal('sister'),
   pattern.pattern_literal('brother'),))

def facts_for_bc_rules(rule, context = None, index = None):
  if context is None: context = contexts.simple_context()
  assert_('family', 'as_au',
          (rule.pattern(0).as_data(context),
           rule.pattern(1).as_data(context),))
  assert_('family', 'as_au',
          (rule.pattern(2).as_data(context),
           rule.pattern(3).as_data(context),))
  assert_('family', 'as_nn',
          (rule.pattern(4).as_data(context),
           rule.pattern(5).as_data(context),))
  assert_('family', 'as_nn',
          (rule.pattern(6).as_data(context),
           rule.pattern(7).as_data(context),))
  context.done()

fc_rule.fc_rule('facts_for_bc_rules', This_rule_base, facts_for_bc_rules,
  (),
  (pattern.pattern_literal('brother'),
   pattern.pattern_literal('uncle'),
   pattern.pattern_literal('sister'),
   pattern.pattern_literal('aunt'),
   pattern.pattern_literal('son'),
   pattern.pattern_literal('nephew'),
   pattern.pattern_literal('daughter'),
   pattern.pattern_literal('niece'),))

def how_related_child_parent(context):
  return context['plan#2'](context['p2_type'], context['p1_type'])

def how_related_parent_child(context):
  return context['plan#2'](context['p2_type'], context['p1_type'])

def how_related_siblings(context):
  return context['p2_type'] + ' <=> ' + context['p1_type']

def how_related_nn_au(context):
  return context['plan#2'](context['p2_type'], context['p1_type'])

def how_related_au_nn(context):
  return context['plan#2'](context['p2_type'], context['p1_type'])

def how_related_cousins(context):
  return context['plan#2']()

def how_related_removed_cousins(context):
  nth_cousin = context['plan#3']()
  return "%s, %d removed" % (nth_cousin, context['r1'])

def how_related_cousins_removed(context):
  nth_cousin = context['plan#3']()
  return "%s, %d removed" % (nth_cousin, context['r1'])

def nth_cousin_1(context):
  return "1st cousins"

def nth_cousin_2(context):
  return "2nd cousins"

def nth_cousin_3(context):
  return "3rd cousins"

def nth_cousin_rest(context):
  return "%dth cousins" % context['n']

def add_empty_prefix(context, x, y):
  return x + ' <=> ' + y

def add_prefix(context, x, y):
  pre = ' '.join(context['prefix']) + ' '
  return pre + x + ' <=> ' + pre + y
