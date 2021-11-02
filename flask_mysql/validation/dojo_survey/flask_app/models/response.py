from flask.helpers import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Response():
    db_name = 'dojo_survey_schema'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.language = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = '''INSERT INTO responses (name, location, language, comment)
        VALUES(%(name)s, %(location)s, %(language)s, %(comment)s)'''
        return connectToMySQL(cls.db_name).query_db(query, data)

    @staticmethod
    def validate_response(response):
        is_valid = True
        if len(response['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if response['dojo_location'] == "Select your location":
            flash("Must choose a location.")
            is_valid = False
        if response['fav_lang'] == "Select your favorite programming language":
            flash("Must choose a favorite language.")
            is_valid = False
        if len(response['comments']) < 3:
            flash("Comment must be longer than 3 characters.")
            is_valid = False
        return is_valid