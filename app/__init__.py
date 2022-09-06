__version__ = '0.1.0'

from flask import Flask

app = Flask(__name__)

app.secret_key = '66e0c4a852d3b55ca598abf7792086b2'

from app.routes import index
from app.routes import localizacao_atual
