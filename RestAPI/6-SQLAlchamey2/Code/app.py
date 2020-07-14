from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from resources.user import UserRegister
from resources.item import Item, ItemList
from db import db

from security import authenticate, identity
import os

path = "/Users/tuncutku/Desktop/Courses/RestAPI/5-SQLAlchamey/Code/"

os.chdir(path)

app = Flask(__name__)
app.secret_key = "tunc"
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")

if __name__ == "__main__":
    db.init_app()
    app.run(port=5000, debug=True)
