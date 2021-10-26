from flask import Flask, render_template, request, redirect
from user import User

app = Flask(__name__)


@app.route('/users')
def users():
    users = User.get_all()
    print(users)
    return render_template("read.html", users=users)

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

if __name__ == "__main__":
    app.run(debug=True)