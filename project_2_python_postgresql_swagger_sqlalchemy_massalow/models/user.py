from datetime import datetime
from config import db, ma
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class User(db.Model):
    """
    User Model
    """
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(10), nullable=False)
    superior_id = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(32), nullable=True)
    password = db.Column(db.String(32), nullable=False)
    fullname = db.Column(db.String(100), nullable=True)
    dob = db.Column(db.Date, nullable=True)
    address = db.Column(db.String(1000), nullable=True)
    phonenumber = db.Column(db.String(15), nullable=True)
    email = db.Column(db.String(50), nullable=False)


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        sqla_session = db.session
