from app import app
from flask import render_template

from app.models.geo_localization import get_location

@app.route("/geo-localizacao")
def geo_localizacao(): 
    return render_template('geo_localizacao.html', localization=get_location())