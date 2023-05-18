#Um professor quer sortear um dos seus quatro estudantes para apagar o quadro.
#faça um programa que leia o nome dos candidatos e eleja um deles aleatoriamente

import random

nome1 = str(input('Digite o nome do primeiro estudante:'))
nome2 = str(input('Digite o nome do segundo estudante:'))
nome3 = str(input('Digite o nome do terceiro estudante:'))
nome4 = str(input('Digite o nome do quarto estudante:'))

lista = [nome1,nome2,nome3,nome4]
sorteado = random.choice(lista)
print(f'Parabéns, {sorteado}! Você foi sortead(o/a/e) para fazer o trabalho de corno!')
if sorteado == 'InesBrasil':
    print('ALÔALÔ-Graças a deuix!')






