from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    internal_code = StringField('Internal Code', validators=[DataRequired()])
    customer_code = StringField('Customer Code', validators=[DataRequired()])