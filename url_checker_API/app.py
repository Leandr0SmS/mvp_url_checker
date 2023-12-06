from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect

from models import Session, Model, UrlModel, Url_checker
from schemas import UrlStringToCheckSchema, UrlSchema, \
    ErrorSchema, apresenta_url
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
def predict(form: UrlStringToCheckSchema):
    """Adiciona um novo url à base de dados
    Retorna uma representação dos url e a previsão de phishig.

    ## Args:
        url_str (str): String que
            representa um URL

    Returns:
        UrlModel
    """

    # Carregando modelo de ML
    modelo_path = './ml_model/pipe_knn__url_checker.joblib'
    modelo = Model.carrega_modelo(modelo_path)

    # Cria uma instancia do Url_checker para ser checado
    url_to_model = Url_checker(form.url_str).url_to_check()

    # Faz a predição
    predicao = Model.preditor(modelo, url_to_model)

    # Cria um modelo do url para o database
    newUrl = UrlModel(
        url_str=form.url_str,
        length_url=url_to_model["length_url"],
        length_hostname=url_to_model["length_hostname"],
        nb_dots=url_to_model["nb_dots"],
        nb_hyphens=url_to_model["nb_hyphens"],
        nb_underscore=url_to_model["nb_underscore"],
        nb_tilde=url_to_model["nb_tilde"],
        nb_percent=url_to_model["nb_percent"],
        nb_slash=url_to_model["nb_slash"],
        nb_colon=url_to_model["nb_colon"],
        nb_comma=url_to_model["nb_comma"],
        nb_semicolumn=url_to_model["nb_semicolumn"],
        nb_dollar=url_to_model["nb_dollar"],
        nb_space=url_to_model["nb_space"],
        nb_www=url_to_model["nb_www"],
        nb_com=url_to_model["nb_com"],
        http_in_path=url_to_model["http_in_path"],
        url_predic=predicao
    )

    try:
        logger.debug(f"Adicionando url: '{newUrl.url_str}'")
        # Criando conexão com a base
        session = Session()

        # Checando se url já existe na base
        if session.query(UrlModel)\
            .filter(UrlModel.url_str == newUrl.url_str)\
                .first():
            logger.debug(f"Url ja exista na base:'{newUrl.url_str}'")
            return apresenta_url(newUrl), 200

        # Adicionando url
        session.add(newUrl)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Adicionado url: '{newUrl.url_str}'")
        return apresenta_url(newUrl), 200

    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo URL :/"
        logger.warning(
            f"Erro ao adicionar URL: '{newUrl.url_str}', {error_msg}"
            )
        return {"message": error_msg, "error": e}, 400
