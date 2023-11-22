from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, jsonify

from models import Session, Model, UrlModel, Url_checker
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
    """
    Redireciona para /openapi,
    tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

    
# Rota de adição de paciente
@app.post('/url_check', tags=[url_data],
          responses={"200": UrlSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: UrlToCheckSchema):
    """Adiciona um novo url à base de dados
    Retorna uma representação dos url e a previsão de phishig.
    
    ## Args:
        url_str (str): String que
            representa um URL
        length_url (int):
            length of url_str
        length_hostname (int):
            length of url_str host name
        nb_dots (int):
            number of dots in ulr_str
        nb_hyphens (int):
            number od hypens in ulr_str
        nb_underscore (int):
            number of underscore in ulr_str
        nb_tilde (int):
            number of tilde in ulr_str
        nb_percent (int):
            number of percent in ulr_str
        nb_slash (int):
            number of slash in ulr_str
        nb_colon (int):
            number of colon in ulr_str
        nb_comma (int):
            number of comma in ulr_str
        nb_semicolumn (int):
            number of semicolumn in ulr_st
        nb_dollar (int):
            number of dollar in ulr_st
        nb_www (int):
            number of www in ulr_st
        http_in_path (int):
            number of http in the path of url_str
        url_predic (int):
            0 - legitimo
            1 - phishing
        
    Returns:
        dict: url_str and url_predic
    """
    
    print("Instanciando modelo...")
    # Carregando modelo
    ml_path = './ml_model/model_url_checker.joblib'
    modelo = Model.carrega_modelo(ml_path)
    print("Modelo Instanciado!!")
    
    predicao = Model.preditor(modelo, form)
    
    newUrl = UrlModel(
        url_str=form.url_str,
        length_url=form.length_url,
        length_hostname=form.length_hostname,
        nb_dots=form.nb_dots,
        nb_hyphens=form.nb_hyphens,
        nb_underscore=form.nb_underscore,
        nb_tilde=form.nb_tilde,
        nb_percent=form.nb_percent,
        nb_slash=form.nb_slash,
        nb_colon=form.nb_colon,
        nb_comma=form.nb_comma,
        nb_semicolumn=form.nb_semicolumn,
        nb_dollar=form.nb_dollar,
        nb_www=form.nb_www,
        http_in_path=form.http_in_path,
        url_predic=predicao
    )
    logger.debug(f"Adicionando url: '{newUrl.url_str}'")
    
    try:
        # Criando conexão com a base
        session = Session()
        
        # Checando se paciente já existe na base
        if session.query(UrlModel).filter(newUrl.url_str == form.url_str).first():
            error_msg = "Url já existente na base :/"
            logger.warning(f"Erro ao adicionar url '{newUrl.url_str}', {error_msg}")
            return {"message": error_msg}, 409
        
        # Adicionando paciente
        session.add(newUrl)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Adicionado url de nome: '{newUrl.url_str}'")
        return apresenta_url(newUrl), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo URL :/"
        logger.warning(f"Erro ao adicionar URL: '{newUrl.url_str}', {error_msg}")
        return {"message": error_msg}, 400
