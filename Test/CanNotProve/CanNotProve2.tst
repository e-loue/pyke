# CanNotProve1.tst

We're going to create a zipped egg file with a compiled CanNotProve example in
it and see if pyke can load its compiled files from the zip file.


First, create the egg (in Test/dist) using Test/setup.py:

    >>> import os
    >>> os.chdir('..')  # up to Test directory

    >>> import sys
    >>> sys.argv = ['Test/setup.py', '--quiet', 'bdist_egg']
    >>> from Test import setup  # This runs setup.py

Now, move up another level (so that 'CanNotProve' is not a subdirectory)

    >>> os.chdir('..')  # up to root source directory

Add the egg to the python path:

    >>> import glob
    >>> sys.path.insert(0, glob.glob('Test/dist/CanNotProve*.egg')[0])

Now try the test!

    >>> from CanNotProve import test
    >>> test.__loader__         # doctest: +ELLIPSIS
    <zipimporter ...>
    >>> test.Rule_package = 'CanNotProve'
    >>> test.dotests()

And finally, delete the files created by Test/setup.py

    >>> def rm_r(dir):
    ...     for root, dirs, files in os.walk(dir, topdown=False):
    ...        for name in files:
    ...            os.remove(os.path.join(root, name))
    ...        for name in dirs:
    ...            os.rmdir(os.path.join(root, name))
    ...     os.rmdir(dir)
    >>> rm_r('Test/build')
    >>> rm_r('Test/dist')
    >>> rm_r('Test/CanNotProve.egg-info')

