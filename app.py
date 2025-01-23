from flask import Flask, request
import datetime
import validators
from pymongo import MongoClient

app =  Flask(__name__)

client = MongoClient("mongodb://localhost:27017")
db = client['flask_mongo_db']
collection = db['users']

@app.route("/")
def home():
    return "Hello Everyone !"

@app.route("/greet/<name>")
def greet(name):
    return f"Hello {name} how, how are you?"

@app.route("/user_info/")
def user_info():
    name = request.args.get("Name", type=str)
    age = request.args.get("Age", type=int)
    place = request.args.get("Place", type=str)
    
    return f'Hi {name} you born in {2024 - age} in {place}'

@app.route('/square/<num>')
def square(num):
    return {
        "result" : int(num)**2,
        "status" : "success",
        "code" : 200
    }, 200

@app.route('/div')
def div():
    num1 = request.args.get("num1", type=int)
    num2 = request.args.get("num2", type=int)
    if num2 < 1:
        return "num2 should be greater then 0", 200
    
    return f"{num1} divided by {num2} is {num1/num2}"

@app.route("/info")
def info():
    return {
        "Name" : "Koko",
        "Data" : datetime.datetime.now(),
        "Progress" : "Day 2 complete"
    }

@app.route("/email_validation")
def email_validation():
    email_id = request.args.get("email_id",type=str)
    response = {
        "email_id": email_id,
        "valid": False
    }

    if validators.email(email_id):
        response["valid"] = True
        return response, 200
    
    return response, 400

@app.route("/test_db_connection", methods=['GET'])
def test_db_connection():
    try:
        client.server_info()
        return {'message': 'Connected to MongoDB'}, 200
    except Exception as e:
        return {'error': str(e)}, 500


if __name__ == "__main__":
    app.run(debug=True)