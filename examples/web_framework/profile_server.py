# profile_server.py

import cProfile
import pstats
import simple_server

def run(port=8080, logging=False):
    cProfile.runctx('simple_server.run(port=%d, logging=%s)' % (port, logging),
                    globals(), locals(), 'profile.out')

def stats():
    p = pstats.Stats('profile.out')
    p.sort_stats('time')
    p.print_stats(20)
