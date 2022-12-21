from my_final_project import app, db
from my_final_project.products.models import Product, ProductCategory, ProductionLine
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


from flask_admin import BaseView, expose

class AnalyticsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')


# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'simplex'

admin = Admin(app, name='MRP', template_mode='bootstrap4')
# Add administrative views here

class CustomModelViewName(ModelView):
    can_delete = False
    column_hide_backrefs = False
    can_export = True
    

admin.add_view(AnalyticsView(name='Home', endpoint='home', url='/'))

admin.add_view(ModelView(ProductCategory, db.session, category='Product'))
admin.add_view(ModelView(ProductionLine, db.session, category='Product'))
admin.add_view(CustomModelViewName(Product, db.session, category='Product'))