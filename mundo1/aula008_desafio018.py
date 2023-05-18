# Faça um programa que leia um angulo qualquer e mostre o valor do seno, cosseno e tangente.

import math
ang = float(input('Digite o angulo que deseja:'))
'''precisa converter o 'ang' p radianos  pq na funcionalidade '.cos/sin/tan' a variavel está em radianos '''
seno = math.sin(math.radians(ang))
print(f'o ângulo de {ang} tem o SENO de {seno:.2f}')
cosseno = math.cos(math.radians(ang))
print(f'o ângulo de {ang} tem o COSSENO de {cosseno:.2f}')
tangente = math.tan(math.radians(ang))
print(f'o ângulo de {ang} tem o TANGENTE de {tangente:.2f}')

#OU

from math import sin,cos, tan, radians
ang = float(input('Digite o angulo que deseja:'))
'''precisa converter o 'ang' p radianos  pq na funcionalidade '.cos/sin/tan' a variavel está em radianos '''
seno = sin(radians(ang))
print(f'o ângulo de {ang} tem o SENO de {seno:.2f}')
cosseno = cos(radians(ang))
print(f'o ângulo de {ang} tem o COSSENO de {cosseno:.2f}')
tangente = tan(radians(ang))
print(f'o ângulo de {ang} tem o TANGENTE de {tangente:.2f}')


