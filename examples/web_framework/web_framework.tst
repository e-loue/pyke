# web_framework.tst

First, fire up the server:

    >>> import sys
    >>> import os
    >>> import signal
    >>> import time
    >>> import subprocess
    >>> server = subprocess.Popen(("python2.5", "-i"),
    ...                           stdin=subprocess.PIPE,
    ...                           stdout=subprocess.PIPE,
    ...                           stderr=subprocess.PIPE,
    ...                           close_fds=True, env=os.environ)
    >>> server.stderr.readline()        # doctest: +ELLIPSIS
    'Python ...\n'
    >>> server.stderr.readline()        # doctest: +ELLIPSIS
    '[...\n'
    >>> server.stderr.readline()        # doctest: +ELLIPSIS
    'Type ...\n'
    >>> server.stderr.read(4)
    '>>> '
    >>> server.stdin.write("print 'mom'\n")
    >>> server.stdout.readline()
    'mom\n'
    >>> server.stderr.read(4)
    '>>> '
    >>> server.stdin.write("import sys\n")
    >>> server.stderr.read(4)
    '>>> '
    >>> server.stdin.write("sys.path.insert(0, '')\n")
    >>> server.stderr.read(4)
    '>>> '
    >>> server.stdin.write("import simple_server\n")
    >>> server.stderr.read(4)
    '>>> '
    >>> server.stdin.write("print 'dad'\n")
    >>> server.stdout.readline()
    'dad\n'
    >>> server.stderr.read(4)
    '>>> '
    >>> server.stdin.write("simple_server.run()\n")
    >>> time.sleep(0.4)

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
          <p>3:12:00</p>
        <h2>Directors</h2>
        <ol>
          <li>Stanley Kramer
          </li>
        </ol>
      </body>
    </html>
    <BLANKLINE>

    #>>> server.stderr.readline()        # doctest: +ELLIPSIS
    #'localhost - - [...] "GET /movie/1/movie.html HTTP/1.0" 200 305\n'

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
          <p>1:39:00</p>
        <h2>Directors</h2>
        <ol>
          <li>Richard Lester
          </li>
        </ol>
      </body>
    </html>
    <BLANKLINE>

    #>>> server.stderr.readline()        # doctest: +ELLIPSIS
    #'localhost - - [...] "GET /movie/3/movie.html HTTP/1.0" 200 335\n'

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
          <p>1:39:00</p>
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

    #>>> server.stderr.readline()        # doctest: +ELLIPSIS
    #'localhost - - [...] "GET /movie/3/movie2.html HTTP/1.0" 200 432\n'

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
          <p>2:11:00</p>
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

    #>>> server.stderr.readline()        # doctest: +ELLIPSIS
    #'localhost - - [...] "GET /movie/6/movie2.html HTTP/1.0" 200 488\n'

Kill server:

    >>> time.sleep(0.4)
    >>> os.kill(server.pid, signal.SIGINT)
    >>> server.stdin.close()
    >>> server.wait()
    0
