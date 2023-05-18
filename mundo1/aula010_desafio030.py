#Leia um numero inteiro e mostre se é par ou impar.



numero = int(input('Digite um número inteiro:'))
resultado = numero%2
if resultado == 1:
 print('O número digitado é IMPAR')
else:
 print('O número digitado é PAR')
