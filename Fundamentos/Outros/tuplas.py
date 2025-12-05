# As tuplas são imutáveis
# Uso as tuplas quando tenho certeza que o seu valor não vai ser alterado

num1 = [1, 2, 3] # Lista
num2 = (1, 2, 3) # Tupla

num1[0] = 5
num2[0] = 5

print(num1)
print(num2)

