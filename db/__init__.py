
from flask_sqlalchemy import SQLAlchemy

from .schema import metadata

database = SQLAlchemy(metadata=metadata)
