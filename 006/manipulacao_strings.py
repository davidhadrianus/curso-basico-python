
nome = "David"
sobrenome = "Hadrianus"
mensagem = "Bem-vindo"
frase = 'frase de efeito'

# acessar carateres
print(nome[2])
# Fatiamento de String (Slicing)
print(sobrenome[0:3])
print(sobrenome[:4])
print(sobrenome[4:])
print(sobrenome[::-1])
# Concatenação de Strings
fullname = nome + " " + sobrenome
print(fullname)
# Repetiçao de String
print('ha' * 4)
# Tamanho de uma String
print(len(fullname))
# Transformação de Case
print(fullname.upper())
print(fullname.lower())
print('texto capitalize'.capitalize())
print(frase.title())
# Replase - Substituição de partes
print(mensagem.replace('vindo', 'indo'))
# Divisão de String
print(frase.split(' '))
# f-string
print(f'ola, {nome} {sobrenome}')
