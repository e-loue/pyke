NOTE: This example is only a proof-of-concept and is not intended for
      production use!

This example generates SQL statements, given a tuple of column names.  It was
originally written for MySQL but now also supports Sqlite3.  It is relatively
easy to port to other database engines.

The following files can be used to create and populate the database.  A
pre-populated Sqlite3 database is included in this directory as 'sqlite3.db'.

    create_database.sql
        Creates movie_db database and users: movie_admin/admin_pw and
        movie_user/user_pw.
    create_tables.sql       # for MySQL
    create_tables.sqlite3   # for Sqlite3
        movie
            id                  int auto_increment
            title               varchar(100)
            genre_id            int
            year                year
            length              time
        genre
            id                  int auto_increment
            genre_name          varchar(100)
        director
            id                  int auto_increment
            director_name       varchar(100)
        movie_director_link
            movie_id            int
            director_id         int
            billing             int
        catalog
            movie_id            int
            dvd_number          int
            selection_number    int default 1
    drop_tables.sql

This shell script loads 6 movies:

    load_tables    # for MySQL
    load_sqlite3   # for Sqlite3
        Loads the following files in the indicated order:
            genre.txt
            movie.txt
            director.txt
            movie_director_link.txt
            catalog.txt

load_mysql_schema.py
load_sqlite3_schema.py
    These provide one function which loads the "schema" fact base from the
    database connection provided:

        load_schema(pyke_engine, dbi_module, db_connection)

    All facts are asserted as universal facts so that they remain after an
    engine.reset() is done.

    The following facts are asserted:

        schema.paramstyle(paramstyle) # e.g.: format, qmark
        schema.column(table_name, col_name, type, null, key, default, extra)
        schema.primary_key(table_name, columns)
        schema.many_to_1(table_many, table_1,
                         table_many_columns, table_1_columns)
        schema.links_to(depth, start_table, end_table, joins)

database.krb
    This uses backward-chaining to build SQL statements and cook them into
    plans that execute them.  The top-level goal is:

        get_data($starting_tables, $needed_data) \
          taking(db_cursor, starting_keys)

    $starting_tables is a list of tables that you have id values for.  The
    starting_keys parameter to the plan is a dictionary mapping these table
    names to id values that identify a unique row in that table.

    The $needed_data is a tuple of column_names and/or (multi-row-name,
    (options), column_name...).

    The plan will return a dictionary with keys from $needed_data and values
    from the database.  Where the multi-row-name sub-tuple is used, the key in
    the top-level dictionary is multi-row-name (this can be anything, it
    doesn't match anything in the schema).  Its value is a tuple of
    dictionaries with the indicated column_names as keys and values from the
    database.

driver.py
driver_sqlite3.py
    These have a debug "cursor" class that can be used instead of a real
    database cursor.  The debug cursor class does not require a database
    connection and returns dummy data from any SELECT call.

    Import either driver (for mysql) or driver_sqlite3, for example:

    >>> import driver_sqlite3

    Test functions:

    >>> driver_sqlite3.init()
            Creates a pyke engine and calls load_schema.
    >>> driver_sqlite3.run()
            Loops on "goal: " prompt.  Type a goal, or trace/untrace rule_name.
            Empty string terminates the loop.  Examples:

                goal: get_data((movie), (title, year, length))
                goal: get_data((director), (director_name, (movies, (), title, year))

            When the plan is run, it first runs it with the debug cursor, then
            enters a loop prompting for the starting_keys values.  These
            should be entered space separated.  An empty line terminates the
            plan loop.  For example:

                ('movie',): 1

