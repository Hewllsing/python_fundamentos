# Importa o módulo completo 'desafio_08', onde estão as funções de conversão
import desafio_08

# Define uma temperatura em graus Celsius
temperatura = 32.0

# Converte de Celsius para Fahrenheit usando a função do módulo
print(f"Celsius para Fahreinheit: {desafio_08.celsius_f(temperatura)}")


# Importa apenas as funções específicas do módulo
from desafio_08 import fahreinheit_c, celsius_f

# Converte Celsius -> Fahrenheit novamente (reutilizando a função importada diretamente)
temperatura = celsius_f(temperatura)

# Converte Fahrenheit -> Celsius e exibe a temperatura arredondada
print(f"Fahreinheit para Celsius: {round(fahreinheit_c(temperatura)):.1f}")
