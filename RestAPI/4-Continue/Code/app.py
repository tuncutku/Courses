from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from user import UserRegister
from item import Item, ItemList

from security import authenticate, identity
import os

path = "/Users/tuncutku/Desktop/Courses/RestAPI/4-Continue/Code/"

os.chdir(path)

app = Flask(__name__)
app.secret_key = "tunc"
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
