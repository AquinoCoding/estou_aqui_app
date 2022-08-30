from app import app
from flask import render_template

@app.route("/formulario")
def formulario(): 
    return render_template('forms.html', titulo='Formulario')