from app import app
from flask import render_template, request, url_for, redirect

from app.models.geo_localization import get_location

from app.services.listen_to_voice import liste_voice


@app.route("/geo-localizacao")
def geo_localizacao():
    
    liste_voice(f'Voce está na pagina de geo localização, aqui voce pode pesquisar para onde voce quer ir.    Sua localizção atual é {get_location(None)}')

    return render_template('geo_localizacao.html', localization=get_location(None), titulo="APP")

@app.route("/geo-localizacao/<localization>")
def geo_localizacao_find(localization):
    
    #liste_voice(f'Voce pesquisou {localization}, estou buscando essa localização')
    
    return render_template('geo_localizacao.html', localization=get_location(localization), titulo="APP")

@app.route("/geo-localizacao-post", methods=["POST"])
def geo_localizacao_post():
    
    localization = request.form.get('search')
    
    liste_voice(f'Voce pesquisou {localization}, estou buscando essa localização')

    return redirect(url_for('geo_localizacao_find', localization=localization))
