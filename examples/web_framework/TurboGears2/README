This was originally run on TurboGears2-1.9.7a3dev_r5053.  Since TurboGears 2
is still evolving, you may have to tweak this at step 4 if you use a different
version...

1.  Follow the directions to install TurboGears on:
    http://www.turbogears.org/2.0/docs/main/DownloadInstall.html

2.  If you created a virtual environment, make sure you also install
    MySQL-python.  (I just made a symbolic link from
        /usr/lib/python2.5/site-packages/MySQLdb
        /usr/lib/python2.5/site-packages/_mysql_exceptions.py
        /usr/lib/python2.5/site-packages/_mysql_exceptions.pyc
        /usr/lib/python2.5/site-packages/_mysql.so
    to the virtual environment's lib/python2.5/site-packages directory).

3.  In the directory that you want to contain the TurboGears application (for
    example, your virtual environment, tg2env, if you followed the steps
    outlined by TurboGears):

    $ paster quickstart --sqlalchemy
    Enter project name: tg2movie
    Enter package name [tg2movie]: 
    Do you need Identity (usernames/passwords) in this project? [no] 

    This will create a directory called "tg2movie".

4.  Copy the 2 html templates from this directory into the new
    tg2movie/tg2movie/templates directory.

    Modify the 3 new files below using the corresponding files from this
    directory:
    
        tg2movie/development.ini
        tg2movie/tg2movie/controllers/root.py
        tg2movie/tg2movie/model/__init__.py

5.  Start TurboGears.  From the top-level "tg2movie" directory:

    $ paster serve development.ini

    This starts the TurboGears server listening on port 8080 (which is in the
    development.ini file if you want to change it).

6.  From your browser goto:

        http://localhost:8080/movie/1
        http://localhost:8080/movie/2
        http://localhost:8080/movie/3
        http://localhost:8080/movie/4
        http://localhost:8080/movie/5
        http://localhost:8080/movie/6
        http://localhost:8080/movie2/1
        http://localhost:8080/movie2/2
        http://localhost:8080/movie2/3
        http://localhost:8080/movie2/4
        http://localhost:8080/movie2/5
        http://localhost:8080/movie2/6

7.  Hit Ctrl-C to kill TurboGears when you're done.

