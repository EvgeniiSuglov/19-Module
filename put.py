import requests

url = 'https://petstore.swagger.io/v2/user/Mister%20A'

headers = {
    'accept: application/json',
    'Content-Type: application/json'
}
data = {
  "id": 0,
  "username": "Mister A",
  "firstName": "Artur",
  "lastName": "Avangard",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 0
}

res = requests.put(url, data, headers=headers)

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))
