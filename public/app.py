from dependency_injector import containers, providers
from dependency_injector.ext import flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/database.sqlite'

db = SQLAlchemy(app)


@app.route("/admin")
def index():
    return "Hello World"
