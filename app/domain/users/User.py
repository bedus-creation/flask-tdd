from bootstrap.app import db
from bootstrap.app import TableName


class User(db.Model):
    __tablename__ = TableName.USER

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    fullname = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
