# findall.tst

    >>> import sys
    >>> import pyke
    >>> import os
    >>> new_path = os.path.join(os.path.dirname(os.path.dirname(pyke.__file__)),
    ...                         'examples/findall')
    >>> sys.path.append(new_path)

    >>> import run

    >>> run.fc_test()
    egon has ('harald', 'claudia') as cousins
    ralf has ('harald', 'claudia') as cousins
    hilde has () as cousins
    diethelm has () as cousins
    harald has ('egon', 'ralf') as cousins
    claudia has ('egon', 'ralf') as cousins

    >>> run.bc_test()
    egon has ('harald', 'claudia') as cousins
    ralf has ('harald', 'claudia') as cousins
    hilde has () as cousins
    diethelm has () as cousins
    harald has ('egon', 'ralf') as cousins
    claudia has ('egon', 'ralf') as cousins
