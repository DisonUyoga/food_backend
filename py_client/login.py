import requests

endpoint="http://localhost:8000/api/token/"


data={
"username": "Dison",
"password":"disonnnnnnn123"
}

response=requests.post(endpoint, json=data)

print(response.json())