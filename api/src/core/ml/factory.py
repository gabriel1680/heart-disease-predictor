from src.core.ml.model import Model
from pickle import load


class ModelFactory:

    def create_model() -> Model:
        loaded_model = load(open('../ml_model/model.pkl', 'rb'))
        return Model(loaded_model)
