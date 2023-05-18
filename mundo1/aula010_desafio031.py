#Pergunte a distancia de uma viagem em km,
#calcule o preço da passagem, cobrando r$0,50/km para viagens de ate 200km
#e R$0,45 para viagens mais longas.


distancia = float(input('Digite a km que vc vai percorrer:'))
curtas = distancia*0.50
longas = distancia*0.45
if distancia <=200:
    print(f'o custo da viagem será R${curtas:.2f}')
else:
    print(f'o custo da viagem será R${longas:.2f}')






