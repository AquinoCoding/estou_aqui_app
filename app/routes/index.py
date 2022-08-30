from app import app
from flask import render_template

from app.services.listen_to_voice import liste_voice

@app.route("/")
def index():
    
    liste_voice('Bem vindo ao estou aqui app. Seu app de mobilidade')
    
    return render_template('index.html')

@app.route("/logout")
def logout(): 
    return render_template('login.html')
