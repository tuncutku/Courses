from flask import Flask, render_template, request, session, make_response
from flask_restful import Api
from flask_jwt import JWT

from database.db import db

__author__ = "tuncutku"

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["PROPAGATE_EXCEPTIONS"] = True
app.secret_key = "tunc"
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


# jwt = JWT(app, authenticate, identity)  # /auth

# api.add_resource(Store, "/")


@app.route("/")
def home_template():
    return render_template("home.html")


if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)
