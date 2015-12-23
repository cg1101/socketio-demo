
class Config:
	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	SECRET_KEY = 'development secret!'
	# DB_URL = 'mysql+pymysql://localhost/fake_login'
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://localhost/fake_login'
	SQLALCHEMY_TRACK_MODIFICATIONS = True

class TestingConfig(Config):
	SECRET_KEY = 'testing secret!'
	# DB_URL = 'mysql+pymysql://localhost/fake_login'
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://localhost/fake_login'
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
	SECRET_KEY = 'production secret!'
	# DB_URL = 'mysql+pymysql://localhost/fake_login'
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://localhost/fake_login'
	SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
	'development': DevelopmentConfig,
	'default': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,
}
