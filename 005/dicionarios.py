pessoa = {'nome': 'David Hadrianus', 'idade': 30, 'altura': 1.74}

print(type(pessoa))
print(pessoa)
# forma de acesso
print(pessoa.get('idade'))
print(pessoa.items())
print(pessoa.keys())
print(pessoa.values())
print(pessoa['nome'])

# adicionando um item ao dicionario
pessoa['sexo'] = 'M'
print(pessoa)

# removendo um item do dicionario
del pessoa['sexo']
print(pessoa)