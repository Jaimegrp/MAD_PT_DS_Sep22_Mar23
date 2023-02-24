from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3
import sklearn
import pickle
import numpy as np

app = Flask(__name__)
app.config['DEBUG'] = True

root = "." # Ruta a la carpeta donde esté el modelo guardado
model = pickle.load(open(root + 'advertising.model', 'rb'))

# POST {"TV":, "radio":, "newspaper":} -> It returns the sales prediction for input investments
@app.route('/predict', methods=['POST'])
def get_predict():

    # Get current time for the PREDICTIONS table
    str_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # Establish SQLITE3 connection and create a cursor to operate upon the DB
    

    # Get POST JSON data
    data = request.get_json()
    tv = data["TV"]
    radio = data["radio"]
    newspaper = data["newspaper"]

    # Model prediciton
    

    # Save prediction in PREDICTIONS table
    
    
    # Return the prediction
    



app.run(port=4000)