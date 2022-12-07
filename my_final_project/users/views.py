from flask import render_template, Blueprint

bp = Blueprint('users', __name__, template_folder='templates')

@bp.route('/login')
def login():
    return render_template('login.html')