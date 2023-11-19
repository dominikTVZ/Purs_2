import requests

rjecnik = {'temperatura': 12}
response = requests.post('http://localhost:80/temperatura', json = rjecnik)
print(response.text)