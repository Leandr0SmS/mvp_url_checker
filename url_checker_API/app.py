from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, jsonify

from model.url_check import UrlModel
from schemas import *
from logger import logger
from flask_cors import CORS

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(
    name="Documentação", 
    description="Seleção de documentação: Swagger, Redoc ou RapiDoc"
    )
url_data = Tag(
    name="URL Check",
    description="Recebe um string representando um URL"
)


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi,
    tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.get('/url_check', tags=[url_data],
         responses={"200": UrlChecked, "404": ErrorSchema})
def get_url_predic(query: UrlTest):
    """Recebe uma string url e retorna a url com a predição
    """
    logger.debug("prevendo url")

    # Predição com modelo
    predict = 1

    return jsonify({
            "url": query.url_str,
            "predict": predict,
            }), 200
