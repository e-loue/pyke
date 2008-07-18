# foo.py

def gen2(n):
    try:
        for x in range(n):
            try:
                yield x
            finally:
                print "gen2 inner finally"
    except Exception, e:
        print "gen2 caught", repr(e)
    finally:
        print "gen2 finally"
    print "gen2 done"

def gen(n):
    try:
        for x in gen2(n):
            try:
                yield x
            finally:
                print "gen inner finally"
    except Exception, e:
        print "gen caught", repr(e)
    finally:
        print "gen finally"
    print "gen done"

def test1():
    try:
        for x in gen(2):
            print "test in for, doing: assert False"
            raise ValueError("this is a test")
        print "test after for"
    finally:
        print "test finally"

def test2():
    try:
        for x in gen(2):
            print "test in for, doing: break"
            break
        print "test after for"
    finally:
        print "test finally"
