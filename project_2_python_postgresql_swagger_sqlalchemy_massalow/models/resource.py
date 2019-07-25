from datetime import datetime
from config import db, ma
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Resource(db.Model):
    """
    Resource Model
    """
    __tablename__ = "resource"
    resource_id = db.Column(db.Integer, primary_key=True)
    table_name = db.Column(db.String(50), nullable=False)
    specific_id = db.Column(db.Integer, nullable=False)
    required_role = db.Column(db.String(32), nullable=True)
    date_created = db.Column(db.Date, nullable=False)


class ResourceSchema(ma.ModelSchema):
    class Meta:
        model = Resource
        sqla_session = db.session
