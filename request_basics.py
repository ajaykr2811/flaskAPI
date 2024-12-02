import requests

responce = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(responce.status_code)

print(responce.json())