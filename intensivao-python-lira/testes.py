# import requests
# import json

# cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
# cotacoes = cotacoes.json()
# cotacao_dolar = cotacoes['USDBRL']['bid']
# print(cotacao_dolar)

carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
x = carnes
del (x[-1])

print(carnes)
print(x)