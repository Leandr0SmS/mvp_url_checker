from sklearn.model_selection import train_test_split

class PreProcessador:

    def separacao_x_y_attr(self, dataset):
        """
            Separa entradas (X), saídas (Y) e atributos do dataset 
        """
        shape = dataset.shape
        dateSet_len = shape[1] - 1 # Numbero de colunas do dataset
        
        # Separando em dados de entrada e saída
        X = dataset.iloc[:, 1:dateSet_len]
        Y = dataset.iloc[:, dateSet_len]
        
        return (X, Y)

        
