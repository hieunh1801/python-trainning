from datetime import datetime
from config import db, ma


class File(db.Model):
    """
    FileDetail Model
    """
    __tablename__ = "file"
    file_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10), nullable=True)
    url = db.Column(db.String(50), nullable=True)


class FileSchema(ma.ModelSchema):
    class Meta:
        model = File
        sqla_session = db.session
