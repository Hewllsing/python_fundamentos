import random

n = 1
while n <= 5: 
    print(n)
    n += 1
    if n == 4:
        break # quando o if for verdadeiro, vai parar o programa e vai para o ultimo print
else:
    print('Fim de ciclo')
print('Fim do programa')

valor = random.randint(1, 10)
print(valor)