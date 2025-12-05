matriz = [[1,2,3],[4,5,6],[7,8,9]]

print(matriz)
print(matriz[0]) #Mostra a 1ª lista
print(matriz[1]) #Mostra a 2ª lista
print(matriz[2]) #Mostra a 3ª lista

print(matriz[1][0])
print(' ')

for j in range(3):
    for k in range(3):
        print(matriz[j][k])

print(' ')

for linha in matriz:
    for num in linha:
        print(num)
