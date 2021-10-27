from flask import Flask, render_template, request, redirect
from user import User

app = Flask(__name__)


@app.route('/users')
def users():
    users = User.get_all()
    print(users)
    return render_template("read.html", users=users)

@app.route('/users/user/<int:id>')
def show_user(id):
    data = {
        "id": id
    }
    user = User.get_one(data)
    print(user)
    return render_template('show.html', user=user[0])

@app.route('/users/new')
def user_creation():
    return render_template("create.html")

@app.route('/users/creation', methods=["POST"])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.create(data)
    return redirect('/users')

@app.route('/users/user/<int:id>/edit')
def edit_user(id):
    data = {
        "id": id
    }
    user = User.get_one(data)
    print(user)
    return render_template("edit.html", user=user[0])

@app.route('/users/user/edit/make_change', methods=["POST"])
def make_edit():
    data = {
        "id": request.form["id"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.update(data)
    return redirect(f'/users/user/{request.form["id"]}')

@app.route('/users/user/<int:id>/delete')
def remove_user(id):
    data = {
        "id": id
    }
    User.delete(data)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)