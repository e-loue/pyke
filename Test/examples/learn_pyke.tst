# learn_pyke.tst

    >>> import sys
    >>> import pyke
    >>> import os
    >>> new_path = os.path.join(os.path.dirname(os.path.dirname(pyke.__file__)),
    ...                         'examples/learn_pyke')
    >>> sys.path.append(new_path)

    >>> import driver
    >>> from StringIO import StringIO
    >>> import sys

    >>> sys.stdin = StringIO('8\n2\n2\n13\n')
    >>> driver.run()
    ______________________________________________________________________________
    Assume that the following two patterns are contained in different rules
    and that none of the pattern variables are initially bound to values:
    <BLANKLINE>
    pattern 1: ((ho, $_, ($a, $a)), ($a, $a, $b), ($a, *$b))
    pattern 2: ($a, $a, $x)
    <BLANKLINE>
    If the two patterns are matched together, what will $x be bound to?
      1. (a, b)
      2. $a
      3. ho
      4. ($a, *$b)
      5. (ho, *$b)
      6. (ho, *($a, $a))
      7. (ho, ($a, $a))
      8. (ho, $a, $a)
      9. (ho, *(ho, ho))
     10. (ho, (ho, ho))
     11. (ho, $_, (ho, ho))
     12. (ho, ho, (ho, ho))
     13. (ho, ho, ho)
     14. nothing, the two patterns don't match
     15. nothing, pattern 1 is not a legal pattern
     16. I don't have a clue...
    ? [1-16] Incorrect: Pattern variable '$a' is bound to a value.
    ______________________________________________________________________________
    "Rest" pattern variables are used at the end of a tuple pattern to match the
    rest of the tuple.
    <BLANKLINE>
    What is the syntax for a "rest" pattern variable?
      1. $rest
      2. _rest
      3. Preceding a pattern variable with an asterisk ('*'), like: *$foo.
    ? [1-3] Incorrect: A "rest" pattern variable is any pattern variable preceded
               by an asterisk ('*').
    ______________________________________________________________________________
    After matching the following two patterns, what is $c set to?
    <BLANKLINE>
    pattern 1: ($a, $b, *$c)
    pattern 2: (1, 2, 3)
      1. 3
      2. (3)
      3. (3,)
      4. nothing, the two patterns don't match
      5. nothing, pattern 1 is not a legal pattern
    ? [1-5] Correct!  (Note that a comma is not required for singleton tuples in PyKE).
    ______________________________________________________________________________
    Assume that the following two patterns are contained in different rules
    and that none of the pattern variables are initially bound to values:
    <BLANKLINE>
    pattern 1: ((ho, $_, ($a, $a)), ($a, $a, $b), ($a, *$b))
    pattern 2: ($a, $a, $x)
    <BLANKLINE>
    If the two patterns are matched together, what will $x be bound to?
      1. (a, b)
      2. $a
      3. ho
      4. ($a, *$b)
      5. (ho, *$b)
      6. (ho, *($a, $a))
      7. (ho, ($a, $a))
      8. (ho, $a, $a)
      9. (ho, *(ho, ho))
     10. (ho, (ho, ho))
     11. (ho, $_, (ho, ho))
     12. (ho, ho, (ho, ho))
     13. (ho, ho, ho)
     14. nothing, the two patterns don't match
     15. nothing, pattern 1 is not a legal pattern
     16. I don't have a clue...
    ? [1-16] Correct!
        matching Pattern 1: (ho, $_, ($a, $a))
              to Pattern 2: $a
           binds Pattern 2: $a to Pattern 1: (ho, $_, (ho, ho))
        matching Pattern 1: ($a, $a, $b)
              to Pattern 2: $a, which is bound to Pattern 1: (ho, $_, ($a, $a))
           binds Pattern 1: $a to ho,
             and Pattern 1: $b to Pattern 1: ($a, $a) which expands to (ho, ho)
        matching Pattern 1: ($a, *$b)
              to Pattern 2: $x
           binds Pattern 2: $x to Pattern 1: ($a, *$b) which expands to (ho, ho, ho)

