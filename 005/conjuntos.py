
conjunto1 = {1,2,3,4}
conjunto2 = {3,4,5,6}

conjunto_uniao = conjunto1.union(conjunto2)
print(conjunto_uniao)

conjunto_interseccao = conjunto1.intersection(conjunto2)
print(conjunto_interseccao)

conjunto_diferenca = conjunto1.difference(conjunto2)
print(conjunto_diferenca)

conjunto_diferenca_simetrica = conjunto1.symmetric_difference(conjunto2)
print(conjunto_diferenca_simetrica)

print(conjunto1.issubset(conjunto2))
print(conjunto1.issuperset(conjunto2))

print(conjunto1.discard(3))
print(conjunto1)

conjunto1.clear()
print(conjunto1)