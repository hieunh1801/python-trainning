from datetime import datetime
from config import db, ma


class UserGroup(db.Model):
    """
    User Group Model
    """
    __tablename__ = "user_group"
    user_group_id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, nullable=False)
    group_name = db.Column(db.Integer, nullable=False)


class UserGroupSchema(ma.ModelSchema):
    class Meta:
        model = UserGroup
        sqla_session = db.session
