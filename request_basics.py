import requests

#get request
# responce = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# print(responce.status_code)

# print(responce.json())

#post request

# data = {
#     "Name" : "Koko",
#     "Age" : 12,
#     "Place" : "Tokyo"
# }
# responce = requests.post("https://jsonplaceholder.typicode.com/posts",json=data)

# print("Status code :",responce.status_code)
# print("Responce :",responce.json())

#Error Handling

# try:
#     response = requests.get("https://jsonplaceholder.typicode.com/invalid-url")
#     response.raise_for_status()
# except requests.exceptions.HTTPError as err:
#     print(f"HTTP Error :{err}")

#Task 1:Fetch a list of all the users

# response = requests.get("https://jsonplaceholder.typicode.com/users")

# users = response.json()

# for user in users:
#     print(user["name"])

#Task 2: Use POST to create a new post with a title and body.

# data = {
#     "Name" : "lufa",
#     "Age" : 16,
#     "Place" : "Rio"
# }
# response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)

# print(response.status_code)
# print(response.json())

#Task 3: Handle an invalid endpoint error gracefully

# try:
#     response = requests.get("https://jsonplaceholder.typicode.com/invalid-url")
#     response.raise_for_status()
# except Exception as err:
#     print(f"Error :{err}")