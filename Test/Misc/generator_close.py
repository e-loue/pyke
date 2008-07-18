# generator_close.py

import sys

class Backup(Exception): pass

def gen1(name, n):
    try:
        try:
            for i in range(n): yield i
        except Exception, e:
            print "gen1(%s) => %s: %s" % (name, e.__class__.__name__, str(e))
            raise
    finally:
        print "gen1(%s) done" % name

def gen2(name):
    try:
        try:
            for i in gen1("first", 5):
                for j in gen_exception("second"): yield i, j
        except Exception, e:
            print "gen2(%s) => %s: %s" % (name, e.__class__.__name__, str(e))
            raise
    finally:
        print "gen2(%s) done" % name

def gen_exception(name):
    try:
        try:
            for i in gen1("inner", 5):
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

def test():
    for i, x in enumerate(gen2("top")):
        print "got", x
        if i == 3:
            print "test: raising exception"
            raise Backup("test: hello bob")
