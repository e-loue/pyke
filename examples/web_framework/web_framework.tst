# web_framework.tst

First, fire up the server:

    >>> import sys
    >>> import os
    >>> import signal
    >>> import time
    >>> import subprocess
    >>> server = subprocess.Popen((sys.executable, "-i", "-u"),
    ...                           stdin=subprocess.PIPE,
    ...                           stdout=subprocess.PIPE,
    ...                           stderr=subprocess.STDOUT,
    ...                           close_fds=True, env=os.environ)
    >>> server.stdin.write(r'''
    ... print 'mom'
    ... import sys
    ... from examples.web_framework import simple_server
    ... print >> sys.stderr, 'dad'
    ... simple_server.run()
    ... ''')                            # doctest: +ELLIPSIS
    >>> #server.stdin.write("sys.path.insert(0, '')\n")
    >>> server.stdout.readline()        # doctest: +ELLIPSIS
    'Python ...\n'
    >>> server.stdout.readline()        # doctest: +ELLIPSIS
    '[...\n'
    >>> server.stdout.readline()        # doctest: +ELLIPSIS
    'Type ...\n'
    >>> server.stdout.readline()
    '>>> >>> mom\n'
    >>> server.stdout.readline()
    '>>> >>> >>> dad\n'
    >>> server.stdout.read(4)
    '>>> '
    >>> while True:
    ...     line = server.stdout.readline()
    ...     if not line.startswith('writing [examples.'):
    ...         break
    >>> line                            # doctest: +ELLIPSIS
    'Server running...\n'
    >>> time.sleep(0.8)

Then interact with it:

    >>> import urllib
    >>> def get(path):
    ...     f = urllib.urlopen("http://localhost:8080/" + path)
    ...     #print >> sys.stderr, "info:", tuple(sorted(f.info().keys()))
    ...     try:
    ...         return f.read() # int(f.info()['content-length']))
    ...     finally:
    ...         f.close()

    >>> print get("movie/1/movie.html")
    <html>
      <head>
        <title>It's a Mad, Mad, Mad, Mad World</title>
      </head>
      <body>
        <h1>It's a Mad, Mad, Mad, Mad World</h1>
        <h2>Year</h2>
          <p>1963</p>
        <h2>Length</h2>
          <p>3:12</p>
        <h2>Directors</h2>
        <ol>
          <li>Stanley Kramer
          </li>
        </ol>
      </body>
    </html>
    <BLANKLINE>

    >>> server.stdout.readline()        # doctest: +ELLIPSIS
    "get_plan(..., ('movie',), ...examples/web_framework/movie.html)\n"

    >>> server.stdout.readline()        # doctest: +ELLIPSIS
    'localhost - - [...] "GET /movie/1/movie.html HTTP/1.0" 200 302\n'

    >>> print get("movie/3/movie.html")
    <html>
      <head>
        <title>A Funny Thing Happened on the Way to the Forum</title>
      </head>
      <body>
        <h1>A Funny Thing Happened on the Way to the Forum</h1>
        <h2>Year</h2>
          <p>1966</p>
        <h2>Length</h2>
          <p>1:39</p>
        <h2>Directors</h2>
        <ol>
          <li>Richard Lester
          </li>
        </ol>
      </body>
    </html>
    <BLANKLINE>

    >>> server.stdout.readline()        # doctest: +ELLIPSIS
    'localhost - - [...] "GET /movie/3/movie.html HTTP/1.0" 200 332\n'

    >>> print get("movie/3/movie2.html")
    <html>
      <head>
        <title>A Funny Thing Happened on the Way to the Forum</title>
      </head>
      <body>
        <h1>A Funny Thing Happened on the Way to the Forum</h1>
        <h2>Year:</h2>
          <p>1966</p>
        <h2>Length:</h2>
          <p>1:39</p>
        <h2>Directors:</h2>
        <ol>
          <li>Richard Lester
          </li>
        </ol>
        <h2>DVD List:</h2>
        <ol>
          <li>102(1)
          </li>
    <li>105(1)
          </li>
        </ol>
      </body>
    </html>
    <BLANKLINE>

    >>> server.stdout.readline()        # doctest: +ELLIPSIS
    "get_plan(..., ('movie',), ...examples/web_framework/movie2.html)\n"

    >>> server.stdout.readline()        # doctest: +ELLIPSIS
    'localhost - - [...] "GET /movie/3/movie2.html HTTP/1.0" 200 429\n'

    >>> print get("movie/6/movie2.html")
    <html>
      <head>
        <title>Casino Royale</title>
      </head>
      <body>
        <h1>Casino Royale</h1>
        <h2>Year:</h2>
          <p>1967</p>
        <h2>Length:</h2>
          <p>2:11</p>
        <h2>Directors:</h2>
        <ol>
          <li>Val Guest
          </li>
    <li>Ken Hughes
          </li>
    <li>John Huston
          </li>
    <li>Joseph McGrath
          </li>
    <li>Robert Parrish
          </li>
    <li>Richard Talmadge
          </li>
        </ol>
        <h2>DVD List:</h2>
        <ol>
          <li>104(1)
          </li>
        </ol>
      </body>
    </html>
    <BLANKLINE>

    >>> server.stdout.readline()        # doctest: +ELLIPSIS
    'localhost - - [...] "GET /movie/6/movie2.html HTTP/1.0" 200 485\n'

Kill server:

    >>> time.sleep(0.4)
    >>> os.kill(server.pid, signal.SIGINT)
    >>> server.stdin.close()
    >>> server.wait()
    0
