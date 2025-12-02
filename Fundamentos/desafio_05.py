#Pedir ao utilizador para introduzir uma sequencia de numeros, exemplo: 1234. converter essa sequencia para texto, por exemplo "Um", "Dois", "Tres", "Quatro".quit

dicionario_numeros = {"0":"Zero", "1":"Um", "2":"Dois", "3":"Tres", "4":"Quatro", "5":"Cinco", "6":"Seis", "7":"Sete", "8":"Oito", "9":"Nove"}

num_utilizador = input("Por favor, introduza 5 numeros: ") # Input
num_escrito = "" # Output 

for dicionario in num_utilizador:
    num_escrito = num_escrito + dicionario_numeros.get(dicionario, ", ") + " "
print(f"Sequencia em escrita: {num_escrito}")