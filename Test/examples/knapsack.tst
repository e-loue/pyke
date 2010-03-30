# knapsack.tst

    >>> import sys
    >>> import pyke
    >>> import os
    >>> new_path = os.path.join(os.path.dirname(os.path.dirname(pyke.__file__)),
    ...                         'examples/knapsack')
    >>> sys.path.append(new_path)

    >>> import driver

    >>> driver.run((('bread', 4, 9200),
    ...          ('pasta', 2, 4500),
    ...          ('peanutButter', 1, 6700),
    ...          ('babyFood', 3, 6900)),
    ...         4)
    (13600, (('peanutButter', 1, 6700), ('babyFood', 3, 6900)))

