
from src.core.ml.result import TrainTestResult


class Model():
    """ Representa o modelo de machine learning que é usado pela aplicação.
    """

    def __init__(self, ml_model):
        """Cria uma instância de Model

        Arguments:
            trained_model: modelo de machine learning.
        """
        self.__ml_model = ml_model

    def predict(self, predictor_vector: list):
        """Realiza a predição a partir de uma lista"""
        return self.__ml_model.predict(predictor_vector)

    def train(self, train_result: TrainTestResult):
        """ Cria e treina um modelo SVM. Poderia ter um Grid Search
        com cross_validation para escolher os melhores hiperparâmetros, etc.
        """
        self.__ml_model.fit(train_result.X, train_result.Y)
