from unittest import TestResult
from src.core.ml.model import Model
from sklearn.metrics import accuracy_score

class AccuracyEvaluator:
    """Avaliador de acurácia do modelo"""

    def __init__(self, model: Model):
        self.__trained_model = model

    def evaluate(self, test_result: TestResult):
        """ Faz uma predição e avalia o modelo. Poderia parametrizar o tipo de
        avaliação, entre outros.
        """
        predictions = self.__trained_model.predict(test_result.X)
        return accuracy_score(test_result.Y, predictions)
