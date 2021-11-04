from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db_name = 'user_login_db'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT *  FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.db_name).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @classmethod
    def get_all_emails(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db_name).query_db(query)
        all_emails = []
        for entry in results:
            all_emails.append(entry['email'])
        return all_emails

    @staticmethod
    def validate_registration(user, used_emails):
        is_valid = True
        if len(user['first_name']) < 2 or not user['first_name'].isalpha():
            flash("First Name must be at least 2 characters and contain only letters.", "registration_error")
            is_valid = False
        if len(user['last_name']) < 2 or not user['last_name'].isalpha():
            flash("Last Name must be at least 2 characters and contain only letters.", "registration_error")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Email Address!", "registration_error")
            is_valid = False
        if user['email'] in used_emails:
            flash("Email already in use.", "registration_error")
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash("Passwords did not match.", "registration_error")
            is_valid = False

        # Checking password security    
        password_secure = False
        for x in user['password']:
            print(x)
            print(f"character is upper: {x.isupper()}")
            print(f"character is digit: {x.isdigit()}")
            if x.isupper():
                password_secure = True
            if x.isdigit():
                password_secure = True
        if not password_secure:
            flash("Password must contain at least one uppercase letter and number.", "registration_error")
            is_valid = False

        return is_valid