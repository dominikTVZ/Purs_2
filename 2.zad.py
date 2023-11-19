import requests

rjecnik = {'username' : 'PURS', 'password': '1234'}
response = requests.post('http://localhost:80/login', json = rjecnik)
print(response.text)