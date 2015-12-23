
from sqlalchemy import MetaData, Table, Column
from sqlalchemy import INTEGER, VARCHAR, BOOLEAN
from sqlalchemy import text

metadata = MetaData()

t_user = Table('user', metadata,
	Column('user_id', INTEGER, primary_key=True, key='userId', doc=''),
	Column('email_address', VARCHAR(30), nullable=False, unique=True, key='emailAddress', doc=''),
	Column('active', BOOLEAN, nullable=False, server_default=text('TRUE'), key='isActive', doc=''),
	Column('family_name', VARCHAR(30), nullable=True, key='familyName', doc=''),
	Column('given_name', VARCHAR(30), nullable=True, key='givenName', doc=''),
	)