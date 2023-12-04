import numpy as np
import joblib


class Model:

    def carrega_modelo(path):
        """ Carrega modelo do .joblib file
        """

        if path.endswith('.joblib'):
            modelo = joblib.load(path)
        else:
            raise Exception('Formato de arquivo não suportado')
        return modelo

    def carrega_escala(path):
        """ Carrega escala do .joblib file
        """

        if path.endswith('.joblib'):
            escala = joblib.load(path)
        else:
            raise Exception('Formato de arquivo não suportado')
        return escala

    def preditor(model, escala, form):
        """ Realiza a predição de um paciente com base no modelo treinado
        """
        X_input = np.array([
                    form["length_url"],
                    form["length_hostname"],
                    form["nb_dots"],
                    form["nb_hyphens"],
                    form["nb_underscore"],
                    form["nb_tilde"],
                    form["nb_percent"],
                    form["nb_slash"],
                    form["nb_colon"],
                    form["nb_comma"],
                    form["nb_semicolumn"],
                    form["nb_dollar"],
                    form["nb_space"],
                    form["nb_www"],
                    form["nb_com"],
                    form["http_in_path"],
                ])

        # Ajuste de escala
        escalaEntradaX = escala.transform([X_input])

        # Reshape para que o modelo
        predict_phishing = model.predict(escalaEntradaX)
        print(predict_phishing)
        if predict_phishing[0] == 'phishing':
            result = 1
        elif predict_phishing[0] == 'legitimate':
            result = 0
        return result
