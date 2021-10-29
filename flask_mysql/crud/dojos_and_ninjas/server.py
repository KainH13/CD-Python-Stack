from flask_app import app
# add from flask_app.controllers import controllers
from flask_app.controllers import dojos

if __name__ == "__main__":
    app.run(debug=True)