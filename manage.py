
import os

from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from app import create_app, database, socketio

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

migrate = Migrate()
migrate.init_app(app, database)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def run():
	import sys
	port = 5000 if sys.version_info.major == 2 else 1080
	socketio.run(
		app,
		host='127.0.0.1',
		port=port,
		use_reloader=True
	)

if __name__ == "__main__":
	manager.run()
