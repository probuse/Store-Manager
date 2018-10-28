from database.db import DBHandler
from flask import current_app as app
import re
from werkzeug.security import check_password_hash
db_obj = DBHandler(app.config['DATABASE_URL'])

class User:
    """Class handles user object operations"""

    def __init__(self, email, username, password, is_admin):
        self.email = email
        self.username = username
        self.password = password
        self.is_admin = is_admin

    def query_username(username):
        """Method to retrieve a username from the database"""
        # db_obj = DBHandler(app.config['DATABASE_URL'])
        user = db_obj.fetch_by_param('users', 'username', username)

        if user is None:
            return False
        else:
            print(user)
            return user

    def query_email(email):
        """Method to retrieve a username from the database"""

        # db_obj = DBHandler(app.config['DATABASE_URL'])
        user = db_obj.fetch_by_param('users', 'email', email)

        if user is None:
            return False
        else:
            return user

    def query_password(password):
        """Method to retrieve a username from the database"""

        # db_obj = DBHandler(app.config['DATABASE_URL'])
        user = db_obj.fetch_by_param('users', 'password', password)
        if not check_password_hash(user['password'], password):
            return False
        return True

    def insert_user(self):
        # db_obj = DBHandler(app.config['DATABASE_URL'])
        user = db_obj.create_user(self.email, self.username, self.password, self.is_admin)

        if user is None:
            return False
        else:
            return user

    def authenticate_user(password):
        # db_obj = DBHandler(app.config['DATABASE_URL'])
        user = db_obj.fetch_by_param('users', 'password', password)
        if not check_password_hash(user['password'], password):
            return False
        return True


class Product:
    def __init__(self, username, product_name, unit_price, stock):
        self.username = username
        self.product_name = product_name
        self.unit_price = unit_price
        self.stock = stock

    def insert_product(self):
        # db_obj = DBHandler(app.config['DATABASE_URL'])
        user = db_obj.create_product(self.username, self.product_name, self.unit_price, self.stock)

        if user is None:
            return False
        else:
            return user

    def view_products():
        # db_obj = DBHandler(app.config['DATABASE_URL'])
        response = db_obj.view_all_products()
        return response
