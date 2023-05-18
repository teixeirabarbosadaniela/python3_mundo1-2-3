#Sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia os nomes dos 4 alunos e mostre a ordem.

'''
#os erros

import random
nome1 = str(input('Digite o primeiro nome:'))
nome2 = str(input('Digite o segundo nome:'))
nome3 = str(input('Digite o terceiro nome:'))
nome4 = str(input('Digite o quarto nome:'))

lista = [nome1,nome2,nome3, nome4]

sorteado1 = random.choice(lista)
sorteado2 = random.choice(lista)
sorteado3 = random.choice(lista)
sorteado4 = random.choice(lista)

print(f'A ordem de apresentação será {sorteado1}, {sorteado2}, {sorteado3} e {sorteado4}!')

#assim pode repetir os itens da lista ¬¬'
-----

import random

nome1 = str(input('Digite o primeiro nome:'))
nome2 = str(input('Digite o segundo nome:'))
nome3 = str(input('Digite o terceiro nome:'))
nome4 = str(input('Digite o quarto nome:'))

lista = [nome1,nome2,nome3, nome4]

sorteado = random.choices(lista)
print(f'A ordem de apresentação será {sorteado}, {sorteado}, {sorteado} e {sorteado}!')

#sorteou os mesmos nomes
'''

import random
nome1 = str(input('Digite o primeiro nome:'))
nome2 = str(input('Digite o segundo nome:'))
nome3 = str(input('Digite o terceiro nome:'))
nome4 = str(input('Digite o quarto nome:'))
lista = [nome1,nome2,nome3, nome4]
random.shuffle(lista)
print(f'A ordem de apresentação será {lista}!')

from random import shuffle
nome1 = str(input('Digite o primeiro nome:'))
nome2 = str(input('Digite o segundo nome:'))
nome3 = str(input('Digite o terceiro nome:'))
nome4 = str(input('Digite o quarto nome:'))
lista = [nome1,nome2,nome3, nome4]
shuffle(lista)
print(f'A ordem de apresentação será {lista}!')

#guanabara informou que pode repetir por ser randomico,
# mas existe um que cancele a possibilidade de repetição do mesmo item?