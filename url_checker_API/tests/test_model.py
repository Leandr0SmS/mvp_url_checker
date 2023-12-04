import pytest
import pandas as pd
from models.modelo import Model

def test_model():
    
    modelo_path = '../ml_model/model_url_checker.joblib'
    escala_path = '../ml_model/scale_url_checker.joblib'
    
    # URL de importação do dataset
    url = "https://raw.githubusercontent.com/Leandr0SmS/mvp_url_checker/main/dataset_phishing_golden.csv"

    # Lê o arquivo
    dataset = pd.read_csv(url, delimiter=',')
    
    modelo = Model.carrega_modelo(modelo_path)
    
    escala = Model.carrega_escala(escala_path)

    # Separação em conjuntos de treino e teste
    array = dataset.values

    dateSet_len_test = shape[1] - 1 # Numbero de colunas do dataset

    X_test_2 = array[:,1:dateSet_len_test]
    y_test_2 = array[:,dateSet_len_test]

    # Padronização nos dados de entrada usando o scaler utilizado em X
    rescaledEntrada_X = scaler.transform(X_test_2)
    saidas_teste_2 = model.predict(rescaledEntrada_X)

    target_names = ["legitimate", "phishing"]
    print(classification_report(y_test_2, saidas_teste_2, target_names=target_names))

    result_test_2 = cross_val_score(model, X_test_2, y_test_2, cv=kfold, scoring=scoring)
    print(f"acc: {result_test_2.mean()}")
    assert result_test_2.mean() >= 0.7