import requests
import json

# Faz a requisição via link da API
cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
# Atribui os valores em formato json para dicionario
cotacoes = cotacoes.json()
print(cotacoes)

# Para buscar o valor da cotacao de dolar para real
cotacao_dolar = cotacoes["USDBRL"]["bid"]
print(cotacao_dolar)
