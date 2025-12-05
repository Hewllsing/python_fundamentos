'''
nome = input('Qual é o seu nome? ')
print('Olá ' + nome)
'''
# Desafio 1
'''
Pedir ao utilizador para digitar o nome e depois dizer uma cor.
A sáida deve obter uma resposta do tipo:
    O Marcos gosta da cor verde
'''
# Desafio 2
'''
Pedir ao utilizador para digitar o ano de nascimento.
A sáida deve obter uma resposta do tipo:
    A tua idade é ??
'''

nome2 = input('Qual é o seu nome? ')
cor = input('Qual é a sua cor preferida? ')
print('O ' + nome2 + ' gosta da cor ' + cor + '.')
print(f'O {nome2} gosta da cor {cor}.')

ano = input('Qual o teu ano de nascimento? ')
idade = 2025 - int(ano)
print('A tua idade é ' + str(idade))
print('A tua idade é', idade)
print(f'A tua idade é {idade}')
