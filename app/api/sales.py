from flask import request
from flask_restful import Resource, Api
from database.model import Productpoints, Salepoints
from app_utils import empty_string_catcher
from app.api import apsn_v1
from .products import products_list

sales_list = []

API = Api(apsn_v1)



class Sales(Resource):
    """This function returns a list of all products in the inventory"""

    def get(self, sale_id=0):
        all_sales = []
        single_sale = []
        if (sale_id):
            for sale_list in sales_list:
                if sale_list.sale_id == sale_id:
                    req_dict = (sale_list.to_json_id())
                    single_sale.append(req_dict)
            if not single_sale:
                return {'message': 'product not in inventory'}, 200
            else:
                return single_sale, 200
        else:
            for sale_list in sales_list:
                all_sales.append(sale_list.to_json())
            return all_sales, 200

    def post(self):
        """This function lets the administrator add a new product to the inventory"""

        data = request.get_json()
        sale_id = len(sales_list) + 1
        product_id = data['product_id']
        product_name = data['product_name']
        unit_price = data['unit_price']
        quantity = data['quantity']
        total = data['quantity'] * data['unit_price']
        if not isinstance(product_name, str) or not isinstance(product_id, int) or not isinstance(unit_price, int) \
                or not isinstance(quantity, int):
            return {'message': 'Error:Invalid value added, please review'}, 400
        if not empty_string_catcher(product_name):
            return {'message': 'Empty values are not allowed'}, 400
        for product_list in products_list:
            if product_list.product_id != product_id or product_list.unit_price != unit_price \
                    or product_list.product_name != data["product_name"]:
                return {'message': 'non existent product'}, 400
            else:
                sales_list.append(Salepoints(sale_id, product_id, product_name, unit_price, quantity, total))
            return {'message': 'sale made'}, 201


API.add_resource(Sales, '/sales', '/sales/<int:sale_id>')