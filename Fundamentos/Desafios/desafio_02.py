# Dada uma lista de numeros, pesquise e mostre qual deles é o maior

numeros_list = [5, 3, 7, 19, 1, 3, 4, 12, 6, 7]
numero_maior = 0

for numero in numeros_list:
    if numero > numero_maior:
        numero_maior = numero
print(f"O maior numero da lista é o: {numero_maior}")