from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# POST - Used to receive data
# GET - Used to send data back only

# Initial Stores
stores = [{"name": "My Store", "items": [{"name": "my item", "price": 15.99}]}]


@app.route("/")
def home():
    return render_template("index.html")


# POST /store data: {name:}
@app.route("/store", methods=["POST"])
def create_store():
    requestData = request.get_json()
    new_store = {"name": requestData["name"], "items": []}
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
@app.route("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
    return jsonify({"message": "store not found"})


# GET /store
@app.route("/store")
def get_stores():
    return jsonify({"store": stores})


# POST /store/<string:name>/item {name: ,price:}
@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
    requestData = request.get_json()
    for store in stores:
        if store["name"] == name:
            newItem = {"name": requestData["name"], "price": requestData["price"]}
            store["items"].append(newItem)
            return jsonify(store)
    return jsonify({"message": "store not found"})


# GET /store/<string:name>/item
@app.route("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify({"items": store["items"]})
    return jsonify({"message": "store not found"})


app.run(port=5000)
