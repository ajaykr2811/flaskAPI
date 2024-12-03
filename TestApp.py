from flask import Flask, request
from flask_restful import Api, Resource
import os,json

app = Flask(__name__)
api = Api(app)

users_data = {
    "1": {"name": "Alice", "age": 25, "location": "New York"},
    "2": {"name": "Bob", "age": 30, "location": "Los Angeles"},
    "3": {"name": "Charlie", "age": 22, "location": "Chicago"},
    "4": {"name": "David", "age": 28, "location": "Houston"},
    "5": {"name": "Eve", "age": 35, "location": "Phoenix"},
    "6": {"name": "Frank", "age": 27, "location": "Philadelphia"},
    "7": {"name": "Grace", "age": 29, "location": "San Antonio"},
    "8": {"name": "Hank", "age": 24, "location": "San Diego"},
    "9": {"name": "Ivy", "age": 31, "location": "Dallas"},
    "10": {"name": "Jack", "age": 26, "location": "San Jose"}
}

'''
# File to store user data
USER_DATA_FILE = "users_data.json"

# Function to load data from JSON file
def load_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as file:
            try:
                return json.load(file) or {}  # Return {} if the file is empty
            except json.JSONDecodeError:
                return {}  # Return an empty dict if JSON is invalid
    return {}

# Function to save data to JSON file
def save_data(data):
    with open(USER_DATA_FILE, "w") as file:
        json.dump(data, file)

# Load initial data
users_data = load_data()
'''

class hello_world(Resource):
    def get(self,user_id):
        return users_data.get(user_id,{"error": "user not found"}), 200
    
    def post(self):
        data = request.get_json()
        user_id = len(users_data) + 1
        users_data[user_id] = {
            "name": data["name"],
            "age": data["age"],
            "location": data["location"]
        }
        return {"info": f"user added with ID {user_id}"}, 201
    
api.add_resource(hello_world, "/<string:user_id>","/")

if __name__ == "__main__":
    app.run(debug=True)