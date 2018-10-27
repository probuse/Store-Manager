from app.api import auth_v1
from app_utils import empty_string_catcher, email_validator
from flask import request, current_app as app

from database.db import DBHandler

from flask_restful import Resource, Api
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash

from flask_jwt_extended import (create_access_token, jwt_required, get_jwt_identity)

api = Api(auth_v1)

'''This class handles user registration'''


class Registration(Resource):

    def post(self):
        data = request.get_json()
        email = data['email']
        username = data['username']
        password = generate_password_hash(data['password'], method='sha256')
        is_admin = data['is_admin']
        if not isinstance(username, str) or not isinstance(password, str) or not isinstance(is_admin, bool):
            return {"message": "Please review the values added"}, 400

        if not empty_string_catcher(username) or not empty_string_catcher(password):
            return {'message': 'please fill all fields'}, 400

        if not email_validator(email):
            return {'message': 'Error: invalid email: Please check email'}, 400

        db_obj = DBHandler(app.config['DATABASE_URL'])
        if db_obj.find_by_username(username):
            return {'message': 'A user with that username already exists'}, 409
        if db_obj.find_by_email(email):
            return {'message': 'A user with that email already exists'}, 409
        else:
            db_obj.create_user(data)
            return {'message': 'User successfully created'}, 201


class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']

        if not isinstance(username, str) or not isinstance(password, str):
            return {'message': 'please insert correct values'}, 400
        if not empty_string_catcher(username) or not empty_string_catcher(password):
            return {'message': 'please fill all fields'}, 400

        db_obj = DBHandler(app.config['DATABASE_URL'])

        query = db_obj.fetch_by_param(
            'users', 'username', data['username'])
        if not query:
            return {'message': 'The user does not exist, please register'}, 400

        user = db_obj.auth_user(username)

        if not check_password_hash(user['password'], password):
            return {'message': 'Error: wrong password'}, 400

        access_token = create_access_token(identity=user)
        return {'access_token': access_token}, 200


api.add_resource(Registration, '/signup')
api.add_resource(Login, '/login')
