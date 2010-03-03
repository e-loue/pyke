# CanNotProve2.tst

We're going to create a zipped egg file with a compiled CanNotProve example in
it and see if pyke can load its compiled files from the zip file.


First, create the egg (in Test/dist) using Test/setup.py:

    >>> import os
    >>> os.chdir('..')  # up to Test directory

    >>> import contextlib
    >>> import zipfile
    >>> with contextlib.closing(zipfile.PyZipFile('CanNotProve.egg', 'w')) as z:
    ...     z.writepy('CanNotProve')
    ...     z.write('CanNotProve/compiled_krb/facts.fbc')

Now, move up another level (so that 'CanNotProve' is not a subdirectory)

    >>> os.chdir('..')  # up to root source directory

Add the egg to the python path:

    >>> import sys
    >>> sys.path.insert(0, 'Test/CanNotProve.egg')

Now try the test!

    >>> from CanNotProve import test
    >>> test.__loader__         # doctest: +ELLIPSIS
    <zipimporter ...>
    >>> test.dotests()

And finally, delete the egg file:

    >>> os.remove('Test/CanNotProve.egg')

