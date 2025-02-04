import json
from flask import Flask, request

app = Flask(__name__)

DATA_FILE = "data.json"

def load_data():
    """Load data from the JSON file."""
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"lost_items": [], "found_items": [], "users": [], "claims": [], "notifications": []}

def save_data(data):
    """Save data back to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

data_store = load_data()

def response(message, data=None, status=200):
    res = {"message": message}
    if data is not None:
        res.update(data)
    return res, status

# Lost Items CRUD
@app.route("/lost-items", methods=["POST"])
def create_lost_item():
    """Create a new lost item entry and save it to data.json"""
    data = request.json
    data["id"] = len(data_store["lost_items"]) + 1
    data_store["lost_items"].append(data)
    save_data(data_store)
    return response("Lost item created successfully", {"item": data}, 201)

@app.route("/lost-items", methods=["GET"])
def get_lost_items():
    """Retrieve all lost items"""
    return response("Lost items retrieved successfully", {"lost_items": data_store["lost_items"]})

@app.route("/lost-items/<int:id>", methods=["GET"])
def get_lost_item(id):
    """Retrieve a specific lost item by ID"""
    item = next((item for item in data_store["lost_items"] if item["id"] == id), None)
    return response("Item found", {"item": item}) if item else response("Item not found", status=404)

@app.route("/lost-items/<int:id>", methods=["PUT"])
def update_lost_item(id):
    """Update an existing lost item"""
    data = request.json
    for item in data_store["lost_items"]:
        if item["id"] == id:
            item.update(data)
            save_data(data_store)
            return response("Lost item updated successfully", {"item": item})
    return response("Item not found", status=404)

@app.route("/lost-items/<int:id>", methods=["DELETE"])
def delete_lost_item(id):
    """Delete a lost item by ID"""
    data_store["lost_items"] = [item for item in data_store["lost_items"] if item["id"] != id]
    save_data(data_store)
    return response("Lost item deleted successfully")

# Found Items CRUD
@app.route("/found-items", methods=["POST"])
def create_found_item():
    """Create a new found item entry"""
    data = request.json
    data["id"] = len(data_store["found_items"]) + 1
    data_store["found_items"].append(data)
    save_data(data_store)
    return response("Found item created successfully", {"item": data}, 201)

@app.route("/found-items", methods=["GET"])
def get_found_items():
    """Retrieve all found items"""
    return response("Found items retrieved successfully", {"found_items": data_store["found_items"]})

@app.route("/found-items/<int:id>", methods=["GET"])
def get_found_item(id):
    """Retrieve a specific found item by ID"""
    item = next((item for item in data_store["found_items"] if item["id"] == id), None)
    return response("Item found", {"item": item}) if item else response("Item not found", status=404)

@app.route("/found-items/<int:id>", methods=["PUT"])
def update_found_item(id):
    """Update an existing found item"""
    data = request.json
    for item in data_store["found_items"]:
        if item["id"] == id:
            item.update(data)
            save_data(data_store)
            return response("Found item updated successfully", {"item": item})
    return response("Item not found", status=404)

@app.route("/found-items/<int:id>", methods=["DELETE"])
def delete_found_item(id):
    """Delete a found item by ID"""
    data_store["found_items"] = [item for item in data_store["found_items"] if item["id"] != id]
    save_data(data_store)
    return response("Found item deleted successfully")

# User CRUD
@app.route("/users", methods=["POST"])
def create_user():
    """Register a new user"""
    data = request.json
    data["id"] = len(data_store["users"]) + 1
    data_store["users"].append(data)
    save_data(data_store)
    return response("User created successfully", {"user": data}, 201)

@app.route("/users", methods=["GET"])
def get_users():
    """Retrieve all users"""
    return response("Users retrieved successfully", {"users": data_store["users"]})

@app.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    """Retrieve a user by ID"""
    user = next((user for user in data_store["users"] if user["id"] == id), None)
    return response("User found", {"user": user}) if user else response("User not found", status=404)

@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    """Update an existing user"""
    data = request.json
    for user in data_store["users"]:
        if user["id"] == id:
            user.update(data)
            save_data(data_store)
            return response("User updated successfully", {"user": user})
    return response("User not found", status=404)

@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    """Delete a user by ID"""
    data_store["users"] = [user for user in data_store["users"] if user["id"] != id]
    save_data(data_store)
    return response("User deleted successfully")

if __name__ == "__main__":
    app.run(debug=True)
