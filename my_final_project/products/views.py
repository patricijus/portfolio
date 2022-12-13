from flask import render_template, Blueprint, redirect, url_for
from .models import Product
from .forms import ProductForm
from my_final_project import db

bp = Blueprint('products', __name__, template_folder='templates', url_prefix='/')

@bp.route('/')
def main():
    return render_template('product-main.html')

@bp.route('/product_list')
def product_list():
    products = Product.query.all()
    return render_template('product-list.html', products=products)


@bp.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = ProductForm()
    error = None
    if form.validate_on_submit():
        try:
            product = Product(name=form.name.data)
            print(product)
            db.session.add(product)
            db.session.commit()
            return redirect(url_for('products.product_list'))
        except:
            error = "Duplicate"
            return render_template('product-add.html', form=form, error=error)
    return render_template('product-add.html', form=form)

@bp.route('/edit_product/<int:id>')
def edit_product(id):

    return "Future edit product"
