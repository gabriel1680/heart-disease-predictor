from abc import ABC, abstractmethod
from unittest import TestResult
from src.core.ml.model import Model
from sklearn.metrics import accuracy_score, recall_score, precision_score


class Evaluator(ABC):
    """
    Classe abstrata que implementa o padrão de projeto Template Method
    seguindo o Open-Close Principle para que caso haja uma nova métrica a ser considerada,
    será necessário somente implementar a nova classe herdando de Evaluator.
    """

    def __init__(self, model: Model):
        self.__trained_model = model

    def evaluate(self, test_result: TestResult):
        """ Faz uma predição e avalia o modelo. Poderia parametrizar o tipo de
        avaliação, entre outros.
        """
        predictions = self.__trained_model.predict(test_result.X)
        return self.evaluate_by_threshold(test_result.Y, predictions)

    @abstractmethod
    def evaluate_by_threshold(self, test_result_Y: list, model_predictions: list) -> float:
        ...


class AccuracyEvaluator(Evaluator):
    """Avaliador de acurácia do modelo"""

    def evaluate_by_threshold(self, test_result_Y: list, model_predictions: list) -> float:
        return accuracy_score(test_result_Y, model_predictions)


class RecallEvaluator(Evaluator):
    """Avaliador de recall do modelo"""

    def evaluate_by_threshold(self, test_result_Y: list, model_predictions: list) -> float:
        return recall_score(test_result_Y, model_predictions)


class PrecisionEvaluator(Evaluator):
    """Avaliador de precisão do modelo"""

    def evaluate_by_threshold(self, test_result_Y: list, model_predictions: list) -> float:
        return precision_score(test_result_Y, model_predictions)
