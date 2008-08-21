# metaclass.py

from pyke.unique import unique

class metaclass(type): # this _must_ be derived from 'type'!
    _ignore_setattr = False
    def __init__(self, name, bases, dict):
        # This gets called when new derived classes are created.
        #
        # We don't need to define an __init__ method here, but I was just
        # curious about how this thing works...
        print "metaclass: name", name, ", bases", bases, \
              ", dict keys", tuple(sorted(dict.keys()))
        super(metaclass, self).__init__(name, bases, dict)
    def __call__(self, *args, **kws):
        # This gets called when new instances are created (using the class as
        # a function).
        obj = super(metaclass, self).__call__(*args, **kws)
        del obj._ignore_setattr
        print "add instance", obj, "to", self.knowledge_base
        return obj

class tracked_object(object):
    r'''
        All classes to be tracked by an object base would be derived from this
        one:

        >>> class foo(tracked_object):
        ...     def __init__(self, arg):
        ...         super(foo, self).__init__()
        ...         print "foo.__init__:", arg
        ...         self.x = arg    # should be ignored
        metaclass: name foo , bases (<class '__main__.tracked_object'>,) ,
        dict keys ('__init__', '__module__')


        And we can keep deriving classes:

        >>> class bar(foo):
        ...     def __init__(self, arg1, arg2):
        ...         super(bar, self).__init__(arg1)
        ...         print "bar.__init__:", arg1, arg2
        ...         self.y = arg2    # should be ignored
        metaclass: name bar , bases (<class '__main__.foo'>,) ,
        dict keys ('__init__', '__module__')


        We can't do the next step directly in the class definition because the
        knowledge_engine.engine hasn't been created yet and so the object
        bases don't exist at that point in time.

        So this simulates adding the knowledge_base to the class later, after
        the knowledge_engine.engine and object bases have been created.

        >>> foo.knowledge_base = 'foo base'
        >>> bar.knowledge_base = 'bar base'


        And now we create some instances (shouldn't see any attribute change
        notifications here!):

        >>> f = foo(44)
        foo.__init__: 44
        add instance <__main__.foo object at 0x...> to foo base
        >>> b = bar(55, 66)
        foo.__init__: 55
        bar.__init__: 55 66
        add instance <__main__.bar object at 0x...> to bar base


        And modify some attributes:

        >>> f.x = 'y'
        notify foo base of attribute change:
        (<__main__.foo object at 0x...>, x, y)
        >>> b.y = 'z'
        notify bar base of attribute change:
        (<__main__.bar object at 0x...>, y, z)
        >>> b.y = 'z' # should be ignored
        >>> b.z = "wasn't set"
        notify bar base of attribute change:
        (<__main__.bar object at 0x...>, z, wasn't set)

    '''
    __metaclass__ = metaclass
    _not_bound = unique('_not_bound') # a value that should != any other value!
    def __init__(self):
        self._ignore_setattr = True
    def __setattr__(self, attr, value):
        # This gets called when any attribute is changed.  We would need to
        # figure out how to ignore attribute setting by the __init__
        # function...
        #
        # Also the check to see if the attribute has actually changed by doing
        # a '!=' check could theoretically lead to problems.  For example this
        # would fail to change the attribute to another value that wasn't
        # identical to the first, but '==' to it: for example, 4 and 4.0.
        if getattr(self, attr, self._not_bound) != value:
            super(tracked_object, self).__setattr__(attr, value)
            if not hasattr(self, '_ignore_setattr'):
                print "notify", self.knowledge_base, \
                      "of attribute change: (%s, %s, %s)" % (self, attr, value)

def test():
    import sys
    import doctest
    sys.exit(doctest.testmod(optionflags = doctest.ELLIPSIS
                                         | doctest.NORMALIZE_WHITESPACE)
                            [0])

if __name__ == "__main__":
    test()
