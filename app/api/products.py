from flask import request
from flask_restful import Resource, Api
from database.model import Productpoints, Salepoints
from app_utils import empty_string_catcher
from app.api import apcn_v1

products_list = []

sales_list = []

API = Api(apcn_v1)

"""This class handles the creation and returning of products"""


class Products(Resource):
    """This function returns a list of all products in the inventory"""

    def get(self, product_id=0):
        all_products = []
        single_product = []
        if (product_id):
            for product_list in products_list:
                if product_list.product_id == product_id:
                    req_dict = (product_list.to_json_id())
                    single_product.append(req_dict)
            if not single_product:
                return {'message': 'product not in inventory'}, 200
            else:
                return single_product, 200
        else:
            for product_list in products_list:
                all_products.append(product_list.to_json())
            if not all_products:
                return {'message': 'No product in inventory'}, 200
            return all_products, 200

    def post(self):
        """This function lets the administrator add a new product to the inventory"""

        data = request.get_json()
        product_id = len(products_list) + 1
        product_name = data['product_name']
        unit_price = data['unit_price']
        stock = data['stock']
        if not isinstance(product_name, str) or not isinstance(unit_price, int) or not isinstance(stock, int):
            return {'message': 'Error:Invalid value please review product inputs'}, 400
        if not empty_string_catcher(product_name):
            return {'message': 'Empty values are not allowed'}, 400
        products_list.append(Productpoints(product_id, product_name, unit_price, stock))
        return {'message': 'product created'}, 201





API.add_resource(Products, '/products', '/products/<int:product_id>')

