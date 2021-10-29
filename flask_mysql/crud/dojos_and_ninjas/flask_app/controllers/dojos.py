# name should be plural
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo

@app.route('/dojos')
def dojos_page():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('dojos.html', dojos=dojos)

@app.route('/dojos/dojo/create', methods=["POST"])
def add_dojo():
    data = {
        "name": request.form["dojo_name"]
    }
    Dojo.create(data)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template('show.html', dojo=dojo)
