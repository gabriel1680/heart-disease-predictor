from src.core import MLModel
from pickle import load


class MLModelFactory:

    def create_model() -> MLModel:
        loaded_model = load(open('ml_model/model.pkl', 'rb'))
        return MLModel(loaded_model)
