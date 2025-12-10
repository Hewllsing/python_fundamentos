# Pedir ao utilizador para introduzir o preço de um produto e a respectiva percentagem de desconto
# O programa deverá calcular e mostrar o valor a pagar após desconto
# Caso a informação não seja válida, o programa deverá indicar qual foi o erro.

# Loop para garantir que o usuário digite um preço válido
while True:
    try:
        # Lê o preço do produto (pode gerar ValueError se não for número)
        preco_produto = float(input("Preço do produto: "))
        
        # Verifica se o valor é maior que zero
        if preco_produto <= 0:
            print("Os valores precisam ser acima de 0.")
        else:
            break  # Sai do loop se o preço for válido
            
    # Trata erro caso o usuário digite algo que não seja número
    except ValueError:
        print("O campo não pode estar vazio, digite apenas números.")
    
    # Trata erro caso haja uma divisão por zero (não ocorre aqui, mas deixado como exemplo)
    except ZeroDivisionError:
        print("O número precisa ser acima de 0.")

# Agora pede o desconto e calcula o valor final
try:
    # Lê a percentagem de desconto
    desconto_produto = float(input("Desconto: "))
    
    # Calcula o valor final após aplicar o desconto
    valor_a_pagar = preco_produto - (preco_produto * (desconto_produto / 100))
    
    # Mostra o valor já com desconto
    print(f"O valor a pagar é: {valor_a_pagar}.")
    
# Trata erro caso o usuário escreva algo que não seja número
except ValueError:
    print("O campo não pode estar vazio, digite apenas números.")

# Trata erro caso haja uma divisão por zero (não ocorre aqui, mas deixado como exemplo)
except ZeroDivisionError:
    print("O número precisa ser acima de 0.")
