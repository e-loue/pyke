# forall.tst

    >>> import sys
    >>> import pyke
    >>> import os
    >>> new_path = os.path.join(os.path.dirname(os.path.dirname(pyke.__file__)),
    ...                         'examples/forall')
    >>> sys.path.append(new_path)

    >>> import run

    >>> run.fc_test()
    arthur2 has no step brothers or sisters
    helen has no step brothers or sisters
    roberta has no step brothers or sisters

    >>> run.bc_test()
    arthur2
    helen
    roberta

