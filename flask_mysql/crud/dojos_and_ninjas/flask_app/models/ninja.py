from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    db = 'dojos_and_ninjas_schema'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.age = data['age']

    @classmethod
    def create(cls, data):
        query = '''INSERT INTO ninjas (first_name, last_name, age, dojo_id)
        VALUES(%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)'''
        return connectToMySQL(cls.db).query_db(query, data)