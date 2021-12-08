from bootstrap.app import TableName
from bootstrap.app import db


class Thread(db.Model):
    __tablename__ = TableName.USER

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.text)
