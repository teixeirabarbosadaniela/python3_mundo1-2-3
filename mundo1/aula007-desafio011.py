#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
#e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

lp = float(input('Digite a largura da parede:'))
ap = float(input('Digite a altura da parede:'))
atdp = lp*ap  #AreaTotalDaParede
print(f'Sua parede tem dimensão de {lp:.2f}x{ap:.2f}, sendo sua área total de {atdp:.2f}m².')
tinta = atdp/2
print(f'Para pintar esta parede, você vai precisar de {tinta:.1f}l de tinta.')

