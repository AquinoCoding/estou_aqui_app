from app import app
from flask import render_template

@app.route("/")
def index(): 
    return render_template('index.html')

@app.route("/modal")
def modal(): 
    return render_template('modal.html')
