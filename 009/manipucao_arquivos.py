# Operações Fundamentais e Modos de Abertura:
# "r": modo leitura (padrão) - abre o arquivo para ler.
# "w": modo escrita - cria um arquivo novo ou substitui o conteúdo existente.
# "a": modo append (acrescentar) - adiciona conteúdo ao final do arquivo.
# "r+": leitura e escrita.
# "w+": escrita e leitura.
# "a+": append e leitura.
from pathlib import Path

BASE_DIR = Path(__file__).parent
ARQUIVO = BASE_DIR / 'arquivo.txt'

with open(ARQUIVO, 'w') as arquivo:
    arquivo.write('linha 1\n')
    arquivo.write('linha 2\n')
    arquivo.write('linha 3\n')

with open(ARQUIVO, 'r') as arquivo:
    print(arquivo.read())

with open(ARQUIVO, 'a') as arquivo:
    arquivo.write('linha 4\n')
    arquivo.write('linha 5\n')

with open(ARQUIVO, 'r') as arquivo:
    print(arquivo.read())
