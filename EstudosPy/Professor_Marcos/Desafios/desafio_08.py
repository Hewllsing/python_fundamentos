# Função que converte de graus Celsius para Fahrenheit
# Desafio em conjunto com o 8.1

def celsius_f(temperatura):
    # Fórmula: F = C * 1.8 + 32
    return temperatura * 1.8 + 32

# Função que converte de Fahrenheit para Celsius
def fahreinheit_c(temperatura):
    # Fórmula: C = (F - 32) / 1.8
    return (temperatura - 32) / 1.8
