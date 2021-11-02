from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    db_name = 'email_validation_db'

    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO emails (email) VALUES(%(email)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL(cls.db_name).query_db(query)
        emails = []
        for email in results:
            emails.append(cls(email))
        return emails

    @classmethod
    def remove(cls, data):
        query = "DELETE FROM emails WHERE id = %(id)s"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @staticmethod
    def validate_email(email, used_emails):
        is_valid = True
        if not EMAIL_REGEX.match(email['email']):
            flash("Invalid Email Address!")
            is_valid = False
        if email['email'] in used_emails:
            flash("Email already validated.")
            is_valid = False
        return is_valid