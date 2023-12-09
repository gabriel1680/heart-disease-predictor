from src.core.ml.model import Model
from pickle import load


class ModelFactory:
    """Fábrica do modelo de machine learning utilizado."""

    def create_model() -> Model:
        """Cria a instancia do modelo a partir do arquivo gerado de um modelo treinado.
        """
        loaded_model = load(open('ml_model/model.pkl', 'rb'))
        return Model(loaded_model)
