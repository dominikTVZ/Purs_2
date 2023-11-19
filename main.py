from flask import Flask, request, redirect, url_for, make_response

app = Flask('prva aplikacija')
temperature = []

#1.zad
@app.get('/')
def home():
    return 'Pocetna stranica'

@app.get('/login')
def login():
    return 'Stranica za prijavu'

#2.zad
@app.post('/login')
def check():
    username = request.json.get('username')
    password = request.json.get('password')

    if username == 'PURS' and password == '1234':
        return redirect(url_for('home'))
    else: 
        return redirect(url_for('login'))
 
 #3.zad   
@app.post('/temperatura')
def temp_add():
    global temperature
    if request.json.get('temperatura'):
        temperature.append(request.json.get('temperatura'))
        return('Uspješno ste dodali ključ', 201)
    else:
        return('Niste upisali ispravan ključ', 404)

#4.zad
@app.get('/temperatura')
def temp_print():
    global temperature
    if len(temperature) > 0:
        json = {'temperatura' : temperature[-1]}
        return json, 200
    else:
        return 'Nema temperature u listi'

#5.zad
@app.delete('/temperatura')
def temp_delete():
    global temperature
    temperatura =  request.args.get('id')

    if temperatura is not None:
        temperature.remove(temperatura)
        return 'Uspješno ste izrbisali temperaturu', 202
    else:
        return 'Unesli ste krive podatke', 404

app.run(host = '0.0.0.0', port = 80)









