from flask import render_template, Blueprint
from .models import User

bp = Blueprint('users', __name__, template_folder='templates')

@bp.route('/login')
def login():
    return render_template('login.html')

@bp.route('/users')
def users():
    users = User.query.all()
    return render_template('users-list.html', users=users)