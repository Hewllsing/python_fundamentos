import pandas as pd

# 1ª Forma — Criar um DataFrame vazio
# dataframe = pd.DataFrame()

# 2ª Forma — Criar um DataFrame a partir de um dicionário
venda = {
    "data": ["15/02/2021", "16/02/2021"],
    "valor": [500, 300],
    "produto": ["feijao", "arroz"],
    "qtd": [50, 70]
}

# Exibe o dicionário original
print(venda)

# Converte o dicionário em um DataFrame
vendas_dataframe = pd.DataFrame(venda)
print(vendas_dataframe)

# 3ª Forma — Criar um DataFrame a partir de um arquivo Excel
# O arquivo "vendas_tabela.xlsx" deve estar na mesma pasta do main.py
# Caso esteja em outra, usar o caminho completo
vendas_df = pd.read_excel("vendas_tabela.xlsx")
print(vendas_df)

# HEAD → mostra as primeiras linhas do DataFrame
print(f"Head: {vendas_df.head(20)}")  # Mostra os primeiros 20 registros

# SHAPE → retorna o número de linhas e colunas (linhas, colunas)
print(f"Shape: {vendas_df.shape}")

# DESCRIBE → retorna estatísticas descritivas das colunas numéricas
print(f"Describe: {vendas_df.describe()}")

# Seleciona apenas as colunas "Produto" e "ID Loja"
# Cria um novo DataFrame com essas duas colunas
produto = vendas_df[["Produto", "ID Loja"]]
print(produto)  # Pode usar .head() para limitar a visualização

# LOC → acessar uma linha específica pelo índice
print(vendas_df.loc[1])  # Mostra somente a linha de índice 1

# LOC com slicing → mostra um intervalo de linhas
print(vendas_df.loc[1:10])  # Mostra da linha 1 até a linha 10
