import json
import requests

url = "https://reqres.in/api"

head = {"x-api-key": "reqres-free-v1", "Content-Type": "application/json"}

file = open("./users.json")
payload = json.load(file)

# {"name": "morpheus", "job": "leader"}

# list_users = requests.get(url=url + "/users?page=2")

# single_users = requests.get(url=url + "/users/2")

# delay_res = requests.get(url=url + "/users?delay=3", headers=head)

create_user = requests.post(url=url + "/users", headers=head, json=payload)

print(create_user.json())
