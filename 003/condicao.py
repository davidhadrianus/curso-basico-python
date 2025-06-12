
# Sintaxe

# if condicao:
#     instrucaos
# elif outra_condicao:
#     instrucaos
# else:
#     instrucaos 

# Exemplos

idade1 = int(input('Digite sua idade1: '))
idade2 = int(input('Digite sua idade2: '))

if idade1 > idade2:
    print(f'{idade1} e maior que {idade2}')
elif idade1 < idade2:
    print(f'{idade1} e meno que {idade2}')
else:
    print(f'{idade1} e igual a {idade2}')

# utilizando match case
dias_semana = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']

dia = input('Digite um dia: ')

match dia:
    case 'sabado' | 'domingo':
        print('Fim de semana')
    case _:
        print('Dia util')