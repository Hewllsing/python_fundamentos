import requests

# link do open_weather: https://openweathermap.org/
# tem que se fazer primeiro um registo para obter uma API_KEY
# vai receber um e-mail com a API_KEY

API_KEY = "3689129ee7af0fa500cad990971aecd6"
cidade = "Braga"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

requisicao = requests.get(link)
print(requisicao)

# (200) - Valido(funcionou)
# (400) - Não encontrado
# (500) - Servidor não disponivel
# (401) - Problema na solicitação feita pelo navegador

# tudo contido na API
requisicao_dic = requisicao.json()
print(requisicao_dic)

# nome da cidade
print(f"Cidade: {cidade}")
descricao = requisicao_dic['weather'][0]['description']

# descricao do clima ex: "algumas nuvens"
print(f"Descrição: {descricao}")

# temperatura ex: 14.8 ªC
temperatura = requisicao_dic['main']['temp'] - 273.15
temperatura = round(temperatura, 1) # arredondando a temperatura para 1 casa decimal após o ponto ex: 14.8
print(f"Temperatura: {temperatura}ºC")