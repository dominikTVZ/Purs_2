from flask import Flask, request, redirect, url_for, make_response

app = Flask('prva aplikacija')


@app.get('/')
def home():
    return 'Pocetna stranica'

@app.get('/login')
def login():
    return 'Stranica za prijavu'

@app.post('/login')
def check():
    username = request.json.get('username')
    password = request.json.get('password')

    if username == 'PURS' and password == '1234':
        return redirect(url_for('home'))
    else: 
        return redirect(url_for('login'))
    



app.run(host = '0.0.0.0', port = 80)