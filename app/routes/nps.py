from app import app
from flask import render_template

@app.route("/nps")
def nps():
    
    texts = ['Gostei', 'Legal', 'Bacana', 'Muito bom']
    
    return render_template('nps.html', titulo='Feedbacks do Cliente', texts=texts)