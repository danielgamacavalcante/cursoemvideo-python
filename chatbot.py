import requests #item q instala
import json

from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    data = request.get_json(silent=True)
    #print(data)
    intentName = data['queryResult']['intent']['displayName']
    nome=data['queryResult']['parameters']['nome']
    prontuario=data['queryResult']['parameters']['prontuario']
    telefone = data['queryResult']['parameters']['telefone']