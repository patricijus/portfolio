#################
#### imports ####
#################
from flask import Flask
 
################
#### config ####
################
 
app = Flask(__name__)
app.config.from_pyfile('flask.cfg')
from . import views