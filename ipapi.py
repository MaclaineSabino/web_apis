import json
import requests

def infoIp(ip):

    url='https://ipapi.co/'+ip+'/json/'

    resultado = requests.get(url)
    options = requests.options(url)

    return (resultado.json(),options.text)


res,opt = infoIp('187.41.217.250')
print(res)
print(opt)

#ipapi é uma api pública onde com requisições get e informando um IP você obtém
