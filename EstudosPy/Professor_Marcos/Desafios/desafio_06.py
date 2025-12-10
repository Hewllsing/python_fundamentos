# Função que recebe dois números e retorna o maior entre eles
def maior(num1, num2):
    # Verifica se o primeiro número é maior que o segundo
    if num1 > num2:
        return num1  # Retorna o primeiro número
    else:
        return num2  # Caso contrário, retorna o segundo número

# Exemplo de uso da função
print(maior(30, 40))
