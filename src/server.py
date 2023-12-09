from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS

from src.core.ml.factory import ModelFactory
from src.core.prediction_data import PredictionData

from src.schema import PredictionRequest, PredictionResponse


info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)

prediction_tag = Tag(name="Predição",
                     description="Realiza a predição de doenças cardíacas")
home_tag = Tag(name="Documentação",
               description="Seleção de documentação: Swagger, Redoc ou RapiDoc")

CORS(app)


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post("/", tags=[prediction_tag], responses={"200", PredictionResponse})
def get_prediction_result(form: PredictionRequest):
    prediction_data = PredictionData(
        form.age,
        form.sex,
        form.cp,
        form.trestbps,
        form.chol,
        form.fbs
    )
    model = ModelFactory.create_model()
    result = model.predict(prediction_data.get_params())
    msg = "Você têm problemas cardíacos" if result == 1 else "Você não têm problemas cardíacos"
    return {"prediction": msg}, 200
