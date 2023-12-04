from sklearn.metrics import accuracy_score, recall_score, \
                            precision_score, f1_score


class Avaliador:

    def avaliar(self, modelo, escala, X_test, Y_test):

        """ Predição e avaliação do modelo
        """

        pos_label = 'phishing'

        # Ajuste de escala
        escalaEntradaX = escala.transform(X_test)

        # Reshape para que o modelo
        predicoes = modelo.predict(escalaEntradaX)

        return (accuracy_score(Y_test, predicoes),
                recall_score(Y_test, predicoes, pos_label=pos_label),
                precision_score(Y_test, predicoes, pos_label=pos_label),
                f1_score(Y_test, predicoes, pos_label=pos_label))
