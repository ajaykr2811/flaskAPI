from flask import Flask, request
import datetime
app =  Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)