from my_final_project import db
from dataclasses import dataclass

@dataclass
class Product(db.Model):

    id: int
    name: str
    internal_code: str
    customer_code: str


    id = db.Column(db.Integer, primary_key=True)
    internal_code = db.Column(db.String, unique=True, nullable=False)
    customer_code = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, unique=True, nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('product_category.id'))
    production_line_id = db.Column(db.Integer, db.ForeignKey('production_line.id'))

    category = db.relationship('ProductCategory', backref=db.backref('products', lazy='dynamic'))
    prod_line = db.relationship('ProductionLine', backref=db.backref('products', lazy='dynamic'))
    def __repr__(self) -> str:
        return f"{self.name}"

@dataclass
class ProductCategory(db.Model):

    __tablename__ = 'product_category'

    id: int
    name: str

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"{self.name}"

@dataclass
class ProductionLine(db.Model):
    __tablename__ = 'production_line'

    id: int
    name: str

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"{self.name}"



