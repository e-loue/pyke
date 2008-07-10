# backup.tst

r"""

    >>> import test
    >>> test.test()
    Traceback (most recent call last):
        ...
    KeyError: '$ans_0 not bound'

"""

def test():
    import sys
    import doctest
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__": test()
