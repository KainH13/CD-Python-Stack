from logging import debug
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'test key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        if 'count' in session:
            session['count'] += 1
        else:
            session['count'] = 1
    elif request.method == 'POST':
        if request.form.get('add_two') == 'Add Two':
            if 'count' in session:
                session['count'] += 2
            else:
                session['count'] = 2
        elif request.form.get('clear') == 'Clear':
            session.clear()
            return redirect('/')
    return render_template("index.html")

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)