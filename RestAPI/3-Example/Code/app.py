from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = "tunc"
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = []


class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        "price", type=float, required=True, help="this field cannot left blank"
    )

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x["name"] == name, items), None)
        return {"item": item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x["name"] == name, items), None):
            return (
                {"message": "An item with the name {} already exists".format(name)},
                400,
            )
        data = request.get_json()  # silent=True can be used to prevent error
        item = {"name": name, "price": data["price"]}
        items.append(item)
        return item, 201  # 202 accepted - data is processed

    def delete(self, name):
        global items
        items = list(filter(lambda x: x["name"] != name, items))
        return {"message": "{} has been deleted".format(name)}

    def put(self, name):
        data = parser.parse_args()  # request.get_json()
        item = next(filter(lambda x: x["name"] == name, items), None)
        if item is None:
            item = {"name": name, "price": data["price"]}
            items.append(item)
        else:
            item.update(data)
        return item


class ItemList(Resource):
    def get(self):
        return {"items": items}


api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")

app.run(port=5000, debug=True)
