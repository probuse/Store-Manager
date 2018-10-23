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
        user_id = len(users) + 1
        email = data['email']
        password = data['password']
        role = data['role']
        users_list.append(Registereduser(user_id, email, password, role))
        return {'message': 'User registered'}, 400


class Login(Resource):
    def post(self):
        data = request.get_json()
        email = data['email']
        password = data['password']
        role = data['role']
        user_dict = dict(email=email, password=password, role=role)

        access_token = create_access_token(identity=user_dict)
        return {'access_token': access_token}, 200


api.add_resource(SignUp, '/signup')
api.add_resource(Login, '/login')
