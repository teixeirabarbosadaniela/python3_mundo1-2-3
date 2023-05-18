#Leia o comprimento de 3 retas e diga se pode ou nao formar um triângulo.
ladoA = float(input('Digite o primeiro segmento:'))
ladoB = float(input('Digite o segundo segmento:'))
ladoC = float(input('Digite o terceiro segmento:'))
'''
if (ladoB - ladoC) > ladoA < ladoB + ladoC:
    print('Triangulo possível')
elif (ladoA - ladoC) > ladoB < ladoA + ladoC:
    print('Triangulo possível')
elif (ladoA - ladoB) > ladoC < ladoA + ladoB:
    print('Triangulo possível')
else:
    print('Triangulo impossível')
    
'''
if ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoA + ladoB:
    print('Triangulo POSSÍVEL')
else:
    print('Triangulo IMPOSSÍVEL, tente novamente')