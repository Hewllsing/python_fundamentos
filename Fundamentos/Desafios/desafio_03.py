# Deverá criar um programa que remova os duplicados da lista

numeros_list = [1, 3, 9, 1, 5, 4, 3, 9, 7, 1]
numeros_list_sem_duplicados = []

# METODO 1
for numero in numeros_list:
        if numero not in numeros_list_sem_duplicados:
            numeros_list_sem_duplicados.append(numero)
print(f"Lista sem duplicados 1: {numeros_list_sem_duplicados}")

# METODO 2
for numero in numeros_list:
        if numeros_list.count(numero) > 1:
            numeros_list.remove(numero)
print(f"Lista sem duplicados 2: {numeros_list}")
