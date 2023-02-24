import json
import os
import time
import boto3
import pickle
import sklearn
# la tabla de
tabla = "pythonTabla"
# recurso DynamoDB con la tabla
dynamo = boto3.resource('dynamodb').Table(tabla)
# Aquí deberían rellenar el código que cargue el modelo desde el S3 donde se encontrase:
s3 = boto3.resource('s3')
cubo = "micubo-pythoncito"
nombre_modelo = "advertising.model"
modelo = pickle.loads(s3.Bucket(cubo).Object(nombre_modelo).get()['Body'].read())
#print(modelo)
# funciones a definir
def predict(x):
    None
def review_predict():
    None
def saludo():
    return json.dumps("Hola, soy un pobre predictor que no sabe HTML (desde el repo)")
def lambda_handler(event, context=None):
    # Log event...
    print(event)
    # proceso de desvio de endpoints
    if event['routeKey']=='GET /':
        print("emitiendo el saludo")
        return saludo()
    elif event['routeKey']=='POST /predict':
        print("creando prediccion")
        return predict(event["queryStringParameters"])
    elif event['routeKey']=='GET /review_predicts':
        print("verificando predicciones")
        return review_predict()