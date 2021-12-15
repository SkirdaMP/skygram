import os
from flask import Flask


def create_app():
    flask_app = Flask(__name__)
    app_settings = os.getenv("APP_SETTINGS")
    flask_app.config.from_object(app_settings)

    with flask_app.app_context():
        from app.views import skygram_blueprint

        flask_app.register_blueprint(skygram_blueprint)

    return flask_app
