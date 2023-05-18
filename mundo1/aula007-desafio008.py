#Escreva um programa que leia um valor em metros e o exiba convertido em centrimetros e milimetros.
vm = int(input('Digite qual o comprimento da sua rua em metros:'))
km = vm/1000
hm = vm/100
dam = vm/10
dm = vm*10
cm = vm*100
mm = vm*1000
print(f'A seguir, temos as conversões de valor digitado: \nquilômetros: {km:.3f}km; \nhectômetro: {hm:.2f}hm; \ndecametro: {dam:.1f}dam; \ndecímetro: {dm:.0f}dm; \ncentímetros: {cm:.0f}cm; \nmilímetros: {mm:.0f}mm.')