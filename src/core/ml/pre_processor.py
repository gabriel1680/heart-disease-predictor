from src.core.ml.test_result import TestResult, TrainTestResult
from sklearn.model_selection import train_test_split


class PreProcessor:

    seed = 7

    def __init__(self, dataset, test_percentage):
        self.dataset = dataset.query(
            "chol != '?' & fbs != '?' & trestbps != '?'")
        self.test_percentage = test_percentage

    def process(self):
        """ Cuida de todo o pré-processamento. """
        test_data = self.__prepare_holdout(
            self.dataset, self.test_percentage, self.seed)
        X_train, X_test, Y_train, Y_test = test_data
        return (TrainTestResult(X_train, Y_train), TestResult(X_test, Y_test))

    def __prepare_holdout(self, dataset, percentual_teste, seed):
        """ Divide os dados em treino e teste usando o método holdout.
        Assume que a variável target está na última coluna.
        O parâmetro test_size é o percentual de dados de teste.
        """
        data = dataset.values
        X = data[:, 0:6]
        Y = data[:, 6].astype(int)
        return train_test_split(X, Y, test_size=percentual_teste, random_state=self.seed)
