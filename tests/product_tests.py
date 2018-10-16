import unittest
import json
from app import create_app

user_data = dict(product_name="Acer",
                            unit_price=19000000,
                            stock=100)

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()


    """testing  GET all items in the inventory"""

    def test_get_all_inventory_items(self):
        with self.app.test_client() as client:
            response = client.get("/v1/products",
                                  content_type="application/json",
                                  data=json.dumps(user_data))
            response_json = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn("Acer", response_json[0]['product_name'])

    """testing  GET a single item in the inventory"""

    def test_get_one_item_in_inventory(self):
        with self.app.test_client() as client:
            response = client.get("/v1/products/1",
                                  content_type="application/json",
                                  data=json.dumps(user_data))
            response_json = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn("Acer", response_json[0]['product_name'])

    """testing adding an item to cart"""

    def test_add_new_inventory_item(self):
        with self.app.test_client() as client:
            response = client.post('/v1/products', content_type='application/json',
                                   data=json.dumps(user_data))
            self.assertEqual(response.status_code, 201)
            responseJson = json.loads(response.data.decode())
            self.assertIn('product created', responseJson['message'])



    if __name__ == '__main__':
        unittest.main()
