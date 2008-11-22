# CanNotProve.tst

r"""

    >>> import test
    >>> test.dotests()

"""

def test():
    import sys
    import doctest
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__": test()
