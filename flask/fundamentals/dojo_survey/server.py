from logging import debug
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'dont look at this!'


@app.route('/')
def index():
    return render_template("form.html")

@app.route('/submit', methods=['POST'])
def log_data():
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



if __name__ == "__main__":
    app.run(debug=True)