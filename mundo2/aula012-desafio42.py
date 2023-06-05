#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
#será formado:
#Equilátero: todos os lados iguais;
#Isósceles: dois lados iguais;
#Escaleno: todos os lados diferentes.

ladoA = float(input('Digite o primeiro segmento:'))
ladoB = float(input('Digite o segundo segmento:'))
ladoC = float(input('Digite o terceiro segmento:'))

if ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoA + ladoB:
    print('Triangulo POSSÍVEL')

    if ladoA == ladoB == ladoC:
        print('As medidas formam um triângulo EQUILÁTERO.')
    elif ladoA != ladoB != ladoC != ladoA:
        print('As medidas formam um triângulo ESCALENO.')
    else:                   #ou ladoA == ladoB != ladoC or ladoB == ladoC != ladoA or ladoC == ladoA != ladoB:
        print('As medidas formam um triângulo ISÓSCELES.')

else:
    print('Triangulo IMPOSSÍVEL, tente novamente')

