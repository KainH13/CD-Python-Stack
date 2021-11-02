from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.response import Response

@app.route('/')
def index():
    return render_template("form.html")

@app.route('/submit', methods=['POST'])
def log_data():
    data = {
        "name": request.form["name"],
        "location": request.form["dojo_location"],
        "language": request.form["fav_lang"],
        "comment": request.form["comments"]
    }

    # validations
    if not Response.validate_response(request.form):
        return redirect('/')

    Response.create(data)

    print("entered submit function")
    session['name'] = request.form['name']
    print(f"{session['name']}")
    session['dojo_location'] = request.form['dojo_location']
    print(f"{session['dojo_location']}")
    session['fav_lang'] = request.form['fav_lang']
    print(f"{session['fav_lang']}")
    session['comments'] = request.form['comments']
    print(f"{session['comments']}")
    return redirect('/results')

@app.route('/results')
def show_results():
    return render_template("results.html")