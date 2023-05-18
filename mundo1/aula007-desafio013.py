#Faça um algoritmo que leia o salario de um funcionário e mostre seu novo salario, com 15% de aumento.
salario1 = float(input('Qual o valor do seu salario atualmente? R$'))
salario2 = salario1+(salario1*15/100)
abono = (salario1*15/100)
print(f'Você recebeu 15% de aumento sobre seu valor de salario atual. Com o reajuste, vocÊ passará a receber R${salario2:.2f}, uma diferença de R${abono:.2f}.')
