
from src.core.ml.result import TrainTestResult


class Model():

    def __init__(self, trained_model):
        self.__ml_model = trained_model

    def predict(self, predictor_vector: list):
        return self.__ml_model.predict(predictor_vector)

    def train(self, train_result: TrainTestResult):
        """ Cria e treina um modelo SVM. Poderia ter um Grid Search
        com cross_validation para escolher os melhores hiperparâmetros, etc.
        """
        self.__ml_model.fit(train_result.X, train_result.Y)
