import unittest
import json
from app import create_app


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()

    """testing  GET all created questions"""

    def test_get_all_inventory_items(self):
        with self.app.test_client() as client:
            response = client.get("/v1/products",
                                  content_type="application/json",
                                  data=json.dumps(dict(product_name="Lenovo")))
            response_json = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            # self.assertEqual("Lenove", response_json[0]['product'])

    """testing creation of a new question"""

    def test_add_new_question(self):
        with self.app.test_client() as client:
            response = client.post('/v1/questions/MakeQuestions', content_type='application/json',
                                   data=json.dumps(dict(question="Is python growing?")))

            self.assertEqual(response.status_code, 201)
            responseJson = json.loads(response.data.decode())
            self.assertIn('question created', responseJson['message'])


    if __name__ == '__main__':
        unittest.main()
