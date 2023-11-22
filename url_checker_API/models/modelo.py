import numpy as np
import pickle
import joblib
import sklearn


class Model:
    
    def carrega_modelo(path):
        """
        Carrega modelo do .pkl file
        """
        
        if path.endswith('.pkl'):
            model = pickle.load(open(path, 'rb'))
        elif path.endswith('.joblib'):
            model = joblib.load(path)
        else:
            raise Exception('Formato de arquivo não suportado')
        return model
    
    def preditor(model, form):
        """Realiza a predição de um paciente com base no modelo treinado
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
                    form["nb_www"],
                    form["http_in_path"],
                ])

        # Faremos o reshape para que o modelo entenda que estamos passando
        predict_phishing = model.predict(X_input.reshape(1, -1))
        if predict_phishing[0] == 'phishing':
            result = 1
        elif predict_phishing[0] == 'legitimate':
            result = 0
        return result