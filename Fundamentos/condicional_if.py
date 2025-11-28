'''
if condicao:
    instrução1
    instrução2
instrução
'''

# idade = input('Qual é a sua idade? ')

'''
if int(idade) < 18:
    print('Ainda não tens idade para tirar a carta.')
    print('Espera mais algum tempo.')
elif condição:
    instrução
elif condição:
    instrução
else:
    print('Podes tirar a carta.')
'''

# Desafio 3
'''
Pedir a um aluno para introdzir a nota do teste
Se a nota for inferior a 50, responder "Insuficiente"
Se a nota for maior que 50, responder "Suficiente"    
Se a nota for maior que 70, responder "Bom"
Se a nota for maior que 90, responder "Muito Bom"

'''
'''
nota_teste = int(input('Qual é a tua nota? '))

if nota_teste < 50:
    print('Insuficiente')
elif nota_teste < 70:
    print('Suficiente')
elif nota_teste < 90:
    print('Bom')
else:
    print('Muito Bom.')
'''

# Operadores lógicos (and, or, not)
domingo_faz_sol = False
tenho_boleia = False

#and
if domingo_faz_sol and tenho_boleia:
    print('Vou à praia')
else:
    print('Fico em casa')

#or
if domingo_faz_sol or tenho_boleia:
    print('Vou à praia')
else:
    print('Fico em casa')

if domingo_faz_sol or not tenho_boleia:
    print('Vou à praia')
else:
    print('Fico em casa')

# Operadores de comparação
'''
<
>
<=
>=
==
!=

'''

# Desafio 4
'''
Pedir ao utilizador para introduzir uma password
Verificar se tem no minimo 6 caracteres e no maximo 15 caracteres
Caso a password seja invalida, o programa deverá dar essa indicação
'''

pswd = input('Qual é a sua password? ')
if len(pswd) < 6 or len(pswd) > 15:
    print('A password não é válida')
else:
    print('A password foi aceite.')