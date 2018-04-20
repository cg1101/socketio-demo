
import os

class Config:
	SECRET_KEY = 'secret for cookie'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI']
	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	pass

class TestingConfig(Config):
	pass

class ProductionConfig(Config):
	pass

config = {
	'production': ProductionConfig,
	'testing': TestingConfig,
	'development': DevelopmentConfig,
	'default': DevelopmentConfig,
}
