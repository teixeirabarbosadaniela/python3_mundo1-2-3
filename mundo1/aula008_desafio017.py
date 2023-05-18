#Faça um programa que leia o comprimeiro do cateto oposto adjacente de um triangulo retangulo,
# calcule e mostre o comprimento da hipotenusa.

co = float(input('Digite o comprimento do cateto oposto:'))
ca = float(input('Digite o comprimento do cateto adjascente:'))
hi = (ca**2 + co**2)**(1/2)
print(f'A hipotenusa do triangulo mede {hi:.2f}')
#ou
import math
co = float(input('Digite o comprimento do cateto oposto:'))
ca = float(input('Digite o comprimento do cateto adjascente:'))
hi = math.hypot(co,ca)
print(f'A hipotenusa do triangulo mede {hi:.2f}')
#ou
from math import hypot
co = float(input('Digite o comprimento do cateto oposto:'))
ca = float(input('Digite o comprimento do cateto adjascente:'))
hi = hypot(co,ca)
print(f'A hipotenusa do triangulo mede {hi:.2f}')