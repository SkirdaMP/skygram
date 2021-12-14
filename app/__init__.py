from flask import Flask

from config import DevelopmentConfig


def create_app(config_object=DevelopmentConfig):
    flask_app = Flask(__name__)
    flask_app.config.from_object(config_object)

    with flask_app.app_context():
        from app.views import skygram_blueprint

        flask_app.register_blueprint(skygram_blueprint)

    return flask_app