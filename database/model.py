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

    def to_json_id(self):
        jsondata = {'product_name': self.product_name,
                    'unit_price': self.unit_price,
                    'stock': self.stock
                    }
        return jsondata


class Salepoints():
    def __init__(self, sale_id, product_id, username, quantity, total):
        self.sale_id = sale_id
        self.product_id = product_id
        self.username = username
        self.quantity = quantity
        self.total = total

    def to_json(self):
        jsondata = {'sale_id': self.sale_id,
                    'product_id': self.product_id,
                    'username': self.username,
                    'quantity': self.quantity,
                    'total': self.total
                    }
        return jsondata

    def to_json_id(self):
        jsondata = {'product_id': self.product_id,
                    'username': self.username,
                    'quantity': self.quantity,
                    'total': self.total
                    }
        return jsondata


class Registereduser():
    def __init__(self, user_id, email, password, role):
        self.user_id = user_id
        self.email = email
        self.password = password
        self.role = role

    def to_json(self):
        jsondata = {'user_id': self.user_id,
                    'email': self.email,
                    'password': self.password,
                    'role': self.role
                    }
        return jsondata
