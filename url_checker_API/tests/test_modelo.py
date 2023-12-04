from models.avaliador import Avaliador
from models.carregador import Carregador
from models.modelo import Model
from models.pre_processador import PreProcessador

# Instanciação das Classes
pre_processador = PreProcessador()
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()

# Parâmetros
url_dados = "database/dataset_phishing_golden.csv"

# Carga dos dados
dataset = carregador.carregar_dados(url_dados)

# Separando em dados de entrada e saída
X, Y = pre_processador.separacao_x_y_attr(dataset)


# Método para testar modelo KNN a partir do arquivo correspondente
def test_modelo_knn():

    # Importando modelo de KNN e a escala
    knn_path = './ml_model/model_url_checker.joblib'
    modelo_knn = Model.carrega_modelo(knn_path)
    knn_escala_path = './ml_model/scale_url_checker.joblib'
    knn_escala = Model.carrega_escala(knn_escala_path)

    # Obtendo as métricas do KNN
    acuracia_knn, recall_knn, precisao_knn, \
        f1_knn = avaliador.avaliar(
                                modelo_knn,
                                knn_escala,
                                X,
                                Y
                            )

    # Testando as métricas do KNN
    # Modifique as métricas de acordo com seus requisitos
    assert acuracia_knn >= 0.70
    assert recall_knn >= 0.7
    assert precisao_knn >= 0.68
    assert f1_knn >= 0.6
