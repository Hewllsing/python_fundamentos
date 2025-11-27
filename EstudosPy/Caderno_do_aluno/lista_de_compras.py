frutas = [""] * 5
for i in range(len(frutas)):
    frutas[i] = input("Digite o nome de uma fruta para adicionar à lista de compras: ")

print("Sua lista de compras contém:")
for fruta in frutas:
    print(f"- {fruta}")
    

print(frutas)



