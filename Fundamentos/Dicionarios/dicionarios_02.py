#Dicionario, dentro de outro dicionário
dados = {
    'Joao': {
        'Idade': 25, 'Cidade': 'Lisboa'
    }, 
    'Maria': {
        'Idade': 30, 'Cidade': 'Porto'
    },
    'Ana': {
        'Idade': 22, 'Cidade': 'Coimbra' 
    }
}

print(f"Dados do Joao: { dados['Joao'] }")
print(f"Dados do Maria: { dados['Maria'] }")
print(f"Dados do Ana: { dados['Ana'] }") 

# Buscar apenas os dados especificos
print(dados['Joao']['Idade']) 

# Atribuir valor a uma variavel
idade_maria = dados['Maria']['Idade'] 
print("Idade Maria: ", idade_maria)

# Utilizando condicao
if 'Idade' in dados['Ana']: 
    print("A Idade da Ana é: ", dados['Ana']['Idade'])
else: 
    print("A idade da Ana nao esta disponivel.")

# Usando loop   
for nome, informacoes in dados.items(): # percorre cada par de chaves-valor no dicionario de dados
    idade = informacoes.get("Idade") # get para nao gerar erro, caso nao exista.
    if idade is not None:
        print(f"A idade de {nome} é: {idade}") # utilizamos o informacoes para aceder as chaves dentro do dicionario, como se fosse um i (iterador)

# Para percorrer o dicionario e ler os nomes
for nome in dados: # ou dados.keys() por maior segurança
    print(nome)

# Procurando dados no dicionario a partir de uma variavel, poderia ser tambem um input do usuario
nome = "Maria" 
if nome in dados: # se o nome atribuido existir dentro do dicionario
    print(f"Informações de {nome}: ")
    for chave, valor in dados[nome].items(): # chave é o valor inicial ou a "variavel" e valor é o resultado, valor atribuido a chave. enquanto o dados é o incrementador
        print(f"{chave}: {valor}")
else:
    print(f"{nome} não encontrado no dicionario.")

# Procurando e percorrendo os dados, e utilizando somente o nome e a idade
if nome in dados:
    idade = dados[nome].get("Idade", "Idade não encontrada")
    print(f"Idade de {nome}: {idade}")
else:
    print(f"Não encontramos {nome} no dicionario.")

# Convertendo dicionario em uma lista
chaves = list(dados.keys())

if len(chaves) > 2:
    chaves_na_posicao_2 = chaves[2] # aceder a terceira chave [2]
    dados_chave = dados[chaves_na_posicao_2]

    # Mostrar a chave e os dados correspondentes
    print(f"Chave na posição 2: {chaves_na_posicao_2}") # Aqui tem o valor no caso "Ana"
    print("Dados: ", dados_chave) # E aqui contem todos os dados contidos em "Ana"
else: 
    print("Não há chaves suficientes no dicionário.")