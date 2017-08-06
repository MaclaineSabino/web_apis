import requests
import json

def infoPais(pais):
    url = 'https://restcountries.eu/rest/v2/alpha/'+pais

    opcoes = requests.options(url)
    resultado=requests.get(url)

    return (resultado.json(),opcoes.text)
res,opt = infoPais('bra')
print(res)
print(opt)
