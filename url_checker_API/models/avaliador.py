from sklearn.metrics import accuracy_score, recall_score, \
                            precision_score, f1_score


class Avaliador:

    def avaliar(self, modelo, X_test, Y_test):

        """ Predição e avaliação do modelo
        """

        pos_label = 'phishing'

        # Reshape para que o modelo
        predicoes = modelo.predict(X_test)

        return (accuracy_score(Y_test, predicoes),
                recall_score(Y_test, predicoes, pos_label=pos_label),
                precision_score(Y_test, predicoes, pos_label=pos_label),
                f1_score(Y_test, predicoes, pos_label=pos_label))
