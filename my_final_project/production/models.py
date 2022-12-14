from my_final_project import db
from dataclasses import dataclass

class ProductionLine(db.Model):

    id: int
    name: str


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"ProductionLine({id}, '{self.name}'"
