
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

from .schema import metadata


class MyBase(object):
	pass


class MyDb(object):
	def __init__(self):
		self.engine = None
		self.Base = declarative_base(cls=MyBase, metadata=metadata)
		self.SS = None

	def init_app(self, app):
		self.engine = create_engine(app.config['DB_URL'])
		self.SS = scoped_session(sessionmaker(bind=self.engine))
		self.Base.query = self.SS.query_property()
		app.db = self

# db = MyDb()
