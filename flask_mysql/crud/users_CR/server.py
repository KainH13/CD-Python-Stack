from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/users')
def users():
    

    return render_template("read.html")

@app.route('/user_creation')
def create_user():
    return render_template("create.html")


if __name__ == "__main__":
    app.run(debug=True)