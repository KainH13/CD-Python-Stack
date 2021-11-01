# name should be plural
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/authors')
def authors_page():
    authors = Author.get_all()
    return render_template('authors.html', authors=authors)

@app.route('/authors/author/create', methods=["POST"])
def create_author():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"]
    }
    Author.create(data)
    return redirect('/authors')

@app.route('/authors/<int:id>')
def show_author(id):
    data = {
        "id": id
    }
    author = Author.get_author_with_books(data)
    books = Book.get_all()
    return render_template('author_show.html', author=author, books = books)

@app.route('/authors/author/add_favorite', methods=["POST"])
def add_favorite():
    data = {
        "book_id": request.form["book_id"],
        "author_id": request.form["author_id"]
    }
    Author.add_favorite(data)
    return redirect(f'/authors/{request.form["author_id"]}')
