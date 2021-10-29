from flask_app.config.mysqlconnection import connectToMySQL


class Book:
    db = 'books_schema'

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.num_of_pages = data['num_of_pages']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(cls.db).query_db(query)
        books = []
        for book in results:
            books.append(cls(book))
        return books