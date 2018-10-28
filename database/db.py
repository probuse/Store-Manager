import psycopg2
from urllib.parse import urlparse
from werkzeug.security import generate_password_hash


class DBHandler:
    def __init__(self, database_url):
        parsed_url = urlparse(database_url)
        dbname = parsed_url.path[1:]
        username = parsed_url.username
        hostname = parsed_url.hostname
        password = parsed_url.password
        port = parsed_url.port
        self.conn = psycopg2.connect(
            database=dbname,
            user=username,
            password=password,
            host=hostname,
            port=port)
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    '''Create tables'''

    def create_user_table(self):
        statement = "CREATE TABLE IF NOT EXISTS users (" \
                    "userId SERIAL PRIMARY KEY , " \
                    "email varchar NOT NULL UNIQUE, " \
                    "username varchar NOT NULL UNIQUE, " \
                    "password varchar NOT NULL, " \
                    "is_admin BOOL NOT NULL DEFAULT FALSE)"
        self.cur.execute(statement)

    def create_products_table(self):
        statement = "CREATE TABLE IF NOT EXISTS products (" \
                    "product_id SERIAL PRIMARY KEY , " \
                    "username varchar NOT NULL UNIQUE, " \
                    "product_name varchar NOT NULL UNIQUE, " \
                    "unit_price INT NOT NULL, " \
                    "stock INT NOT NULL)"
        self.cur.execute(statement)

    def create_sales_table(self):
        statement = "CREATE TABLE IF NOT EXISTS sales (" \
                    "sale_id SERIAL PRIMARY KEY , " \
                    "product_id  INT NOT NULL , " \
                    "username varchar NOT NULL UNIQUE, " \
                    "product_name varchar NOT NULL UNIQUE, " \
                    "quantity INT NOT NULL UNIQUE, " \
                    "total INT NOT NULL)"
        self.cur.execute(statement)

    '''Functions to handle users and authentication'''

    def create_user(self, email, username, password, admin):
        self.cur.execute("INSERT INTO users (email, username, password, is_admin) "
                         "VALUES( '{}', '{}', '{}', '{}');".format
                         (email, username, password, admin))

    def find_by_username(self, username):
        query = "SELECT * FROM users WHERE username=%s"
        self.cur.execute(query, (username,))
        user = self.cur.fetchone()
        return user

    def find_by_email(self, email):
        query = "SELECT * FROM users WHERE email=%s"
        self.cur.execute(query, (email,))
        user = self.cur.fetchone()
        return user

    def view_user(self):
        statement = "SELECT name, username, email, is_admin FROM users;"
        self.cur.execute(statement)
        rows = self.cur.fetchall()
        user_list = []
        user_dict = {}
        for row in rows:
            user_dict['email'] = row[1]
            user_dict['username'] = row[2]
            user_dict['is_admin'] = row[4]
            user_list.append(user_dict)
            user_dict = {}
        return user_list

    def auth_user(self, username):
        query = "SELECT * FROM users WHERE username=%s"
        self.cur.execute(query, (username,))
        user = self.cur.fetchone()
        userDict = {"username": user[2], "password": user[3], "is_admin": user[4]}
        return userDict

    def fetch_by_param(self, table_name, column, value):
        """Fetches a single a parameter from a specific table and column"""
        query = "SELECT * FROM {} WHERE {} = '{}'".format(
            table_name, column, value)
        self.cur.execute(query)
        row = self.cur.fetchone()
        return row

    '''Functions to handle Products'''

    def create_product(self, username, product_name, unit_price, stock):
        self.cur.execute("INSERT INTO products (username, product_name, unit_price, stock) "
                         "VALUES( '{}', '{}', '{}', '{}');".format
                         (username, product_name, unit_price, stock))


    '''Function to get all products'''
    def view_all_products(self):
        statement = "SELECT product_name, unit_price, stock FROM products;"
        self.cur.execute(statement)
        rows = self.cur.fetchall()
        product_list = []
        product_dict = {}
        for row in rows:
            product_dict['product_name'] = row[0]
            product_dict['unit_price'] = row[1]
            product_dict['stock'] = row[2]
            product_list.append(product_dict)
            product_dict = {}
        return product_list

        return rows

    """Trancating test database"""

    def trancate_table(self):
        self.cur.execute("DROP TABLE users;")
        self.cur.execute("DROP TABLE products;")
        self.cur.execute("DROP TABLE sales;")
