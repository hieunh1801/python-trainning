from datetime import datetime
from config import db, ma


class BasketDetail(db.Model):
    """
    BasketDetail Model
    """
    __tablename__ = "basket_detail"
    detail_id = db.Column(db.Integer, primary_key=True)
    basket_id = db.Column(db.Integer, nullable=True)
    news_id = db.Column(db.Integer, nullable=True)


class BasketDetailSchema(ma.ModelSchema):
    class Meta:
        model = BasketDetail
        sqla_session = db.session
