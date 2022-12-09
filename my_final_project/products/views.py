from flask import render_template, Blueprint
from .models import Product

bp = Blueprint('products', __name__, template_folder='templates', url_prefix='/products')

@bp.route('/product_list')
def product_list():
    products = Product.query.all()
    return render_template('product-list.html', products=products)


@bp.route('/add_product')
def add_product():
    return "Future add new product form"

@bp.route('/edit_product/<int:id>')
def edit_product(id):
    return "Future edit product"