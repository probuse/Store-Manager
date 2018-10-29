from app.sales import apsn_v1
from app_utils import empty_string_catcher, email_validator
from flask import request, current_app as app, jsonify
from app.models import Sale
from database.db import DBHandler
from flask_restful import Resource, Api
from werkzeug.security import generate_password_hash, check_password_hash

from flask_jwt_extended import (create_access_token, jwt_required, get_jwt_identity)


API = Api(apsn_v1)


class Sales(Resource):
    """This function returns a list of all products in the inventory"""

    def get(self, sale_id=0):
        all_sales = []
        if (sale_id):
            single_sale = [sale_list.to_json_id() for sale_list in sales_list if sale_list.sale_id == sale_id]
            if not single_sale:
                return {'message': 'sale not in inventory'}, 200
            else:
                return single_sale, 200
        else:
            for sale_list in sales_list:
                all_sales.append(sale_list.to_json())
            return all_sales, 200

    def post(self):
        """This function lets the administrator add a new product to the inventory"""
        data = request.get_json()
        product_id = data['product_id']
        username = data['username']
        product_name = data['product_name']
        quantity = data['quantity']
        total = data['total']
        # if not isinstance(product_id, int) or not isinstance(quantity, int):
        #     return {'message': 'Error:Invalid value added, please review'}, 400
        sale_items = Sale(product_id, username, product_name, quantity, total)
        sale_items.insert_sale()
        return {'message': 'product created'}, 201


API.add_resource(Sales, '/sales', '/sales/<int:sale_id>')
