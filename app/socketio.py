
from flask.ext.socketio import SocketIO, emit

socketio = SocketIO()

@socketio.on('message')
def handle_message(message):
	print('rceived message: ' + message)

@socketio.on('json')
def handle_json(json):
	print('received json: ' + str(json))

@socketio.on('my event')
def handle_my_event(json):
	print('received json: ' + str(json))
