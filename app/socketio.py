
from flask.ext.socketio import SocketIO, emit

socketio = SocketIO()

from db import database
from db.model import User

SS = database.session

@socketio.on('message')
def handle_message(message):
	print('rceived message: ' + message)

@socketio.on('json')
def handle_json(json):
	print('received json: ' + str(json))

@socketio.on('my event')
def handle_my_event(json):
	print('received json: ' + str(json))

@socketio.on('add_user')
def handle_add_user(json):
	print('add user using: ' + repr(json))
	user = User(**json['data'])
	SS.add(user)
	SS.flush()
	print('user added')
	emit('user_added', {
		'message': 'user {0} has been added, id: {1}'.format(user.emailAddress, user.userId),
		'user': User.dump(user),
	}, broadcast=True)
