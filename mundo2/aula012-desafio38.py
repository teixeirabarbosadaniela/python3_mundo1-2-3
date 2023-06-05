#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela a mensagem:
#O primeiro valor é maior;
#O segundo valor é maior;
#Não existe valor maior, os dois são iguais.

n1 = int(input('Digite um número inteiro:'))
n2 = int(input('Digite outro número inteiro:'))

if n1 > n2:
    print(f'O PRIMEIRO número foi {n1} e ele é o MAIOR.')
elif n2 > n1:
    print(f'O SEGUNDO número foi {n2} e ele é o MAIOR.')
elif n1 == n2:  #ou else:
    print('Não existe valor maior, os dois são iguais.')