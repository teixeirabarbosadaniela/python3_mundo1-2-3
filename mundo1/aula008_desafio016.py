#Crie um programa que leia um número real qualquer e print sua porção inteira
#EX: Lê 5.678 e mostra 5.

#minha versao
numreal = float(input('Digite um numero real: '))
from math import floor
numinteiro = floor(numreal)
print(f'Você digitou {numreal} e sua porção inteira é:{numinteiro}')


#versoes guanabara
'''
import math
num = float(input('Digite um numero real: '))
print(f'Você digitou {num} e sua porção inteira é:{math.trunc(num)}')


from math import trunc
num = float(input('Digite um numero real: '))
print(f'Você digitou {num} e sua porção inteira é:{trunc(num)}')


num = float(input('Digite um numero real: '))
print(f'Você digitou {num} e sua porção inteira é:{int(num)}')
'''