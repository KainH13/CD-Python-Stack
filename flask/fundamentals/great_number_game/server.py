from flask import Flask, render_template, request, redirect, session
import random


app = Flask(__name__)
app.secret_key = 'hello from a land down under!'


@app.route('/')
def index():
    session['win'] == False
    session['high_guess'] = False
    session['low_guess'] = False
    session['out_guess'] = False
    if session['win'] == True:
        session["num"] = random.randint(1,100)
        print(f"Created new random number {session['num']}")
        return render_template("index.html")
    elif "num" in session:
        print(session["num"])
        return render_template("index.html")
    else:
        session["num"] = random.randint(1,100)
        print(f"Created new random number {session['num']}")
        return render_template("index.html")

@app.route('/check_number', methods=['GET', 'POST'])
def check_number():
    number = int(request.form['number'])
    if number == session['num']:
        print("We have a winner!")
        session['win'] = True
    elif number <= 100 and number >= 0:
        if number < session['num']:
            print("Too low, guess again...")
            session['win'] = False
            session['low_guess'] = True
        elif number > session['num']:
            print("Too high, guess again...")
            session['win'] = False
            session['high_guess'] = True
    else:
        print("Guess not between 1 and 100, guess again...")
        session['win'] = False
        session['out_guess'] = True
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)