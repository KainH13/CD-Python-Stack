from werkzeug import datastructures
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.book import Book
from flask_app.models.author import Author

@app.route('/books')
def books_page():
    books = Book.get_all()
    return render_template('books.html', books=books)

@app.route('/books/book/create', methods=["POST"])
def create():
    data = {
        "title": request.form["title"],
        "num_of_pages": request.form["num_of_pages"]
    }
    Book.create(data)
    return redirect('/books')

@app.route('/books/<int:id>')
def show_book(id):
    data = {
        "id": id
    }
    book = Book.get_book_with_authors(data)
    authors = Author.get_all()
    return render_template('book_show.html', book=book, authors=authors)

@app.route('/books/book/add_author', methods=["POST"])
def add_author():
    data = {
        "book_id": request.form["book_id"],
        "author_id": request.form["author_id"]
    }
    Book.add_author(data)
    return redirect(f'/books/{request.form["book_id"]}')