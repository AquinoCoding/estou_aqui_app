from app import app
from flask import render_template

from app.services.listen_to_voice import liste_voice

@app.route("/login")
def login():
        
    liste_voice('Voce está na pagina de login')
        
    return render_template('login.html', titulo='Login')