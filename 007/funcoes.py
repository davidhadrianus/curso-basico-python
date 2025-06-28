# sintaxe basica
def nome_da_funcao():
    print('Executando a funcao')

nome_da_funcao()
# funcoes com parametros
def saudacao(nome):
    print(f'Ola, {nome}')

saudacao('David')
# funcao com parametros nomeados
def informacao(nome, idade):
    print(f'Nome: {nome}, Idade: {idade}')

informacao(nome='David', idade=30)
# funcoes com retorno
def soma(a, b):
    return a + b

print(soma(5,3))
# funcoes com parametros opcional
def saudacoes(nome='Visitante'):
    print(f'saudacoes, {nome}')

saudacoes()
saudacoes('David')
# funcao com numero indefinido de argumentos
def lista_nome(*nomes):
    for nome in nomes:
        print(f'Nome: {nome}')

lista_nome('David', 'Hadrianus', 'Nataniela', 'Uriel')
# funcao com varios parametros nomeados e indefinidos
def informacoes(**dados):
    """
    returna chave e valor
    """
    for chave, valor in dados.items():
        print(f'{chave}: {valor}')

informacoes(nome='David', altura='1.74', morada='Luanda/Angola')
# funcoes lambdas
dobro = lambda x: x * 2
print(dobro(5))