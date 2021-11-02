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