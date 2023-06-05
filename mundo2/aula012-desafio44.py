#Elabore um programa que calcule o valor a ser pago por um produto, considerando o
#seu preço normal e condição de pagamento:
#À vista em dinheiro/cheque: 10% de desconto;
#À vista no cartão: 5% de desconto;
#Em até 2x no cartão: preço normal (não paga juros);
#3x ou mais no cartão: 20% de juros.

print(15*'='+ " BARBOSA'S MAGAZINE " + 15*'=')
price = float(input('what is the price of the purchases?'))

print('payment methods'.upper(), end ='')
print('''
        [ 1 ] in cash or check
        [ 2 ] credcard
        [ 3 ] credcard (until 2x) 
        [ 4 ] credcard (3x or more)''') #those options (3 and 4) exist in brazil
option = int(input('Which payment method do you choose?'))
if option == 1:
    print(f'With method [ 1 ], cash or check payment, your purchase of ${price:.2f} will cost ${price-(price*0.1):.2f}.')
elif option == 2:
    print(f'With method [ 2 ], credcard payment, your purchase of ${price:.2f} will cost ${price-(price*0.05):.2f}.')
elif option == 3:
    print(f'With method [ 3 ], credcard payment (until 2x), so each month you will need to pay {(price / 2):.2f} with no extra costs.')
elif option == 4:
    fourthextra = price+(price*0.2)
    print(f'With method [ 4 ], credcard payment (3x or more), your purchase of ${price:.2f} will cost ${fourthextra:.2f} total.')
    fourthMethodChoice = int(input('How many times do you want?'))
    if fourthMethodChoice >=3 and fourthMethodChoice <= 12:
        print(f'You chose {fourthMethodChoice}x, so each portion will cost {(fourthextra/fourthMethodChoice):.2f} with extra costs.')
    else:
        print('This number has exceeded our limits. Please, try again with a smaller number between 3 and 12x.')
else:
    print('invalid option, reread the instructions and try again!')