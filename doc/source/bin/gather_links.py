# gather_links.py

from __future__ import with_statement
import re
import os.path

ok1 = re.compile(r'\.\. +_[^:]+: *([^ `]+|[^ ].*_) *$')
ok2 = re.compile(r'\.\. +_[^:]+: *$')
ok3 = re.compile(r'  *[^ ]+$')

split_ref = re.compile(r'(\.\. +_[^:]+: *)([^ `]+|[^ ].*_) *$')

def run_command(args):
    for filename in args:
        dir, base = os.path.split(filename)
        if dir.startswith('./'): dir = dir[2:]
        if dir == '.': dir = ''
        print "dir:", dir, "base:", base
        ans = []
        gathering = False
        need_continuation = False
        with open(filename) as f:
            for line in f:
                line = line.rstrip()
                if need_continuation:
                    need_continuation = False
                    if ok3.match(line):
                        #print "ok3, line:", line
                        ans[-1] += ' ' + line.lstrip()
                    else:
                        #print "no continuation for:", ans[-1], "line:", line
                        ans = []
                        gathering = False
                elif ok1.match(line):
                    #print "ok1, line:", line
                    gathering = True
                    ans.append(line)
                elif ok2.match(line):
                    #print "ok2, line:", line
                    gathering = True
                    ans.append(line)
                    need_continuation = True
                elif gathering:
                    #print "nope!, line:", line
                    #for line in ans: print "dumping:", line
                    ans = []
                    gathering = False
        for line in ans:
            match = split_ref.match(line)
            if not match:
                print "split_ref failed on:", line
            else:
                ref, link = match.groups()
                if link[-1] == '_': print line
                elif link.startswith('http://'): print line
                else:
                    print ref.rstrip(), os.path.normpath(os.path.join(dir, link))

if __name__ == "__main__":
    import sys
    run_command(sys.argv[1:])
