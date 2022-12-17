#################
#### imports ####
#################
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_admin import Admin
# from flask_admin.contrib.sqla import ModelView
################
#### config ####
################

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')
db = SQLAlchemy(app) 
migrate = Migrate(app,db)

from my_final_project.users.models import User
from my_final_project.products.models import Product, ProductCategory, ProductionLine

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Product': Product, 'ProductCategory': ProductCategory, 'ProductionLine': ProductionLine}



# # set optional bootswatch theme
# app.config['FLASK_ADMIN_SWATCH'] = 'simplex'

# admin = Admin(app, name='MRP', template_mode='bootstrap4')
# # Add administrative views here

# class CustomModelViewName(ModelView):
#     can_delete = False
#     column_hide_backrefs = False


# admin.add_view(ModelView(ProductCategory, db.session, category='Product'))
# admin.add_view(ModelView(ProductionLine, db.session, category='Product'))
# admin.add_view(CustomModelViewName(Product, db.session, category='Product'))

from my_final_project.admin import Admin
from my_final_project.users.views import bp as users_blueprint
from my_final_project.products.views import bp as products_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(products_blueprint)