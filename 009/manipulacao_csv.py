from pathlib import Path
import csv

BASE_DIR = Path(__file__).parent
ARQUIVO = BASE_DIR / 'arquivo.csv'

lista = [
    ['nome', 'idade', 'Cidade'],
    ['Lourenco', 86, 'Catete'],
    ['Ana', 68, 'Dondo'],
]

dicionario = [
    {'nome': 'David', 'idade': 30, 'cidade': 'Luanda'},
    {'nome': 'Joao', 'idade': 20, 'cidade': 'Luanda'},
    {'nome': 'Maria', 'idade': 40, 'cidade': 'Luanda'},
]

with open(ARQUIVO, 'w', newline='') as arquivo:
    escrever = csv.writer(arquivo)
    escrever.writerows(lista)

with open(ARQUIVO, 'r', newline='') as arquivo:
    ler = csv.reader(arquivo)
    for linha in ler:
        print(linha)

with open(ARQUIVO, 'w', newline='') as arquivo:
    writer = csv.DictWriter(arquivo, fieldnames=dicionario[0].keys())
    writer.writeheader()
    writer.writerows(dicionario)

with open(ARQUIVO, 'r', newline='') as arquivo:
    reader = csv.DictReader(arquivo)
    for linha in reader:
        print(linha)
