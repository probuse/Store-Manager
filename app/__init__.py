from flask import Flask, jsonify
from .api import apcn_v1, apsn_v1, auth_v1


def create_app():
    app = Flask(__name__)

    @app.errorhandler(404)
    def not_found(e):
        response = jsonify({'message': 'The requested Resource does not exist; Please review the URL'})
        response.status_code = 404
        return response

    app.register_blueprint(apcn_v1)
    app.register_blueprint(apsn_v1)
    app.register_blueprint(auth_v1)

    return app
