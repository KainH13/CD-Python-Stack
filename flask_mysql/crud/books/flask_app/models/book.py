from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author


class Book:
    db = 'books_schema'

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.num_of_pages = data['num_of_pages']
        self.authors = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(cls.db).query_db(query)
        books = []
        for book in results:
            books.append(cls(book))
        return books

    @classmethod
    def create(cls, data):
        query = "INSERT INTO books (title, num_of_pages) VALUES(%(title)s, %(num_of_pages)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_book_with_authors(cls, data):
        query = "SELECT * FROM books LEFT JOIN favorites on favorites.book_id = books.id LEFT JOIN authors on authors.id = favorites.author_id WHERE books.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        book = cls(results[0])
        for row_from_db in results:
            print(row_from_db)
            author_data = {
                "id": row_from_db["authors.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "created_at": row_from_db["authors.created_at"],
                "updated_at": row_from_db["authors.updated_at"],
            }
            book.authors.append( author.Author(author_data))
        return book

    @classmethod
    def add_author(cls, data):
        query = "INSERT INTO favorites (book_id, author_id) VALUES(%(book_id)s, %(author_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)