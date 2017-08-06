import json
import requests

def enviarArquivo():
    dados = {'file':open('1.jpg','rb')}
    url = 'https://file.io'


    resultado = requests.post(url,files=dados)

    return resultado.text


print(enviarArquivo())
