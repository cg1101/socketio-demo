
from flask import Flask, request, render_template, url_for, redirect

from flask_socketio import SocketIO, emit

from config import config
# from db.db import MyDb

from db import database

socketio = SocketIO()


def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)
	
	# db = MyDb()
	# db.init_app(app)
	# SS = db.SS

	database.init_app(app)
	# socketio.init_app(app)

	# with app.app_context():
	from db.model import User
	SS = database.session

	@app.route('/')
	def index():
		# TODO: get a list of users
		users = User.query.all()
		return render_template('index.html', users=users)

	@app.route('/add_user', methods=['POST'])
	def add_user():
		user = User(**request.form)
		SS.add(user)
		SS.flush()
		return redirect(url_for('index'))

	@app.teardown_request
	def terminate_transaction(exception=None):
		if exception:
			SS.rollback()
		else:
			SS.commit()

	# @socketio.on('message')
	# def handle_message(message):
	# 	print('rceived message: ' + message)

	# @socketio.on('json')
	# def handle_json(json):
	# 	print('received json: ' + str(json))

	# @socketio.on('my event')
	# def handle_my_event(json):
	# 	print('received json: ' + str(json))

	return app
