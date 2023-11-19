import requests

response = requests.get('http://localhost:80/temperatura')
print(response.text)