
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
