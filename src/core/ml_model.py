from src.core import PredictionData


class MLModel:

    def __init__(self, model):
        self.__model = model

    def predict(self, prediction_data: PredictionData) -> int:
        params = prediction_data.get_params()
        results = self.__model.predict(params)
        return results[0]
