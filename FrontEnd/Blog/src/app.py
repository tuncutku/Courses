from flask import Flask, render_template, request, session, make_response
from flask_restful import Api

from models.user import User

__author__ = "tuncutku"

app = Flask(__name__)
app.secret_key = "tunc"
api = Api(app)


# @app.route("/")
# def home_template():
#     return render_template("home.html")


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/login", methods=["POST", "GET"])
def profile():
    email = request.form["email"]
    password = request.form["password"]
    User.register(email, password)
    return render_template("profile.html", email=email)


if __name__ == "__main__":
    # create_tables()
    app.run(port=5000, debug=True)
