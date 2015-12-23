
from flask import BluePrint, request, render_template, redirect, url_for

from db import database

views = bp = BluePrint('views', __name__)

from db.model import User
SS = database.session


@bp.route('/')
def index():
	# TODO: get a list of users
	users = User.query.all()
	return render_template('index.html', users=users)


@bp.route('/add_user', methods=['POST'])
def add_user():
	user = User(**request.form)
	SS.add(user)
	SS.flush()
	return redirect(url_for('index'))

