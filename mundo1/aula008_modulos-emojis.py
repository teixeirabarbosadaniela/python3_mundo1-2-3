import math
num = int(input('Digite um numero:'))
raiz = math.sqrt(num)
print(f'A raiz de {num} é igual a {math.ceil(raiz)}!')

###############################
from math import sqrt, floor, ceil
num = int(input('Digite um numero:'))
raiz = sqrt(num)                                                                  
print(f'A raiz de {num} é igual a {floor(raiz)}!')
print(f'A raiz de {num} é igual a {ceil(raiz)}!')
###############################

import random
num = random.random()
print(num)

num2 = random.randint(1,100)
print(num2)

###################

import emoji

print(emoji.emojize('Olá, mundo :innocent:', language = 'alias'))
print(emoji.emojize("quando não da SYNTAXERROR,:snake: é massa :smile::brown_heart:", language ='alias'))
print(emoji.emojize('que soninho :sleeping:', language='alias'))
print(emoji.emojize('miss u:whale:', language='alias'))




















