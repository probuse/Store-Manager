from flask import request
from flask_restful import Resource, Api
from database.model import Productpoints, Salepoints
from app_utils import is_string, empty_string_catcher
from app.api import apcn_v1

products_list = []

sales_list = []

API = Api(apcn_v1)

"""This class handles the creation and returning of products"""

class Products(Resource):
    """This function returns a list of all producst in the inventory"""

    def get(self, product_id=0):
        response = []
        an_list = []
        for product_list in products_list:
            response.append(product_list.to_json())
        if not response:
            return {'message':'No product in inventory'}, 200
        return response, 200


API.add_resource(Products, '/', '/<int:product_id>')