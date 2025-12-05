import math

#peradores aritmeticos
a=5
b=3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b) # Divisão inteira 
print(a % b)  # Resto da divisão
print(a ** b) # Potência

# Operadores por atribuíção
a = a + 2 
a += 2
b *= 2

print(a)
print(b)

# Operadores precedências

#Parentesis
#Potências
#Multiplicação e divisão
#Soma e subtrações

c = 10 + (3 * 2) ** 2 
print(c)

#arredondamento

d = 7.3
e = 7.6
f = -7.6 
print(round(d)) #arredonda para baixo
print(round(e)) #arredonda para cima
print(abs(f)) # Valor absoluto - é o módulo do número 

print(math.ceil(d)) #arredonda para cima
print(math.ceil(e)) #arredonda para cima
print(math.floor(d)) #arredonda para baixo
print(math.floor(e)) #arredonda para baixo

print(math.pi)