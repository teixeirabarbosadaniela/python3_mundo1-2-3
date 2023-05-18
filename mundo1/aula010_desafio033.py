#Programa que leia 3 números e identifique qual é o maior e o menor entre eles.
a = int(input('Digite um numero'))
b = int(input('Digite um numero'))
c = int(input('Digite um numero'))

#Verificando quem é menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print(f'{menor}')

#Verificando maior

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f'{maior}')
