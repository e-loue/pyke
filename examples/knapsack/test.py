#!/usr/bin/python

# test.py

from __future__ import with_statement
from pyke import knowledge_engine
from pyke import krb_traceback 

def run(pantry, capacity):
    engine = knowledge_engine.engine('examples.knapsack')
    engine.activate('knapsack')
    max = 0
    ans = None
    with engine.prove_n('knapsack', 'legal_knapsack', (pantry, capacity), 1) \
      as gen:
        for (knapsack,), no_plan in gen:
            calories = sum(map(lambda x: x[2], knapsack))
            if calories > max:
                max = calories
                ans = knapsack
    return max, ans

if __name__ == "__main__":
    import sys
    print run(eval(sys.argv[1]), int(sys.argv[2]))
