#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
ppo = float(input('Qual é o preço do produto? R$')) #PreçoProdutoOriginal
ppd = ppo-(ppo*(5/100)) #PreçoProdutocomDesconto
print(f'O produto custava R${ppo:.2f}, na promoção com desconto de 5% ele passa a custar R${ppd:.2f}')

