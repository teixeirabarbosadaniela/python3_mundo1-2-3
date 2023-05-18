#Programa que leia velocidade de um carro.
#Se ultrapassar 80km/h, mostre que usuario foi multado e
#informe que a multa vai custar r$7,00 por cada km acima do limite.


velocidade = float(input('Digite a velocidade do carro:'))
if velocidade >80:
    print(f'Você está a {(velocidade):.2f}km/h, portanto será multado porque ultrapassou a velocidade máxima de 80km/h. Deverá pagar R${((velocidade-80)*7):.2f} de multa.')
else:
    print('Tenha um bom dia, dirija com segurança!')