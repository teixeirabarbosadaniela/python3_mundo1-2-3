#Programa que faça o computador pensar em um numero inteiro entre 0 e 5
#peça ao usuario pra tentar descobrir qual foi o numero escolhido
#programa deve revelar se usuario acertou ou errou.



from random import randint
from time import sleep
nhipotetico = int(input('Digite um número entre zero a cinco:'))
nmisterioso = randint(0,5)
print('PROCESSANDO...')
sleep(2)
if nhipotetico == nmisterioso:
    print(f'Parabéns, você acertou! Pensei mesmo no número {nmisterioso}')

elif nhipotetico != [0, 1, 2, 3, 4]:
    print(f'Você digitou {nhipotetico}, eu preciso de um número entre 0 e 4!')

else:
    print(f'Tente outra vez! Você digitou {nhipotetico}, eu pensei em {nmisterioso}')
