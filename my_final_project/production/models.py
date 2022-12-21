from my_final_project import db
from dataclasses import dataclass
import datetime

@dataclass
class Customer(db.Model):

    id: int
    name: str

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"{self.name}"

@dataclass
class Order(db.Model):

    id: int
    customer_id: int
    customer_po_number: str
    tfi_sales_order_number: str
    order_date: datetime.datetime
    delivery_date: datetime.datetime
    production_date: datetime.datetime
    status: str
    order_qty: int
    dispatched_qty: int
    comment: str
    
    customer_id = db.Column(db.Integer, db.ForeignKey('product_category.id'))
    
