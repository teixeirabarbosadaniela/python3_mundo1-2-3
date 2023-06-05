#Crie um programa que faça o computador jogar JOKENPÔ com você.
#(pedra/papel/tesoura)


print('=-'*15 + ' JOKENPO GAME ' + '=-'*15)
from time import sleep
print('PROCESSING...', end = '')
sleep(1)
print('GAME.')
sleep(1)


from random import randint
items = ('ROCK','PAPER', 'SCISSOR')
computer = randint(0,2)


print('''Your options:
[ 0 ] ROCK
[ 1 ] PAPER
[ 2 } SCISSOR''')

player = int(input('Wich one do you choose?'))

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

#when the player put som random number bigger than 2, the game doesnt work and i dont know why!
print('=-'*10)
print(f'The computer played {items[computer]}')
print(f'The player chose {items[player]}')
print('=-'*10)

#player
if computer == 0: #ROCK
    if player == 0:
        print('TIED')
    elif player == 1:
        print('PLAYER WINS')
    elif player == 2:
        print('COMPUTER WINS')
    else:
        print('ERROR! Invalid, try again!')

elif computer == 1:  #PAPER
    if player == 0:
        print('COMPUTER WINS')
    elif player == 1:
        print('TIED')
    elif player == 2:
        print('PLAYER WINS')
    else:
        print('ERROR! Invalid, try again!')

elif computer == 2:  #SCISSOR
    if player == 0:
        print('PLAYER WINS')
    elif player == 1:
        print('COMPUTER WINS')
    elif player == 2:
        print('TIED')
    else:
        print('ERROR! Invalid, try again!')
else:
    print('Not a valid number, please try again!')



