class Productpoints():
    def __init__(self, product_id, product_name, unit_price, stock):
        self.product_id = product_id
        self.product_name = product_name
        self.unit_price = unit_price
        self.stock = stock

    def to_json(self):
        jsondata = {'product_id': self.product_id,
                    'product_name': self.product_name,
                    'unit_price': self.unit_price,
                    'stock': self.stock

                    }
        return jsondata


class Salepoints():
    def __init__(self, sale_id, product_id, product_name, unit_price, quantity):
        self.sale_id = sale_id
        self.product_id = product_id
        self.product_name = product_name
        self.unit_price = unit_price
        self.quantity = quantity

    def to_json(self):
        jsondata = {'sale_id': self.sale_id,
                    'product_id': self.product_id,
                    'product_name': self.product_name,
                    'unit_price': self.unit_price,
                    'quantity': self.quantity
                    }
        return jsondata