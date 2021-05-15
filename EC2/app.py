from keras.models import load_model
from keras.models import Sequential
from keras.layers import (LSTM, GRU, Dense, Flatten, RepeatVector, TimeDistributed, )
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from tensorflow.python.keras.callbacks import ModelCheckpoint
from flask import Flask, request
from flask import jsonify

from metrics import recall_m, precision_m, f1_score

app = Flask(__name__)

model_classification = load_model('classification-cnn-lstm-model.h5', custom_objects={
    'recall_m': recall_m,
    'precision_m': precision_m,
    'f1_score': f1_score
})

model_forecast = load_model('forecasting-cnn-lstm-model.h5')

@app.route("/")
def hello_world():
    return "<p> Hello, World 2!</p>"

@app.route('/classification')
def classify_fault():
    temperatures = [int(v) for v in request.args['temperatures'].split(',')]
    return jsonify(model_classification.predict([[temperatures]])[0].tolist())

@app.route('/forecasting')
def forecast_temperature():
    temperatures = [[int(v)] for v in request.args['temperatures'].split(',')]
    return jsonify(model_forecast.predict([temperatures])[0].tolist())


@app.route('/forecasting-classification')
def forecast_classify_temperature():
    return forecast_temperature().get_data() + classify_fault().get_data()