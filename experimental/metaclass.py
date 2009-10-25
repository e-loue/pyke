# metaclass.py

from pyke.unique import unique

''' 
this metaclass is intended to be used by deriving from tracked_object as base class

pros:
- probably works with IronPython or Jython
- easier to understand

cons:
- __setattr__ defined by classes poses problems

'''
class metaclass_option1(type): # this _must_ be derived from 'type'!
    _ignore_setattr = False
    def __init__(self, name, bases, dict):
        # This gets called when new derived classes are created.
        #
        # We don't need to define an __init__ method here, but I was just
        # curious about how this thing works...
        print "metaclass: name", name, ", bases", bases, \
              ", dict keys", tuple(sorted(dict.keys()))
        super(metaclass_option1, self).__init__(name, bases, dict)
        
    def __call__(self, *args, **kws):
        # This gets called when new instances are created (using the class as
        # a function).
        obj = super(metaclass_option1, self).__call__(*args, **kws)
        del obj._ignore_setattr
        print "add instance", obj, "to", self.knowledge_base
        return obj


''' 
this metaclass requires the __metaclass__ = metaclass_option2 attribute of
classes to be used with the object knowledge base of pyke

pros:
- solves the problem of classes defining their own __setattr__ method
- does not require any multiple inheritance

cons:
- hard to understand
- possibly does not work with IronPython or Jython
 
'''
class metaclass_option2(type): # this _must_ be derived from 'type'!

    def __new__(mcl, name, bases, clsdict):
 
        print "metaclass_option2.__new__: class dict before __new__: name", name, ", bases", bases, \
              ", dict keys", tuple(clsdict.keys()), ", dict values", tuple(clsdict.values())
        
        def __setattr__(self, attr, value):
            # This gets called when any attribute is changed.  We would need to
            # figure out how to ignore attribute setting by the __init__
            # function...
            #
            # Also the check to see if the attribute has actually changed by doing
            # a '!=' check could theoretically lead to problems.  For example this
            # would fail to change the attribute to another value that wasn't
            # identical to the first, but '==' to it: for example, 4 and 4.0.
            if self.__instance__.get(self, False) :
                if getattr(self, attr) != value:                    
                    print "metaclass.__new__: notify knowledge base", \
                          "of attribute change: (%s, %s, %s)" % (self, attr, value)
                                        
                    if self.__cls__setattr__ != None:
                        self.__cls__setattr__(attr, value)
                    else:
                        super(self.__class__, self).__setattr__(attr, value)

            else:
                # does not work to call super.__setattr__
                #super(self.__class__, self).__setattr__(attr, value)
                #
                self.__dict__[attr] = value

        def __getattr__(self, name):
            return self.__dict__[name]

        cls__setattr__ = None
        if clsdict.get('__setattr__', None) != None:
            cls__setattr__ = clsdict['__setattr__']
                        
        clsdict['__setattr__'] = __setattr__
        clsdict['__getattr__'] = __getattr__
        clsdict['__cls__setattr__'] = cls__setattr__
        clsdict['__instance__'] = {}    
        
        print "metaclass_option2.__new__: class dict after __new__: name", name, ", bases", bases, \
              ", dict keys", tuple(sorted(clsdict.keys())), ", dict values", tuple(clsdict.values())
     
        return super(metaclass_option2, mcl).__new__(mcl, name, bases, clsdict)
    

    '''
    def __init__(cls, name, bases, clsdict):
        # This gets called when new derived classes are created.
        #
        # We don't need to define an __init__ method here, but I was just
        # curious about how this thing works...    
        super(metaclass_option2, cls).__init__(name, bases, clsdict)
        
        print "class dict after __init__: name", name, ", bases", bases, \
              ", dict keys", tuple(sorted(clsdict.keys()))

        # does not work to create __instance class member here            
        #clsdict['__instance__'] = {}
    '''
            
    def __call__(cls, *args, **kws):
        # This gets called when new instances are created (using the class as
        # a function).
        obj = super(metaclass_option2, cls).__call__(*args, **kws)
        
        obj.__instance__[obj] = True
               
        print "add instance of class", cls.__name__, "to knowledge base"        
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
        ... # doctest: +NORMALIZE_WHITESPACE
        metaclass: name foo , bases (<class 'experimental.metaclass.tracked_object'>,) ,
        dict keys ('__init__', '__module__')
    
    
        And we can keep deriving classes:
    
        >>> class bar(foo):
        ...     def __init__(self, arg1, arg2):
        ...         super(bar, self).__init__(arg1)
        ...         print "bar.__init__:", arg1, arg2
        ...         self.y = arg2    # should be ignored
        ... # doctest: +NORMALIZE_WHITESPACE
        metaclass: name bar , bases (<class 'experimental.metaclass.foo'>,) ,
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
    
        >>> f = foo(44)             # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
        tracked_object.__setattr__ called on object
          <experimental.metaclass.foo object at 0x...>
          with property _ignore_setattr and value True
        tracked_object.__setattr__ called on object
          <experimental.metaclass.foo object at 0x...>
          with property knowledgebase and value None
        foo.__init__: 44
        tracked_object.__setattr__ called on object
          <experimental.metaclass.foo object at 0x...>
          with property x and value 44
        add instance <experimental.metaclass.foo object at 0x...> to foo base
        >>> b = bar(55, 66)         # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
        tracked_object.__setattr__ called on object
          <experimental.metaclass.bar object at 0x...>
          with property _ignore_setattr and value True
        tracked_object.__setattr__ called on object
          <experimental.metaclass.bar object at 0x...>
          with property knowledgebase and value None
        foo.__init__: 55
        tracked_object.__setattr__ called on object
          <experimental.metaclass.bar object at 0x...>
          with property x and value 55
        bar.__init__: 55 66
        tracked_object.__setattr__ called on object
          <experimental.metaclass.bar object at 0x...>
          with property y and value 66
        add instance <experimental.metaclass.bar object at 0x...> to bar base
    
    
        And modify some attributes:
    
        >>> f.x = 'y'          # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
        tracked_object.__setattr__ called on object
          <experimental.metaclass.foo object at 0x...>
          with property x and value y
        tracked_object.__setattr__: notify foo base of attribute change:
          (<experimental.metaclass.foo object at 0x...>, x, y)
        >>> b.y = 'z'          # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
        tracked_object.__setattr__ called on object
          <experimental.metaclass.bar object at 0x...>
          with property y and value z
        tracked_object.__setattr__: notify bar base of attribute change:
          (<experimental.metaclass.bar object at 0x...>, y, z)
        >>> b.y = 'z' # should be ignored
        ...    # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
        tracked_object.__setattr__ called on object
          <experimental.metaclass.bar object at 0x...>
          with property y and value z
        >>> b.z = "wasn't set" # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
        tracked_object.__setattr__ called on object
          <experimental.metaclass.bar object at 0x...>
          with property z and value wasn't set
        tracked_object.__setattr__: notify bar base of attribute change:
          (<experimental.metaclass.bar object at 0x...>, z, wasn't set)
    
    '''
    __metaclass__ = metaclass_option1
    _not_bound = unique('_not_bound') # a value that should != any other value!
    def __init__(self):
        self._ignore_setattr = True
        self.knowledgebase = None
        
    def __setattr__(self, attr, value):
        # This gets called when any attribute is changed.  We would need to
        # figure out how to ignore attribute setting by the __init__
        # function...
        #
        # Also the check to see if the attribute has actually changed by doing
        # a '!=' check could theoretically lead to problems.  For example this
        # would fail to change the attribute to another value that wasn't
        # identical to the first, but '==' to it: for example, 4 and 4.0.
        print "tracked_object.__setattr__ called on object %s with property %s and value %s" % (self, attr, value)
        if getattr(self, attr, self._not_bound) != value:
            super(tracked_object, self).__setattr__(attr, value)
            if not hasattr(self, '_ignore_setattr'):
                print "tracked_object.__setattr__: notify", self.knowledge_base, \
                      "of attribute change: (%s, %s, %s)" % (self, attr, value)


''' tracked_object and foo_tracked use metaclass_option1
''' 
class foo_tracked(tracked_object):
     def __init__(self, arg):
         super(foo_tracked, self).__init__()         
         self.prop = arg


''' the following classes use metaclass_option2
'''   
class foo_base(object):    
    def __setattr__(self, attr, value):
        print "foo_base.__setattr__ called on object %s with property %s and value %s" % (self, attr, value)
   

class foo_attribute_base(foo_base):
    __metaclass__ = metaclass_option2
    
    def __init__(self, arg):
        super(foo_attribute_base, self).__init__()         
        self.prop = arg

  
class foo_attribute(object):
    __metaclass__ = metaclass_option2
    
    def __init__(self, arg):
        super(foo_attribute, self).__init__()         
        self.prop = arg
         
    def __setattr__(self, attr, value):
        print "foo_attribute.__setattr__ called on object %s with property %s and value %s" % (self, attr, value)
   
                      
class foo(object):
     __metaclass__ = metaclass_option2
     
     def __init__(self, arg):
         super(foo, self).__init__()         
         self.prop = arg
         
         #self.knowledge_base = "foo"
         
     def foo_method(self):
        print "foo_method called"

def test_foo_option2():
    f1 = foo(1) # should add instance to knowledge base
    f1.prop = 2 # should notify knowledge base of property change
    
    f2 = foo("egon")  # should add instance to knowledge base
    f2.prop = "ralf"  # should notify knowledge base of property change

    f3 = foo_attribute(3)
    f3.prop = 4
    
    f4 = foo_attribute("karin")
    f4.prop = "sabine"
    
    f5 = foo_attribute_base(5)
    f5.prop = 6
    
    f6 = foo_attribute_base("sebastian")
    f6.prop = "philipp"

    
def test_foo_option1():
    import sys
    import doctest
    sys.exit(doctest.testmod(optionflags = doctest.ELLIPSIS
                                         | doctest.NORMALIZE_WHITESPACE)
                            [0])

if __name__ == "__main__":
    #test_foo_option1()
    test_foo_option2()
