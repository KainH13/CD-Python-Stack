from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    db_name = 'recipes_db'

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.under_30 = data['under_30']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.likes = 0

    def get_likes(self):
        query = f"SELECT * FROM recipes LEFT JOIN likes ON recipes_id = recipes.id LEFT JOIN users ON users.id = likes.users_id WHERE recipes.id = {self.id}"
        results = connectToMySQL('recipes_db').query_db(query)
        self.likes = len(results)
        return self

    @classmethod
    def create(cls, data):
        query = "INSERT INTO recipes (name, under_30, description, instructions, date_made, users_id) VALUES(%(name)s, %(under_30)s, %(description)s, %(instructions)s, %(date_made)s, %(users_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        return connectToMySQL(cls.db_name).query_db(query)
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name = %(name)s, under_30 = %(under_30)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def add_like(cls, data):
        query = "INSERT INTO likes (users_id, recipes_id) VALUES(%(users_id)s, %(recipes_id)s)"
        return connectToMySQL(cls.db_name).query_db(query, data)
    