import re
from flask_app.models.user import User
from flask_app import app
from flask import render_template, jsonify, request, redirect

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users')
def users():
    return jsonify(User.get_all_json())

@app.route('/create/user', methods=['POST'])
def create_user():
    print(request.form)
    data = {
        'user_name' : request.form['user_name'],
        'email' : request.form['email']
    }
    return jsonify(User.save(data))
    