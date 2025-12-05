# Utilizamos chavetas
# chave : valor
# evitar chaves repetidas
aluno = {'nome':'joana','idade':17, 'inscrito': True} 

print(aluno['nome'])
# print(aluno['ano'])

print(aluno.get('nome'))
print(aluno.get('ano'))
print(aluno.get('ano', 9))

aluno['ano'] = 2025
print(aluno.get('ano'))