import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash
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
        try:
            statement = "CREATE TABLE IF NOT EXISTS users (" \
                        "userId SERIAL PRIMARY KEY , " \
                        "email varchar NOT NULL UNIQUE, " \
                        "username varchar NOT NULL UNIQUE, " \
                        "password varchar NOT NULL, " \
                        "is_admin BOOL NOT NULL DEFAULT FALSE)"
            self.cur.execute(statement)
        except psycopg2.DatabaseError as e:
            if self.conn:
                self.conn.rollback()
            raise e

    '''Functions to handle users and authentication'''

    def create_user(self, data):
        try:
            self.cur.execute("INSERT INTO users (email, username, password, is_admin) "
                             "VALUES( '{}', '{}', '{}', '{}');".format
                             (data['email'], data['username'],
                              generate_password_hash(data['password'], method='sha256'), data['is_admin']))

        except psycopg2.DatabaseError:
            if self.conn:
                self.conn.rollback()
        finally:
            self.conn.close()

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
        print(userDict)
        return userDict

    def fetch_by_param(self, table_name, column, param):
        """Fetches a single a parameter from a specific table and column"""
        query = "SELECT * FROM {} WHERE {} = '{}'".format(
            table_name, column, param)
        self.cur.execute(query)
        row = self.cur.fetchone()
        return row

