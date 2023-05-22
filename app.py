#pip install request 
#pip install pandas
#pip install flask
import requests #item q instala
import json
import pandas as pd
from flask import Flask,request,jsonify


df = pd.DataFrame()
app = Flask(__name__)

#faz uma requisição POST e pega as variáveis displayName, nome, prontuário e telefone criadas no Dialogflow
@app.route('/', methods=['POST'])
def main():
    data = request.get_json(silent=True)
    #print(data)
    intent_name = data['queryResult']['intent']['displayName']
    nome=data['queryResult']['parameters']['nome']
    prontuario=data['queryResult']['parameters']['prontuario']
    telefone = data['queryResult']['parameters']['telefone']
#intentName marcar

#Mensagem de retorno ao usuário
    if intent_name == "marcar":
        data['fulfillmentText'] = f"Ok sr(a) {nome}, sua consulta \
            foi marcada e seu prontuário é o {prontuario} e o telefone é o {telefone}."
        df.to_excel('clientes.xlsx')
    return jsonify(data)

#run Flask app
if __name__ == "__main__":
    app.debug = False
    app.run()