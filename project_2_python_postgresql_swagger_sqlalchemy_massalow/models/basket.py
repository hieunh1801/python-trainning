from datetime import datetime
from config import db, ma


class Basket(db.Model):
    """
    Basket Model
    """
    __tablename__ = "basket"
    basket_id = db.Column(db.Integer, primary_key=True)
    basket_name = db.Column(db.String(1000), nullable=True)


class BasketSchema(ma.ModelSchema):
    class Meta:
        model = Basket
        sqla_session = db.session
