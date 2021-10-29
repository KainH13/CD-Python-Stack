# name should be plural
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.author import Author

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
    author = Author.get_author_with_ninjas(data)
    return render_template('author_show.html', author=author)