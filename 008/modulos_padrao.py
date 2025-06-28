import math
from math import sqrt
import datetime
import random

print(f'raiz: {math.ceil(sqrt(16))}') # raiz quadrada
print(f'potencia: {math.pow(2, 3)}') # potencia
print(f'valor pi: {math.floor(math.pi)}')
print(f'arredondamento: {math.ceil(2.9)}') # arredonda para cima
print(f'arredondamento: {math.floor(2.9)}') # arredonda para baixo

hoje = datetime.date.today()
print(hoje)
agora = datetime.datetime.now()
print(agora)

print(random.randint(1, 10))
print(random.choice(['a', 'b', 'c']))
