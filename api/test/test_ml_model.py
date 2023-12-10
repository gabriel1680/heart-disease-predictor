from src.core.ml.data_loader import DataLoader
from src.core.ml.evaluator import AccuracyEvaluator, PrecisionEvaluator, RecallEvaluator
from src.core.ml.factory import ModelFactory
from src.core.ml.pre_processor import PreProcessor

# carregamento dos dados
loader = DataLoader("data/dataset_test.csv")
dataset = loader.load(
    ["age", "sex", "cp", "trestbps", "chol", "fbs", "num"])

# pré-processamento dos dados
pre_processor = PreProcessor(dataset, 0.2)
train_result, test_result = pre_processor.process()

# treinamento do modelo
model = ModelFactory.create_model()
model.train(train_result)


def test_model_accuracy():
    evaluator = AccuracyEvaluator(model)
    assert evaluator.evaluate(test_result) >= 0.80


def test_model_precision():
    evaluator = PrecisionEvaluator(model)
    assert evaluator.evaluate(test_result) >= 0.75


def test_model_recall():
    evaluator = RecallEvaluator(model)
    assert evaluator.evaluate(test_result) >= 0.80
