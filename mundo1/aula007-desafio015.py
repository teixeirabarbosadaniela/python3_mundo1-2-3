#Escreva um programa que pergunte a quantidade de km percorridos por um carro locado e
# a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.
qd = int(input('Quantos dias alugados?'))
qkm = int(input('Quantos km rodados?'))
diaria = (60*qd)+(0.15*qkm)

print(f'O total a pagar é de R${diaria:.2f}')
