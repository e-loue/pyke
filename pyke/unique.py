# unique.py

from __future__ import with_statement, absolute_import, division

class unique(object):
    def __init__(self, name): self.name = name
    def __repr__(self): return "<unique %s>" % self.name

def test():
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
