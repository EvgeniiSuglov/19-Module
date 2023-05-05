import requests

url = 'https://petstore.swagger.io/v2/user/Mister%20A'

headers = {'accept: application/json'}

res = requests.get(url, headers=headers)

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))