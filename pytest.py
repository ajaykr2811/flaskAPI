import requests
BASE = "http://127.0.0.1:5000/"

# responce = requests.get(BASE + "7").json()

# print(f'My name is {responce["name"]} and my age is {responce["age"]} and I am from {responce["location"]}')

payload = {
    "count": 44,
    "page": 35,
    "other": "Something Great"
}
i = 1
while True:
    res = requests.get("https://httpbin.org/get", params=payload)
    if res.status_code == 200:
        break
    print(f"retrying {i}")
    i+=1

print(res.text)