# generator_exception_propagation.py

class Backup(Exception): pass

class watch(object):
    def __init__(self, name, iterator):
        self.name = name
        self.iterator = iterator
    def __iter__(self):
        print "%s.__iter__()" % self.name
        self.iterator_iter = iter(self.iterator)
        return self
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

def gen1(a):
    try:
        for i in a: yield i
    except Exception, e:
        print "gen1 => %s: %s" % (e.__class__.__name__, str(e))
        raise

def gen2(a, b):
    try:
        for i in a:
            for j in b: yield i, j
    except Exception, e:
        print "gen2 => %s: %s" % (e.__class__.__name__, str(e))
        raise

def gen_exception(a):
    try:
        for i in a:
            if i == 2:
                print "gen_exception: raising exception"
                raise Backup("gen_exception: hello bob")
            yield i
    except Exception, e:
        print "gen_exception => %s: %s" % (e.__class__.__name__, str(e))
        raise

def test():
    for i, x in \
        enumerate(watch("top-gen",
                        gen2(watch("first-gen", range(1, 5)),
                             watch("second-gen",
                                   gen1(watch("gen_exception",
                                              gen_exception(watch("range",
                                                                  range(1,5)))))
                                  )))):
        print "got", x
        if i == 3:
            print "test: raising exception"
            raise Backup("test: hello bob")
