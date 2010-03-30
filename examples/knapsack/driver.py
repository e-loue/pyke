#!/usr/bin/python

# driver.py

from __future__ import with_statement
from pyke import knowledge_engine
from pyke import krb_traceback 

def run(pantry, capacity):
    engine = knowledge_engine.engine(__file__)
    engine.activate('knapsack')
    max = 0
    ans = None
    with engine.prove_goal(
           'knapsack.legal_knapsack($pantry, $capacity, $knapsack)',
           pantry=pantry,
           capacity=capacity) \
      as gen:
        for vars, no_plan in gen:
            knapsack = vars['knapsack']
            calories = sum(map(lambda x: x[2], knapsack))
            if calories > max:
                max = calories
                ans = knapsack
    return max, ans

if __name__ == "__main__":
    import sys
    print run(eval(sys.argv[1]), int(sys.argv[2]))
