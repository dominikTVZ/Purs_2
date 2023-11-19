import requests

id = {'temeperatura' : 12}
response = requests.delete('http://localhost:80/temperatura', params = id)
print(response.text)