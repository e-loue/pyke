# notany.tst

    >>> import sys
    >>> import pyke
    >>> import os
    >>> new_path = os.path.join(os.path.dirname(os.path.dirname(pyke.__file__)),
    ...                         'examples/notany')
    >>> sys.path.append(new_path)

    >>> import driver

    >>> driver.fc_test()
    egon has no uncle
    ralf has no uncle
    anton has no uncle
    elisabeth has no uncle
    karin has no uncle
    sabine has no uncle
    anton has no aunt
    elisabeth has no aunt
    karin has no aunt
    sabine has no aunt

    >>> driver.bc_test()
    anton has no aunt
    elisabeth has no aunt
    karin has no aunt
    sabine has no aunt
    egon has no uncle
    ralf has no uncle
    anton has no uncle
    elisabeth has no uncle
    karin has no uncle
    sabine has no uncle
