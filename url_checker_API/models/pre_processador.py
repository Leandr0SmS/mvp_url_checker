class PreProcessador:

    def separacao_x_y_attr(self, dataset):
        """ Separa entradas (X), saídas (Y) e atributos do dataset
        """
        shape = dataset.shape
        # Numbero de colunas do dataset
        dateSet_len = shape[1] - 1

        # Separando em dados de entrada e saída
        X = dataset.iloc[:, 1:dateSet_len]
        Y = dataset.iloc[:, dateSet_len]

        return (X, Y)

    def csv_dict(self, dataset):
        """ Carrega CSV e tranforms em uma lista de Dicts
        """
        return dataset.to_dict('records')
