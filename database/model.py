class Productpoints():
    def __init__(self, product_id, product_name, price_per_unit):
        self.product_id = product_id
        self.product_name = product_name
        self.price_per_unit = price_per_unit

    def to_json(self):
        jsondata = {'product_id': self.product_id,
                    'product_name': self.product_name,
                    'price_per_unit': self.price_per_unit,

                    }
        return jsondata


class Salepoints():
    def __init__(self, sale_id, shop_attendant, product_sold, price_per_unit, quantity):
        self.sale_id = sale_id
        self.product_id = product_id
        self.shop_attendant = shop_attendant
        self.product_sold = product_sold
        self.price_per_unit = price_per_unit
        self.quantity = quantity

    def to_json(self):
        jsondata = {'sale_id': self.sale_id,
                    'product_id': self.product_id,
                    'shop_attendant': self.shop_attendant,
                    'product_sold': self.product_sold,
                    'price_per_unit': self.price_per_unit,
                    'quantity': self.quantity
                    }
        return jsondata