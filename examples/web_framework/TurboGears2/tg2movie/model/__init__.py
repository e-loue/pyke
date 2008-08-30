"""The application's model objects"""

from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import MetaData

# Bruce added:
from sqlalchemy import Column, MetaData, Table, types
from sqlalchemy.orm import mapper


# Global session manager.  DBSession() returns the session object
# appropriate for the current web request.
DBSession = scoped_session(sessionmaker(autoflush=True, autocommit=False))

# Global metadata. If you have multiple databases with overlapping table
# names, you'll need a metadata for each database.
metadata = MetaData()

#####
# Generally you will not want to define your table's mappers, and data objects
# here in __init__ but will want to create modules them in the model directory
# and import them at the bottom of this file.  
#
######

def init_model(engine):
    """Call me before using any of the tables or classes in the model."""
    
    # If you are using reflection to introspect your database and create 
    # table objects for you, your tables must be defined and mapped inside 
    # the init_model function, so that the engine is available if you 
    # use the model outside tg2, you need to make sure this is called before
    # you use the model. 

    #
    # See the following example: 
    
    #global t_reflected
    
    #t_reflected = Table("Reflected", metadata,
    #    autoload=True, autoload_with=engine)
    global t_movie, t_catalog, t_director, t_genre, t_movie_director_link
    t_catalog = Table("catalog", metadata, autoload=True,
autoload_with=engine)
    t_director = Table("director", metadata, autoload=True,
autoload_with=engine)
    t_genre = Table("genre", metadata, autoload=True, autoload_with=engine)
    t_movie = Table("movie", metadata, autoload=True, autoload_with=engine)
    t_movie_director_link = Table("movie_director_link", metadata,
autoload=True, autoload_with=engine)

    #mapper(Reflected, t_reflected)
    mapper(Movie, t_movie)
    mapper(Catalog, t_catalog)
    mapper(Director, t_director)
    mapper(Genre, t_genre)
    mapper(MovieDirectorLink, t_movie_director_link)

# Import your model modules here. 

class Movie(object):
    pass
    # using 'paster shell', to load the entire environment into an interactive
    # shell
    # ['__class__', '__delattr__', '__dict__', '__doc__', '__getattribute__',
    # '__hash__', '__init__', '__module__', '__new__', '__reduce__',
    # '__reduce_ex__',
    # '__repr__', '__setattr__', '__str__', '__weakref__', '_class_state',
    # 'c', 'genre_id', 'id', 'length', 'title', 'year']

    # conveniance function
    def getDirectorLinks(self):
        if (self.id):
            return DBSession.query(MovieDirectorLink).filter(MovieDirectorLink.movie_id==self.id)

class Catalog(object):
    pass
    # [ ..., 'dvd_number', 'movie_id', 'selection_number']

class Director(object):
    pass
    # [..., 'director_name', 'id']

    # conveniance function
    def getMovieLinks(self):
        if (self.id):
            return DBSession.query(MovieDirectorLink).filter(MovieDirectorLink.director_id==self.id)

class Genre(object):
    pass
    # [..., 'genre_name', 'id']

class MovieDirectorLink(object):
    def getMovie(self):
        if (self.movie_id):
            return DBSession.query(Movie).filter(Movie.id==self.movie_id)[0]
    def getDirector(self):
        if (self.director_id):
            return DBSession.query(Director).filter(Director.id==self.director_id)[0]
    # [ ..., 'billing', 'director_id', 'movie_id']


