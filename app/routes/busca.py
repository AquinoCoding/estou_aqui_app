from app import app
from flask import render_template

@app.route("/buscar")
def buscar(): 
    return render_template('buscar.html', titulo='Buscar Linha')