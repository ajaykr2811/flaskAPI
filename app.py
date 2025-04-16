from flask import Flask, request, jsonify
import datetime
import validators
from pymongo import MongoClient
from flask_cors import CORS
from ariadne import graphql_sync, make_executable_schema
from ariadne.constants import PLAYGROUND_HTML
from resolvers import query, mutation

app =  Flask(__name__)

client = MongoClient("mongodb://localhost:27017")
#client = MongoClient("mongodb://fastapi.hrhgtpe.mongodb.net")
db = client['User']
collection = db['user_info']

@app.route("/")
def home():
    return "Hello Everyone !"

@app.route("/greet/<name>")
def greet(name):
    return f"Hello {name} how, how are you?"

@app.route("/user_info",methods=["POST"])
def user_info():
    request_data = request.get_json()
    req_params = ['name','location','age']
    missing_params = [params for params in req_params if params not in request_data]
    if missing_params:
        return f"reqired parameter {missing_params} are missing", 400
    collection.insert_one(request_data)
    
    return f"Hi {request_data.get('name','')} you born in {2024 - request_data['age']} in {request_data['location']}"

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

@app.route("/get_all_users",methods=["GET"])
def get_all_users():
    data = list(collection.find({},{"_id":0}))  # Use find() to get all documents and convert to list
    return jsonify(data), 200

@app.route("/update_email",methods=["POST"])
def update_email():
    request_data = request.get_json()
    user = collection.update_one(
        {'name':request_data['name']},
        {'$set' : {'email':request_data['email']}}
    )
    if user.matched_count:
        return {'message':f"Email id is updated for {request_data['name']}"}, 200
    else:
        return {'error': f"User name {request_data['name']} not found !!"}, 404

@app.route("/delete_user",methods=["DELETE"])
def delete_user():
    request_data = request.get_json()
    user = collection.delete_one(
        {'name':request_data['name']}
    )
    if user.deleted_count:
        return {'message':f"User info of {request_data['name']} deleted successfully "}, 200
    else:
        return {'error': f"User name {request_data['name']} not found !!"}, 404
    
#-------graphql--


# GraphQL schema
type_defs = open("schema.graphql").read()
schema = make_executable_schema(type_defs, [query,mutation])
CORS(app)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value={"request": request, "db": collection},  # pass mongo collection
        debug=True
    )
    return jsonify(result), 200

if __name__ == "__main__":
    app.run(debug=True)