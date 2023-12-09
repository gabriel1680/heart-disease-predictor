from src.core.ml.data_loader import DataLoader
from src.core.ml.evaluator import AccuracyEvaluator
from src.core.ml.factory import ModelFactory
from src.core.ml.pre_processor import PreProcessor


def test_model_accuracy():
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
    # avaliação de acurácia
    evaluator = AccuracyEvaluator(model)
    assert evaluator.evaluate(test_result) >= 0.80
