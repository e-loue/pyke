# tmp_itertools.py

''' This is a placeholder until the standard python itertools changes its
'chain' function to take a single argument (like this one here).
'''

import itertools

def chain(iterables):
    for iterable in iterables:
        for x in iterable: yield x

count = itertools.count
cycle = itertools.cycle
dropwhile = itertools.dropwhile
groupby = itertools.groupby
ifilterfalse = itertools.ifilterfalse
ifilter = itertools.ifilter
imap = itertools.imap
islice = itertools.islice
izip = itertools.izip
repeat = itertools.repeat
starmap = itertools.starmap
takewhile = itertools.takewhile
tee = itertools.tee
