from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

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
        self.likes = []
        self.num_likes = 0

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
        query = "UPDATE recipes SET name = %(name)s, under_30 = %(under_30)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s WHERE recipes.id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_recipe_with_likes(cls, data):
        query = "SELECT * FROM recipes LEFT JOIN likes ON recipes_id = recipes.id LEFT JOIN users ON users.id = likes.users_id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        recipe = cls(results[0])
        num_likes = 0

        # check for at least 1 like
        if results[0]['likes.id'] != None:
            for row in results:
                user_data = {
                    "id" : row["users.id"],
                    "first_name" : row["first_name"],
                    "last_name" : row["last_name"],
                    "email" : row["email"],
                    "password" : row["password"],
                    "created_at" : row["users.created_at"],
                    "updated_at" : row["users.updated_at"],
                }
                recipe.likes.append(user.User(user_data))
                num_likes += 1
            recipe.num_likes = num_likes
            return recipe
        else:
            return recipe

    @classmethod
    def add_like(cls, data):
        query = "INSERT INTO likes (users_id, recipes_id) VALUES(%(users_id)s, %(recipes_id)s)"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def remove_like(cls, data):
        query = "DELETE FROM likes WHERE users_id = %(users_id)s AND recipes_id = %(recipes_id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)