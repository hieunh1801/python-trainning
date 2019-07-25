from datetime import datetime
from config import db, ma


class Report(db.Model):
    """
    Report Model
    """
    __tablename__ = "report"
    report_id = db.Column(db.Integer, primary_key=True)
    higher_report_id = db.Column(db.Integer, nullable=True)
    numerical_order = db.Column(db.Integer, nullable=True)
    content = db.Column(db.String(1000), nullable=True)


class ReportSchema(ma.ModelSchema):
    class Meta:
        model = Report
        sqla_session = db.session
