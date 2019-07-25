from datetime import datetime
from config import db, ma


class ResourceGroupDetail(db.Model):
    """
    ResourceGroupDetail Model
    """
    __tablename__ = "resource_group_detail"
    detail_id = db.Column(db.Integer, primary_key=True)
    resource_group_id = db.Column(db.Integer, nullable=False)
    resource_id = db.Column(db.Integer, nullable=False)


class ResourceGroupDetailSchema(ma.ModelSchema):
    class Meta:
        model = ResourceGroupDetail
        sqla_session = db.session
