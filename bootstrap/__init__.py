from flask import Flask


def create_app():
    app = Flask(__name__, template_folder="../templates/")

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/database.sqlite'

    from app.http.front.routes import front
    app.register_blueprint(front)

    return app
