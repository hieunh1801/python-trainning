
from datetime import datetime
from config import db, ma
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import UniqueConstraint, PrimaryKeyConstraint


class UserResource(db.Model):
    """
    User Resource Model
    """
    __tablename__ = "user_resource"
    user_resource_id = db.Column(db.Integer, primary_key=True)
    privilege = db.Column(db.String(32), nullable=True)
    user_id = db.Column(db.Interger, ForeignKey('User.user_id'))
    resource_id = db.Column(db.Integer, ForeignKey('Resource.resource_id'))
    __table_args__ = (PrimaryKeyConstraint('user_id', 'resource_id'), )


class UserResourceSchema(ma.ModelSchema):
    class Meta:
        model = UserResource
        sqla_session = db.session
