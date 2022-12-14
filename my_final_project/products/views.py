from flask import render_template, Blueprint, redirect, request, url_for
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
        
        product = Product(
            name=form.name.data,
            customer_code=form.customer_code.data,
            internal_code=form.internal_code.data)
            
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('products.product_list'))

    return render_template('product-add.html', form=form)

@bp.route('/edit_product/<int:id>', methods=['GET','POST'])
def edit_product(id):
    form = ProductForm()
    product = Product.query.filter_by(id=id).first()

    if form.validate_on_submit():
        product.name = form.name.data
        product.customer_code = form.customer_code.data
        product.internal_code = form.internal_code.data
        db.session.commit()
        return redirect(url_for('products.product_list'))
    if request.method == 'GET':
        form.name.data = product.name
        form.customer_code.data = product.customer_code
        form.internal_code.data = product.internal_code
        return render_template('product-add.html', form=form)
    return redirect(url_for('products.product_list'))    
