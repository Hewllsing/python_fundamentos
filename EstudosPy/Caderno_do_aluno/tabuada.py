numero = int(input("Digite um número para ver a tabuada: "))
quantidadeMultiplicada = int(input("Digite a quantidade de vezes que você quer multiplicar: "))

for i in range(1, quantidadeMultiplicada):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")




