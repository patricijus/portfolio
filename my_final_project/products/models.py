from my_final_project import db
from dataclasses import dataclass

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String, unique=True, nullable=False)
class Product(db.Model):

    id: int
    name: str
    internal_code: str
    customer_code: str


    id = db.Column(db.Integer, primary_key=True)
    internal_code = db.Column(db.String, unique=True, nullable=False)
    customer_code = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"Product({id}, '{self.name}'"
        