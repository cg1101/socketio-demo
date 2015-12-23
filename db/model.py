
# from flask import current_app
# Base = current_app.db.Bsae

from . import database

from .schema import t_user

Base = database.Model

class User(Base):
	__table__ = t_user

