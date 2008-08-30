"""Main Controller"""
from tg2movie.lib.base import BaseController
from tg import expose, flash
from pylons.i18n import ugettext as _
#from tg import redirect, validate
#from tg2movie.model import DBSession, metadata
#from dbsprockets.dbmechanic.frameworks.tg2 import DBMechanic
#from dbsprockets.saprovider import SAProvider

from tg2movie.model import DBSession
from tg2movie.model import Movie, Director, MovieDirectorLink, Catalog

class RootController(BaseController):
    #admin = DBMechanic(SAProvider(metadata), '/admin')

    @expose('tg2movie.templates.index')
    def index(self):
        return dict(page='index')

    @expose('tg2movie.templates.about')
    def about(self):
        return dict(page='about')

    @expose('tg2movie.templates.movie')
    def movie(self, id):
        return dict(m=DBSession.query(Movie).filter(Movie.id==id)[0])

    @expose('tg2movie.templates.movie2')
    def movie2(self, id):
        return dict(m=DBSession.query(Movie).filter(Movie.id==id)[0],
                    catalog=DBSession.query(Catalog).filter(Catalog.movie_id==id)[:])


