# generator_exception_propagation.py

import sys

class Backup(Exception): pass

class watch(object):
    def __init__(self, name, gen, *gen_args):
        self.name = name
        print "%s.__init__()" % self.name
        self.iterator = gen(*gen_args)
    def __iter__(self):
        print "%s.__iter__()" % self.name
        self.iterator_iter = iter(self.iterator)
        return self
    def __del__(self):
        print "%s.__del__()" % self.name
        del self.iterator
    def next(self):
        try:
            ans = self.iterator_iter.next()
        except Exception, e:
            print "%s.next() => %s: %s" % \
                  (self.name, e.__class__.__name__, str(e))
            raise
        print "%s.next() => %s" % (self.name, str(ans))
        return ans
    def throw(self, value=None, traceback=None):
        try:
            ans = self.iterator_iter.throw(value, traceback)
        except Exception, e:
            print "%s.throw(%s, %s) => %s: %s" % \
                  (self.name, str(value), "traceback" if traceback else None,
                   e.__class__.__name__, str(e))
            raise
        print "%s.throw(%s, %s) => %s" % \
              (self.name, str(value), "traceback" if traceback else None,
               str(ans))
        return ans
    def close(self):
        print "%s.close()" % self.name
        self.iterator_iter.close()

def gen1(name, gen, *args):
    try:
        try:
            for i in gen(*args): yield i
        except Exception, e:
            print "gen1(%s) => %s: %s" % (name, e.__class__.__name__, str(e))
            raise
    finally:
        print "gen1(%s) done" % name

def gen2(name, gen1, gen1_args, gen2, gen2_args):
    try:
        try:
            for i in gen1(*gen1_args):
                for j in gen2(*gen2_args): yield i, j
        except Exception, e:
            print "gen2(%s) => %s: %s" % (name, e.__class__.__name__, str(e))
            raise
    finally:
        print "gen2(%s) done" % name

def gen_exception(name, gen, *args):
    try:
        try:
            for i in gen(*args):
                if i == 2:
                    print "gen_exception(%s): raising exception" % name
                    raise Backup("gen_exception(%s): hello bob" % name)
                yield i
        except Exception, e:
            print "gen_exception(%s) => %s: %s" % \
                    (name, e.__class__.__name__, str(e))
            raise
    finally:
        print "gen_exception(%s) done" % name

def make_gen():
    return watch("top_gen",
                 gen2, "top_gen",
                       watch, ("first_gen", gen1, "first_gen", range, 1, 5),
                       watch, ("second_gen",
                               gen1, "second_gen",
                                     watch, "gen_exception",
                                            gen_exception, "gen_exception",
                                                watch, "range", range, 1, 5))

def test():
    for i, x in enumerate(make_gen()):
        print "got", x
        if i == 3:
            print "test: raising exception"
            raise Backup("test: hello bob")
