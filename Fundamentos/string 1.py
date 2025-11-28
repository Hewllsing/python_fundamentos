nome = "Joana"
Nome = 'Joana'
nome = "In today´s"
print(nome)
nome = 'Eu hoje vou ao "supermercado"'
print(nome)
email = '''
Ola Joao
Gostaria de marcar uma consulta
Cumprimentos
Marcos Alvaraes
'''
print(email)

frase = 'Hoje está chuva'
print(frase[0])
print(frase[0:6])
print(frase[:6])
print(frase[7:])
print(frase[-2])

nome = "Filipa"
apelido = 'Silva'
idade = 17
# A Filipa Silva tem 17 anos

frase = 'A ' + nome + ' ' + apelido + ' tem ' + str(idade) + ' anos.'
print(frase)

frase= f'A {nome} {apelido} tem {idade} anos.'
print(frase)

nome = 'Joana Santos'
print(len(nome))
print(nome.upper()) # retorna todas as letras em maiusculas
print(nome.lower()) # retorna todas as letras em minusculas
print(nome.find('a')) # vai mostrar a posição da primeira letra "a" encontrada
print(nome.find('tos')) # vai mostrar a posição das letras
print(nome.find('ks')) # se não encontrar, retorna -1
print(nome.capitalize()) #Poen a 1ª letra  da primeiro nome maiuscula

contem1 = 'Joana' in nome
print(contem1)
contem2 = 'joana' in nome
print(contem2)

 
