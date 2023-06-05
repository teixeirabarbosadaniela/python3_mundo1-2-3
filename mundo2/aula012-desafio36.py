#Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário,
#caso contrário, o emprestimo será negado.

valorImovel = float(input('Qual o valor do imóvel que deseja? R$'))
valorSalario = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Em quantos anos deseja quitar este imóvel?'))

valorParcelaMinima = valorSalario * 30/100
valorParcelas = valorImovel / (anos*12)

if valorParcelas <= valorParcelaMinima:
    print(f'Sua simulação de empréstimo foi aprovada, serão R${valorParcelas:.2f} em {anos} anos!')
else:
    print(f'Sua simulação de empréstimo foi negada.')



