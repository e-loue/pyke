#!/usr/bin/env python

# get_links.py

from __future__ import with_statement
import os
import os.path

def run_command(start_dir, outfilename):
    dir = start_dir

    links_seen = set()

    def doctor(link_dir, path):
        # Don't mess with paths that just refer to another link:
        if path.rstrip()[-1] == '_': return path

        path = path.lstrip()

        # Don't mess with paths that point somewhere in the outside universe:
        if path.startswith('http://'): return ' ' + path

        # Prepend link_dir to path
        if link_dir.startswith('./'): path = link_dir[2:] + '/' + path
        elif link_dir != '.': path = link_dir + '/' + path

        # Prepare dir (start_dir, minus initial './')
        if start_dir == '.': dir = ''
        elif start_dir.startswith('./'): dir = start_dir[2:]
        else: dir = start_dir

        rest=' '
        last_dir = None
        while dir and dir != last_dir:
            if path.startswith(dir + '/'):
                ans = rest + path[len(dir) + 1:]
                #print "doctor(%s) abbr:" % (path.rstrip(),), ans
                return ans
            rest += '../'
            last_dir = dir
            dir, ignore = os.path.split(dir)
        ans = rest + path
        #print "doctor(%s) abs:" % (path.rstrip(),), ans
        return ans

    with open(outfilename, "w") as outfile:
        outfile.write("\n")
        while True:
            try:
                with open(os.path.join(dir, 'links')) as links:
                    for line in links:
                        link, path = line.split(':', 1)
                        if link not in links_seen:
                            links_seen.add(link)
                            outfile.write(":".join((link, doctor(dir, path))))
            except IOError:
                pass
            if dir == '.': break
            dir = os.path.dirname(dir)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print >> sys.stderr, "usage: get_links.py dir outfile"
        sys.exit(2)
    run_command(sys.argv[1], sys.argv[2])

