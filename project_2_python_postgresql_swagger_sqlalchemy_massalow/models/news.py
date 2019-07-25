from datetime import datetime
from config import db, ma


class News(db.Model):
    """
    FileDetail Model
    """
    __tablename__ = "news"
    news_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000), nullable=True)
    summarize = db.Column(db.String(1000), nullable=True)
    content = db.Column(db.String(1000), nullable=True)


class FileSchema(ma.ModelSchema):
    class Meta:
        model = News
        sqla_session = db.session
