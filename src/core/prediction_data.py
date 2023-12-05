class PredictionData:

    def __init__(self, age, sex, cp, trestbps, chol, fbs) -> None:
        self.__params = [[float(param)
                          for param in [age, sex, cp, trestbps, chol, fbs]]]

    def get_params(self) -> list:
        return self.__params
