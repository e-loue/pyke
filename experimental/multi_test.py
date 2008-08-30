# multi_test.py

class top(object):
    def foo(self, indent = 0):
        print ' ' * indent + "top.foo"
    def bar(self):
        print "top.bar"

class left(top):
    r'''
        >>> l = left()
        >>> l.foo()     # here left.foo calls top.foo
        left.foo
            top.foo
        >>> l.bar()
        top.bar
    '''
    def foo(self, indent = 0):
        print ' ' * indent + "left.foo"
        super(left, self).foo(indent + 4)

class right(top):
    r'''
        >>> r = right()
        >>> r.foo()
        right.foo
            top.foo
    '''
    def foo(self, indent = 0):
        print ' ' * indent + "right.foo"
        super(right, self).foo(indent + 4)
    def bar(self):
        print "right.bar"

class bottom(left, right):
    r'''
        >>> b = bottom()
        >>> b.foo()     # here left.foo calls right.foo
        bottom.foo
            left.foo
                right.foo
                    top.foo
        >>> b.bar()     # gets right.bar, not left->top.bar
        right.bar
    '''
    def foo(self, indent = 0):
        print ' ' * indent + "bottom.foo"
        super(bottom, self).foo(indent + 4)

def test():
    import sys
    import doctest
    sys.exit(doctest.testmod()[0])

if __name__ == "__main__":
    test()
