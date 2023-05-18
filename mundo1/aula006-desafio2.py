#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações sobre ele

x = input('Digite algo:')
print(x, 'É do tipo primitivo', type(x))
print('A informação que você digitou possui apenas números?', x.isnumeric(), '!')
print('A informação que você digitou possui apenas letras?', x.isalpha(), '!')
print('A informação que você digitou é um espaço?', x.isspace(), '!')
print('A informação que você digitou possui apenas letras minúsculas?', x.islower(), '!')
print('A informação que você digitou possui apenas letras maiúsculas?', x.isupper(), '!')


