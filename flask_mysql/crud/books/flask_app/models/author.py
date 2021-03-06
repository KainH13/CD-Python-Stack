from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book


class Author:
    db = 'books_schema'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL(cls.db).query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors

    @classmethod
    def create(cls, data):
        query = "INSERT INTO authors (first_name, last_name) VALUES(%(first_name)s, %(last_name)s);"
        return connectToMySQL(cls.db).query_db(query, data)


    # incomplete -- will not work
    @classmethod
    def get_author_with_books(cls, data):
        query = "SELECT * FROM authors LEFT JOIN favorites on favorites.author_id = authors.id LEFT JOIN books on books.id = favorites.book_id WHERE authors.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        author = cls(results[0])
        for row_from_db in results:
            book_data = {
                "id": row_from_db["books.id"],
                "title": row_from_db["title"],
                "created_at": row_from_db["books.created_at"],
                "updated_at": row_from_db["books.updated_at"],
                "num_of_pages": row_from_db["num_of_pages"]
            }
            author.books.append( book.Book(book_data))
        return author

    @classmethod
    def add_favorite(cls, data):
        query = "INSERT INTO favorites (book_id, author_id) VALUES(%(book_id)s, %(author_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)