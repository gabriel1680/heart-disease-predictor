class TestResult:
    """Representa o conjunto de dados para o teste do modelo
    """

    def __init__(self, X, Y):
        self.X = X
        self.Y = Y


class TrainTestResult(TestResult):
    """Representa o conjunto de dados para o teste de treino do modelo
    """
    pass
