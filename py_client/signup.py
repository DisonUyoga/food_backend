import requests

endpoint="http://localhost:8000/api/users/"


data={
"username": "Dison",
"email":"disonobudho233@gmail.com",
"password":"disonnnnnnn123"
}

response=requests.post(endpoint, json=data)

print(response.json())