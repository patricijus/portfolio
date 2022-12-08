#################
#### imports ####
#################
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
################
#### config ####
################

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')
db = SQLAlchemy(app) 
migrate = Migrate(app,db)

from my_final_project.users.models import User

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}


from my_final_project.users.views import bp as users_blueprint

app.register_blueprint(users_blueprint)
