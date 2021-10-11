from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:thing>')
def say_thing(thing):
    if thing == "flask":
        return "Hi Flask!"
    elif thing == "michael":
        return "Hi Michael!"
    elif thing == "john":
        return "Hi John!"
    else:
        return "That's not a 'thing' I recognize!"
    
@app.route('/repeat/<int:num>/<string:thing>')
def repeat_thing(num, thing):
    return f"{thing * num}"

@app.route('/<route>')
def check_route(route):
    if route not in ["/dojo", "/say/<string:thing>", "/repeat/<int:num>/<string:thing>"]:
        return "sorry, I don't recognize that route"

if __name__ == "__main__":
    app.run(debug=True)