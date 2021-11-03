from flask_app import app
from flask import render_template, redirect, request, session, flash

@app.route('/')
def login_registration_page():
    return render_template('login_registration.html')
