Pyke: Python Knowledge Engine

Version: 1.1.1

Both forward-chaining and backward-chaining rules (which may include python
code) are compiled into python. Can also automatically assemble python
programs out of python functions which are attached to backward-chaining
rules.

COPYRIGHT AND LICENSE:

This is published under the MIT License.  The copyright and license are in
the file "LICENSE" in the source directory.

DOCUMENTATION:

The complete documentation is at:

    http://pyke.sourceforge.net

A copy of the html documentation is also included in the "doc/html" directory
within the source distribution.


REQUIREMENTS:

Pyke requires python 2.5 or later.  Check with:

    $ python --version

You can download python at:

    http://www.python.org


TO INSTALL:

    1. Download and unzip the source distribution for the version of Python
       that you want to use.

       If you want to use Python 2.5 or 2.6, you need to use the pyke-1.1.1.zip
       sources.

       If you want to use Python 3.x, you need to use the pyke3-1.1.1.zip
       sources.

    2. Open a command line window in the directory above.
    3. Run "python setup.py build"
    4. As administrator, run: "python setup.py install"

See http://pyke.sourceforge.net/about_pyke/installing_pyke.html for more
information.

SOURCE DISTRIBUTION:

The source distribution contains the pyke source code, documentation (both
source and html), unit tests, and examples.

EXAMPLES:

Each example is in a separate subdirectory under the "examples" directory.
Each example has a README.txt file that explains how to run it.

The family_relations example is a good place to start.  It shows several
solutions to the same problem.  It also has an example of a few rule
optimizations that result in a 100 times performance improvement on this
problem.

The sqlgen example uses Sqlite3 (or MySQL) and the python sqlite3 (or MySQLdb)
modules.  It has a function that reads the schema information into pyke facts.
Then the rules in database.krb automatically figure out how to join tables
together to retrieve a list of column names, generate the SQL select
statements and return a plan to execute this SQL statement and return the
results as a dictionary.

The web_framework example uses the sqlgen example.  This demonstrates the use
of multiple rule bases.  The web_framework is a WSGI application that uses the
HTMLTemplate package (install this as administrator with "pip install
HTMLTemplate" or "easy_install HTMLTemplate" -- be sure to get version 1.5 or
later).  It gets the column names from the HTMLTemplate and feeds those to the
sqlgen example to generate a plan to retrieve the data.  It then builds a plan
to populate the template and return the finished HTML document.  It also
caches the plans so that they don't have to be re-generated for each request.
This makes it run a full 10 times faster than the same example done in
TurboGears 2!  The example includes a wsgiref simple_server setup to run it
as an http server so that you can access it through your browser.

The learn_pyke example is an incomplete attempt at a computer based training
program.  It only deals with the topic of pattern matching.  It is left here
as an example of using question bases.

The findall, forall, knapsack, notany and towers_of_hanoi examples are each
very small.

See http://pyke.sourceforge.net/examples.html for more information.


RUNNING DOCTESTS:

Pyke uses the doctest-tools package to run its doctests.  You can run the
"testall.py" program from doctest-tools in any subdirectory, or in the
top-level directory.  You can install doctest-tools as administrator with:

    # pip install doctest-tools

The top-level directory also has it's own "testpyke" script that removes all
compiled_krb directories, then runs the testall.py script (from doctest-tools)
twice.  The first time forces pyke to recompile everything, and the second
time runs the same tests again having pyke re-use the compiled results from
the previous run.  If the "testpyke" program is not on your path, run it as:

    $ ./testpyke


WORKING ON PYKE:

See http://pyke.sourceforge.net/about_pyke/modifying_pyke.html for information
about doing development work on Pyke.  Contributions of any kind are welcome!

