import requests
BASE = "http://127.0.0.1:5000/"

responce = requests.get(BASE + "7").json()

print(f'My name is {responce["name"]} and my age is {responce["age"]} and I am from {responce["location"]}')