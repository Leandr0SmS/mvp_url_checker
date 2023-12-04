from models.carregador import Carregador
from models.pre_processador import PreProcessador
from models.url_checker_model import Url_checker

# Instanciação da Classe
pre_processador = PreProcessador()
carregador = Carregador()

# Parâmetros
url_dados = "database/dataset_phishing_golden.csv"

# Carga dos dados
dataFrame = carregador.carregar_dados(url_dados)

list_dict = pre_processador.csv_dict(dataFrame)


def test_checker_url_model():
    for url_data in list_dict:
        url_data.pop("status")
        url_test = Url_checker(url_data["url"]).url_to_check()
        url_data.pop("url")
        assert url_test == url_data
