from flask import Flask, render_template, request, session, make_response
from flask_restful import Api

from models.user import User

__author__ = "tuncutku"

app = Flask(__name__)
app.secret_key = "tunc"
api = Api(app)


@app.route("/")
def home_template():
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/auth/register", methods=["POST", "GET"])
def auth_register():
    email = request.form["email"]
    password = request.form["password"]
    User.register(email, password)
    session["email"] = password
    return render_template("profile.html", email=session["email"])


@app.route("/auth/login", methods=["POST", "GET"])
def auth_login():
    email = request.form["email"]
    password = request.form["password"]
    if User.login_valid(email, password):
        User.login(email)
    else:
        session["email"] = None

    return render_template("profile.html", email=session["email"])


@app.route("/blogs/<string:user_id>")
def blogs(user_id):
    user = User.get_by_id(user_id)
    user.get

    return render_template("user_blogs.html", email=session["email"])


if __name__ == "__main__":
    # create_tables()
    app.run(port=5000, debug=True)
