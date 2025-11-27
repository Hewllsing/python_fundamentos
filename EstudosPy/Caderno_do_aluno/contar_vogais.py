frase = str(input("Insira uma frase para contar as vogais: "))
vogais = "aeiou"
contador = 0
for i in frase.lower():
    if i in vogais:
        contador += 1
print(f"A quantidade de vogais é: {contador}")

