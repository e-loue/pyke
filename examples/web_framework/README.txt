This example automatically generates programs to render HTMLTemplates
(http://py-templates.sourceforge.net/htmltemplate/index.html).  You can use
pip or easy_install to install the HTMLTemplate package.

It uses the sqlgen example on the back-end to generate and run SQL statements.
You'll need to first set up the sqlgen example database before using this
example.  Check there for the movie_db schema.

This is also an example of using multiple rule bases (its own rule base, and
the sqlgen/database.krb rule base).

This example also caches the plans returned from pyke so it is extremely fast.
In fact, in siege tests compared to this same example running in
TurboGears 2.0, this web framework is a full 10 times faster than TurboGears!

To run this example, you need to be in the examples directory, then:

    >>> from web_framework import simple_server
    >>> simple_server.run()

Then point your browser at:

    http://localhost:8080/movie/1/movie.html

The "movie/1" says that you're starting with a unique row (id of 1) in the
"movie" table.  The "movie.html" is the name of the HTMLTemplate file you want
to use.  You may specify multiple unique starting tables by pairing the table
name with the id value: "/movie/1/genre/2/movie.html", though this doesn't
make much sense with the example templates...

web.krb
    This uses backward-chaining to build a program to fill an HTMLTemplate.

    The top-level goal is:

        process($starting_tables, $template_name)
        taking (db_cursor, starting_keys)

    The plan returned from this goal returns a three tuple:

        http_status, header_list, html_document

wsgi_app.py
    The WSGI front-end that drives pyke and executes the resulting plans.
    This parses the path from the WSGI environ and creates a plan for the
    combination of starting_tables and template_file, if one hasn't already
    been created by an earlier request, or if the template_file has been
    modified since the last plan for it was created.

    To create the plan, it establishes some of the interesting values in its
    environ as facts, then does the "process" goal above.
    
    The plan returned is run with the specific key to produce the WSGI output.

    To echo all sql statements to stderr, set the TRACE_SQL environment
    variable to something other than False prior to executing python. 

simple_server.py
    This is just a simple driver to run the wsgi_app as a local http server
    (default port 8080).  The 'run' function takes two optional arguments:
    port=8080 and logging=True.  Pass logging=False to disable logging
    requests to stderr (e.g., for performance measurement).

test.py
    This is a test driver to let you type goals in and run them to debug the
    rules.

    Test functions:

        init()
            Creates a pyke engine and calls load_mysql_schema.load_schema.
        run()
            Loops on "goal: " prompt.  Type a goal, or trace/untrace rule_name.
            Empty string terminates the loop.  When the plan is returned,
            it enters a loop prompting for a python expression to run the plan
            (the plan itself is in a variable called "plan", and "Db_cursor"
            is a variable containing a database cursor).  For example:
            "plan(Db_cursor, {'movie': 1})".  An empty line terminates the plan
            loop.

movie.html
movie2.html
    Two very simple html templates that you can play with.

siege.urls
    A list of all combinations of movies 1-6 with movie.html and movie2.html
    for the siege program.  This measures the performance of the web server:

        $ siege -c 2 -f siege.urls

profile_server.py
    Invokes the simple_server under cProfile.  Use siege to stimulate the
    server, then type ctl-C to interrupt it:

        Terminal 1                      Terminal 2
        --------------------------      --------------------------
        $ python                        
        >>> from examples.web_framework import profile_server       
        >>> profile_server.run()        
                                        $ siege -c 1 -f siege.urls
        ctl-C                           
        >>> profile_server.stats()      

    The 'run' function takes two optional arguments: port=8080 and
    logging=False.  Pass logging=True to enable logging requests to stderr.

preforked_server.py
    This creates the web server socket, then forks the process to get N long
    running processes all accepting connections from the same socket.  Each
    process will connect independently to the database server when they
    receive their first request.  Use ctl-C to kill all of the processes.
    This will fully utilize multiple processors to achieve higher throughputs:

        $ python
        >>> from examples.web_framework import preforked_server
        >>> preforked_server.run(2)     # 2 is the number of processes

        ctl-C

    The 'run' function takes three optional arguments: num_processes=2,
    port=8080 and logging=False.
