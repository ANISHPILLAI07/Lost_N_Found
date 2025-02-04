# Lost and Found API

This is a simple REST API built with Flask for managing lost and found items, users, and claims.  It stores data in a JSON file.

## Features

* **Lost Items:** Create, retrieve, update, and delete lost item entries.
* **Found Items:** Create, retrieve, update, and delete found item entries.
* **Users:** Create, retrieve, update, and delete user accounts.
* **Data Storage:** Data is persisted in a `data.json` file.

## Getting Started

### Prerequisites

* Python 3.x
* Flask: `pip install Flask`

### Installation

1. Clone the repository (or copy the code).
2. Create a file named `data.json` in the same directory as the script.  This file will store the data.  It can initially be an empty JSON object `{}`.

### Running the API

1. Navigate to the project directory in your terminal.
2. Run the Flask app: `python your_script_name.py` (replace `your_script_name.py` with the actual name of your Python file).

The API will be accessible at `http://127.0.0.1:5000/` (or whatever address Flask indicates in the terminal).

## API Endpoints

### Lost Items

* **`POST /lost-items`**: Create a new lost item.  Requires a JSON payload with item details.  Returns the created item with a 201 status code.
* **`GET /lost-items`**: Retrieve all lost items.  Returns a list of lost items.
* **`GET /lost-items/<int:id>`**: Retrieve a specific lost item by ID. Returns the item if found, 404 if not.
* **`PUT /lost-items/<int:id>`**: Update an existing lost item. Requires a JSON payload with updated item details. Returns the updated item if found, 404 if not.
* **`DELETE /lost-items/<int:id>`**: Delete a lost item by ID. Returns a 200 status code on success.

### Found Items

* **`POST /found-items`**: Create a new found item. Requires a JSON payload. Returns the created item with a 201 status code.
* **`GET /found-items`**: Retrieve all found items.
* **`GET /found-items/<int:id>`**: Retrieve a specific found item by ID.
* **`PUT /found-items/<int:id>`**: Update an existing found item. Requires a JSON payload.
* **`DELETE /found-items/<int:id>`**: Delete a found item by ID.

### Users

* **`POST /users`**: Create a new user. Requires a JSON payload. Returns the created user with a 201 status code.
* **`GET /users`**: Retrieve all users.
* **`GET /users/<int:id>`**: Retrieve a specific user by ID.
* **`PUT /users/<int:id>`**: Update an existing user. Requires a JSON payload.
* **`DELETE /users/<int:id>`**: Delete a user by ID.

## Data Structure (data.json)

The `data.json` file stores the data in the following format:

```json
{
  "lost_items": [
    {"id": 1, "name": "Wallet", "description": "Brown leather wallet", ...},
    ...
  ],
  "found_items": [
    {"id": 1, "name": "Keys", "location": "Park", ...},
    ...
  ],
  "users": [
    {"id": 1, "username": "john_doe", "email": "[email address removed]", ...},
    ...
  ],
  "claims": [],  // Placeholder for future claim management
  "notifications": [] // Placeholder for future notification system
}
