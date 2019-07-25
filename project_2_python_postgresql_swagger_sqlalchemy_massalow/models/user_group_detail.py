from datetime import datetime
from config import db, ma


class UserGroupDetail(db.Model):
    """
    UserGroupDetail Model
    """
    __tablename__ = "user_group_detail"
    detail_id = db.Column(db.Integer, primary_key=True)
    user_group_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)


class UserGroupDetailSchema(ma.ModelSchema):
    class Meta:
        model = UserGroupDetail
        sqla_session = db.session
