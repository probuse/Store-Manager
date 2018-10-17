import unittest
import json
from app import create_app

product_data = dict(product_name="Acer",
                    unit_price=19000000,
                    stock=100)

sale_data = dict(product_id=1,
                 product_name="Acer",
                 unit_price=19000000,
                 quantity=32)


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()

    """testing  GET all items in the inventory"""

    def test_get_all_inventory_items(self):
        with self.app.test_client() as client:
            response = client.get("/v1/products",
                                  content_type="application/json",
                                  data=json.dumps(product_data))
            response_json = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn("Acer", response_json[0]['product_name'])

    """Products tests"""

    """testing  GET a single item in the inventory"""

    def test_get_one_item_in_inventory(self):
        with self.app.test_client() as client:
            response = client.get("/v1/products/1",
                                  content_type="application/json",
                                  data=json.dumps(product_data))
            response_json = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn("Acer", response_json[0]['product_name'])

    """testing adding an item to inventory"""

    def test_add_new_inventory_item(self):
        with self.app.test_client() as client:
            response = client.post('/v1/products', content_type='application/json',
                                   data=json.dumps(product_data))
            self.assertEqual(response.status_code, 201)
            responseJson = json.loads(response.data.decode())
            self.assertIn('product created', responseJson['message'])

    """Testing for wrong data type inserted"""

    def test_wrong_data_type(self):
        with self.app.test_client() as client:
            response = client.post('/v1/products', content_type='application/json',
                                   data=json.dumps(dict(product_name="Acer",
                                                        unit_price="19000000",
                                                        stock=100)))
            self.assertEqual(response.status_code, 400)
            responseJson = json.loads(response.data.decode())
            self.assertIn('Error:Invalid value please review product inputs', responseJson['message'])

    """Testing for empty space"""

    def test_empty_space(self):
        with self.app.test_client() as client:
            response = client.post('/v1/products', content_type='application/json',
                                   data=json.dumps(dict(product_name=" ",
                                                        unit_price=19000000,
                                                        stock=100)))
            self.assertEqual(response.status_code, 400)
            responseJson = json.loads(response.data.decode())
            self.assertIn('Empty values are not allowed', responseJson['message'])

    """Sales tests"""

    """testing  GET all items sold"""

    def test_get_all_items_sold(self):
        with self.app.test_client() as client:
            response = client.get("/v1/sales",
                                  content_type="application/json",
                                  data=json.dumps(sale_data))
            response_json = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn("Acer", response_json[0]['product_name'])


    """testing  GET a single sale"""

    def test_get_one_sale(self):
        with self.app.test_client() as client:
            response = client.get("/v1/sales/1",
                                  content_type="application/json",
                                  data=json.dumps(sale_data))
            response_json = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn("Acer", response_json[0]['product_name'])

    """testing adding a sale"""

    def test_add_new_sale(self):
        with self.app.test_client() as client:
            response = client.post('/v1/sales', content_type='application/json',
                                   data=json.dumps(sale_data))
            self.assertEqual(response.status_code, 201)
            responseJson = json.loads(response.data.decode())
            self.assertIn('sale made', responseJson['message'])

    if __name__ == '__main__':
        unittest.main()
