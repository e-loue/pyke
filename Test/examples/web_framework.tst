# web_framework.tst

    >>> import sys
    >>> import pyke
    >>> import os
    >>> source_dir = os.path.dirname(os.path.dirname(pyke.__file__))
    >>> new_path = os.path.join(source_dir, 'examples')
    >>> sys.path.append(new_path)

First, fire up the server:

    >>> import sys
    >>> import os
    >>> import signal
    >>> import time
    >>> import subprocess
    >>> server = subprocess.Popen((sys.executable, "-u", "-"),
    ...                           stdin=subprocess.PIPE,
    ...                           stdout=subprocess.PIPE,
    ...                           stderr=subprocess.STDOUT,
    ...                           close_fds=True, env=os.environ)
    >>> server.stdin.write(r'''
    ... import sys
    ... sys.path.append(%r)
    ... sys.path.append(%r)
    ... from web_framework import simple_server
    ... simple_server.run()
    ... ''' % (new_path, source_dir))
    >>> server.stdin.close()
    >>> def readline():
    ...     global server_error_msg
    ...     if server.poll() is not None:
    ...         msg = server.stdout.read()
    ...         if msg:
    ...             server_error_msg = '\n'.join(('server: ' + line)
    ...                                          for line in msg.split('\n'))
    ...         sys.stdout.write(server_error_msg)
    ...         sys.stdout.write(
    ...           "Server terminated prematurely with returncode %r\n" % \
    ...             (server.returncode,))
    ...         return
    ...     line = server.stdout.readline()
    ...     print >> sys.stderr, line,
    ...     return line
    >>> while True:
    ...     line = readline()
    ...     if not line.startswith('writing ['):
    ...         break
    >>> line
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

    >>> readline()        # doctest: +ELLIPSIS
    "get_plan(..., ('movie',), ...examples/web_framework/movie.html)\n"
    >>> readline()        # doctest: +ELLIPSIS
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

    >>> readline()        # doctest: +ELLIPSIS
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

    >>> readline()        # doctest: +ELLIPSIS
    "get_plan(..., ('movie',), ...examples/web_framework/movie2.html)\n"
    >>> readline()        # doctest: +ELLIPSIS
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

    >>> readline()        # doctest: +ELLIPSIS
    'localhost - - [...] "GET /movie/6/movie2.html HTTP/1.0" 200 485\n'

Kill server:

    >>> time.sleep(0.4)
    >>> os.kill(server.pid, signal.SIGTERM)
    >>> server.wait()
    -15
