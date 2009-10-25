# profile_server.py

import cProfile
import simple_server

def run(port=8080, logging=False, trace_sql=False, db_engine='sqlite3'):
    cProfile.runctx(
        'simple_server.run(port=%d, logging=%s, trace_sql=%s, db_engine=%r)'
            % (port, logging, trace_sql, db_engine),
        globals(), locals(), 'profile.out')

def stats():
    import pstats
    p = pstats.Stats('profile.out')
    p.sort_stats('time')
    p.print_stats(20)
