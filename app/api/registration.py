from flask import request
from flask_restful import Resource, Api
from database.model import Registereduser
from flask_jwt_extended import create_access_token
from app.api import auth_v1

users_list = []

api = Api(auth_v1)


class SignUp(Resource):

    def post(self):
        data = request.get_json()
        user_id = len(users_list) + 1
        username = data['username']
        password = data['password']
        is_owner = data['is_owner']
        users_list.append(Registereduser(user_id, username, password, is_owner))
        return {'message': 'User registered'}, 201


class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']
        is_owner = data['is_owner']
        user_dict = dict(username=username, password=password, is_owner=is_owner)
        access_token = create_access_token(identity=user_dict)
        return {'access_token': access_token}, 201


api.add_resource(SignUp, '/signup')
api.add_resource(Login, '/login')
