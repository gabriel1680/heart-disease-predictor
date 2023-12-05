from flask import Flask, request, send_from_directory, render_template
from src.core import MLModelFactory, PredictionData


def create_app():

    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template("index.html"), 200

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory('static', 'favicon.ico', mimetype='image/x-icon')

    @app.route('/', methods=['POST'])
    def add_produto():
        form = request.form
        model = MLModelFactory.create_model()
        prediction_data = PredictionData(
            form.get("age"),
            form.get("sex"),
            form.get("cp"),
            form.get("trestbps"),
            form.get("chol"),
            form.get("fbs")
        )
        result = model.predict(prediction_data)
        msg = "Você têm problemas cardíacos" if result == 1 else "Você não têm problemas cardíacos"
        return render_template("result.html", result=msg), 200

    return app
