numeros = [1, 3, 5, 4, 9, 7]

numeros.append(9) # Acrescenta o 9 ao final da lista
print(numeros)
numeros.insert(0, 6) # Acrescenta o 6 na posição 0
print(numeros)
n2 = numeros.copy() # Vai fazer uma copia da lista para n2
print(n2)
n2.append(8)
print(n2)
numeros.sort() # Ordena a lista por ordem crescente
print(numeros)
numeros.reverse() # Ordenar a lista por ordem descendente
print(numeros)
print(numeros.count(4)) # Vai dizer quantas vezes aparece o 4
print(numeros.count(9)) # Vai dizer quantas vezes aparece o 9
print(numeros.index(9)) # Vai mostra em que posição está o primeiro 9 encontrado
# print(numeros.pop()) # Vai retirar o ultimo elemento da lista
encontrar = 8 in numeros
print(encontrar)
encontrar = 4 in numeros
print(encontrar)
