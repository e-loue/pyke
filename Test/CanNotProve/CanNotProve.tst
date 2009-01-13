# CanNotProve.tst

r"""

    >>> from Test.CanNotProve import test
    >>> test.dotests()

"""

def test():
    import sys
    import doctest
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__": test()
