from src.core.ml.result import TestResult, TrainTestResult
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from pandas import DataFrame


class PreProcessor:
    """Responsável pelo pré processamento dos dados"""

    seed = 7

    def __init__(self, dataset: DataFrame, test_percentage: float):
        self.dataset = dataset
        self.test_percentage = test_percentage

    def process(self):
        """Orquestra o pré-processamento dos dados."""

        # limpeza dos dados
        filtered_dataset = self.dataset.query(
            "chol != '?' & fbs != '?' & trestbps != '?'")

        # holdout
        test_data = self.__prepare_holdout(
            filtered_dataset, self.test_percentage, self.seed)

        # normalização dos dados
        rescaled_data = self.__rescale(test_data)

        X_train, X_test, Y_train, Y_test = rescaled_data
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

    def __rescale(self, test_data):
        """Faz a padronização dos dados"""
        X_train, X_test, Y_train, Y_test = test_data
        scaler = MinMaxScaler()

        # dados de treinamento
        scaler.fit(X_train)
        X_train_rescaled = scaler.transform(X_train)

        # dados de teste
        scaler.fit(X_test)
        X_test_rescaled = scaler.transform(X_test)
        return (X_train_rescaled, X_test_rescaled, Y_train, Y_test)
