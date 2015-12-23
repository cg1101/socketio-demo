
from flask import Flask

from config import config
from db import database
from .socketio import socketio

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])

	config[config_name].init_app(app)
	database.init_app(app)
	socketio.init_app(app)

	SS = database.session

	@app.teardown_request
	def terminate_transaction(exception=None):
		if exception:
			SS.rollback()
		else:
			SS.commit()

	return app
