from pydantic import BaseModel


class PredictionRequest(BaseModel):
    """ Define como os parâmetros para geração de uma predição devem ser enviados
    """
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int


class PredictionResponse(BaseModel):
    """ Define a resposta da predição
    """
    prediction: str
