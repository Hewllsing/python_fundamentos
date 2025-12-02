#Pedir ao utilizador para introduzir uma password, Verificar se tem no minimo 6 caracteres e no maximo 15 caracteres, caso a password seja invalida, o programa deverá dar essa indicação

password = input('Qual é a sua password? ')
if len(password) < 6 or len(password) > 15:
    print('A password não é válida')
else:
    print('A password foi aceita.')