import requests

url = 'https://petstore.swagger.io/v2/user/createWithArray'

headers = {
    'accept: application/json',
    'Content-Type: application/json'
}

data = [
  {
    "id": 0,
    "username": "Mister A",
    "firstName": "Artur",
    "lastName": "Ant",
    "email": "AA@mail.ru",
    "password": "qwerty",
    "phone": "89123456789",
    "userStatus": 0
  }
]

res = requests.post(url, data, headers=headers)

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))


