from flask import Flask, request, send_from_directory, render_template
from src.core.ml.factory import ModelFactory
from src.core.prediction_data import PredictionData


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html"), 200


@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/x-icon')


@app.route('/', methods=['POST'])
def get_prediction_result():
    form = request.form
    prediction_data = PredictionData(
        form.get("age"),
        form.get("sex"),
        form.get("cp"),
        form.get("trestbps"),
        form.get("chol"),
        form.get("fbs")
    )
    model = ModelFactory.create_model()
    result = model.predict(prediction_data.get_params())
    msg = "Você têm problemas cardíacos" if result == 1 else "Você não têm problemas cardíacos"
    return render_template("result.html", result=msg), 200
