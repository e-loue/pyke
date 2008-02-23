# immutable_dict.py

class immutable_dict(dict):
    ''' >>> im = immutable_dict((('a', 1), ('b', 2)))
        >>> len(im)
        2
        >>> im['a']
        1
        >>> im['b']
        2
        >>> tuple(sorted(im.keys()))
        ('a', 'b')
        >>> tuple(sorted(im.values()))
        (1, 2)
        >>> 'a' in im
        True
        >>> 'c' in im
        False
        >>> del im['a']
        Traceback (most recent call last):
            ...
        TypeError: del (a) not allowed on plan context
        >>> im['a'] = 3
        Traceback (most recent call last):
            ...
        TypeError: not allowed to change pattern variables (a) in plan
        >>> im.clear()
        Traceback (most recent call last):
            ...
        TypeError: clear not allowed on plan context
        >>> im.pop('a')
        Traceback (most recent call last):
            ...
        TypeError: pop (a) not allowed on plan context
        >>> im.popitem()
        Traceback (most recent call last):
            ...
        TypeError: popitem not allowed on plan context
        >>> im.setdefault('a', [])
        Traceback (most recent call last):
            ...
        TypeError: setdefault (a) not allowed on plan context
        >>> im.update({'c': 3})
        Traceback (most recent call last):
            ...
        TypeError: update not allowed on plan context
    '''
    def __delitem__(self, key):
        raise TypeError("del (%s) not allowed on plan context" % key)
    def __setitem__(self, key, value):
        raise TypeError("not allowed to change pattern variables (%s) in plan" %
                            key)
    def clear(self):
        raise TypeError("clear not allowed on plan context")
    def pop(self, key, default = None):
        raise TypeError("pop (%s) not allowed on plan context" % key)
    def popitem(self):
        raise TypeError("popitem not allowed on plan context")
    def setdefault(self, key, default = None):
        raise TypeError("setdefault (%s) not allowed on plan context" % key)
    def update(self, dict2 = None, **kwargs):
        raise TypeError("update not allowed on plan context")

def test():
    import doctest
    import sys
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
