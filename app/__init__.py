from flask import Flask
from .api import apcn_v1


def create_app():
    app = Flask(__name__)

    app.register_blueprint(apcn_v1)

    return app
