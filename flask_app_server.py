"""
author: atreya
desc:
"""
import flask
import predict_sales
app = flask.Flask(__name__)

@app.route("/")
def root():
    return "Welcome to Roseman Sales Prediction API!"


@app.route("/loadModels/")
def load_model():
    reload(predict_sales)
    return True


@app.route('/predictSales/', methods=['POST'])
def get_sales_predictions():
    data = flask.request.get_json(silent=True)
    prediction = predict_sales.predict_sales(json_data=data)
    return flask.jsonify({"predicted_sales":prediction})

if __name__ == "__main__":
    app.run()