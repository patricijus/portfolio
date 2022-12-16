
from flask import render_template, Blueprint, redirect, request, url_for
from .models import Product, ProductCategory, ProductionLine
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
    categories = ProductCategory.query.all()
    production_lines = ProductionLine.query.all()
    CATEGORIES = [(category.id, category.name) for category in categories]
    PRODUCTION_LINES = [(line.id, line.name) for line in production_lines]
    form = ProductForm()
    form.category_id.choices = CATEGORIES
    form.production_line_id.choices = PRODUCTION_LINES
    error = None
    if form.validate_on_submit():
        
        
        product = Product(
            name=form.name.data,
            customer_code=form.customer_code.data,
            internal_code=form.internal_code.data,
            category_id=form.category_id.data)
            
        db.session.add(product)
        db.session.commit()
        print(form.category_id.data)
        return redirect(url_for('products.product_list'))

    return render_template('product-add.html', form=form)


# @bp.get('/edit_product/<int:id>')
# def edit_product(id):
#     categories = ProductCategory.query.all()
#     CATEGORIES = [(category.id, category.name) for category in categories]
#     form = ProductForm()
#     form.category_id.choices = CATEGORIES
#     product = Product.query.filter_by(id=id).first()

#     form.name.data = product.name
#     form.customer_code.data = product.customer_code
#     form.internal_code.data = product.internal_code
#     form.category_id.data = product.category_id
#     return render_template('product-add.html', form=form)

# @bp.post('/edit_product/<int:id>')
# def edit_products(id):
#     categories = ProductCategory.query.all()
#     CATEGORIES = [(category.id, category.name) for category in categories]
#     form = ProductForm()
#     form.category_id.choices = CATEGORIES
#     product = Product.query.filter_by(id=id).first()
#     if form.validate_on_submit():

#         product.name = form.name.data
#         product.customer_code = form.customer_code.data
#         product.internal_code = form.internal_code.data
#         product.category_id = form.category_id.data
#         db.session.commit()
#         return redirect(url_for('products.product_list'))
#     return redirect(url_for('products.product_list'))

@bp.route('/edit_product/<int:id>', methods=['GET','POST'])
def edit_product(id):
    product = Product.query.filter_by(id=id).first()
    categories = ProductCategory.query.all()
    production_lines = ProductionLine.query.all()
    PRODUCTION_LINES = [(line.id, line.name) for line in production_lines]
    CATEGORIES = [(category.id, category.name) for category in categories]
    product = Product.query.filter_by(id=id).first()
    form = ProductForm(
        category_id=product.category_id,
        production_line_id=product.production_line_id
    )
    form.category_id.choices = CATEGORIES
    form.production_line_id.choices = PRODUCTION_LINES
    

    if form.validate_on_submit():
        product.name = form.name.data
        product.customer_code = form.customer_code.data
        product.internal_code = form.internal_code.data
        product.category_id = form.category_id.data
        product.production_line_id = form.production_line_id.data
        db.session.commit()
        return redirect(url_for('products.product_list'))
    if request.method == 'GET':

        form.name.data = product.name
        form.customer_code.data = product.customer_code
        form.internal_code.data = product.internal_code
        form.category_id.default = product.category_id
        form.production_line_id.default = product.production_line_id
        return render_template('product-add.html', form=form)

    return redirect(url_for('products.product_list'))    

@bp.route('/delete_product/<int:id>', methods=['POST', 'GET'])
def delete_product(id):
    product = Product.query.filter_by(id=id).first()
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('products.product_list'))