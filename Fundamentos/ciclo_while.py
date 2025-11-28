import random

'''
while condição:
    instrução1
    instrução2
    instrução3
    break
else:
    instrução5
instrução4
'''
#ciclo infinito
'''
n = 1
while n <= 5:
    print(n)
print('Fim do programa')
'''
n = 1
while n <= 5: # 
    print(n)
    n += 1
    if n == 4:
        break # quando o if for verdadeiro, vai parar o programa e vai para o ultimo print
else:
    print('Fim de ciclo')
print('Fim do programa')

valor = random.randint(1, 10)
print(valor)

# Desafio 5
'''
Colocar o computador a gerar um numero aleatório entre 1 e 6.
Pedir ao utilizador para tentar adivinhar o número.
Dar ao utilizador 3 tentativas para conseguir.
Dar os prabéns caso acerte, caso contrário, desejar boa sorte para a proxima.
'''
 
