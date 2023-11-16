import numpy as np
import pickle


class Model:
    
    def carrega_modelo(path):
        """Dependendo se o final for .pkl ou .joblib, carregamos de uma forma ou de outra
        """
        
        if path.endswith('.pkl'):
            model = pickle.load(open(path, 'rb'))
        else:
            raise Exception('Formato de arquivo não suportado')
        return model
    
    def preditor(model, form):
        """Realiza a predição de um paciente com base no modelo treinado
        """
        X_input = np.array([
                    form.length_url,
                    form.length_hostname,
                    form.nb_dots,
                    form.nb_hyphens,
                    form.nb_underscore,
                    form.nb_tilde,
                    form.nb_percent,
                    form.nb_slash,
                    form.nb_colon,
                    form.nb_comma,
                    form.nb_semicolumn,
                    form.nb_dollar,
                    form.nb_www,
                    form.http_in_path,
                ])

        # Faremos o reshape para que o modelo entenda que estamos passando
        diagnosis = model.predict(X_input.reshape(1, -1))
        return int(diagnosis[0])