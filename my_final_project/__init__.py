#################
#### imports ####
#################
from flask import Flask
 
################
#### config ####
################
 
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')

from my_final_project.users.views import bp as users_blueprint

app.register_blueprint(users_blueprint)
