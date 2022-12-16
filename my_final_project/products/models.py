from my_final_project import db
from dataclasses import dataclass


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

    def __repr__(self) -> str:
        return f"Product({id}, '{self.name}'"


class ProductCategory(db.Model):

    __tablename__ = 'product_category'

    id: int
    name: str

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"ProductCategory({id}, '{self.name}'"


class ProductionLine(db.Model):
    __tablename__ = 'production_line'

    id: int
    name: str

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"ProductionLine({id}, '{self.name}'"



