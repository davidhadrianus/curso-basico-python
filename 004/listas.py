
lista = [10, 'David Hadrianus', 1.74, True]
# as posições de uma lista começam em 0
print(type(lista))
print(len(lista))
print(type(lista[0]))
print(type(lista[1]))
print(type(lista[2]))
print(type(lista[3]))

print(lista)
# podemos aumentar itens a uma lista utilizando a funcao append(valor)
lista.append('Python')
print(lista)
print(len(lista))
# os elementos de uma lista podem ser acessados por index
print(lista[1])
# os itens de uma lista podem ser removido utilizando a funcçao remove(valor)
lista.remove(10)
print(lista)
print(len(lista))
# podemos adicionar uma lista a outra utilizando a funcao extend(nova_lista)
nova_lista = [1, 2, 3] 
lista.extend(nova_lista)
print(lista)
print(len(lista))
lista = [10, 'David Hadrianus', 1.74, True, [1, 2, 3]]
print(len(lista))
print(lista)
