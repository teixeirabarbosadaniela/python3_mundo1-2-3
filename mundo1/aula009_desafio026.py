#Leia uma frase qualquer e mostre #
#(1) quantas vezes aparece a letra 'A';
#(2) em que posição o 'A' aparece na primeira vez;
#(3) em que posição o 'A' aparece na ultima vez.


frase = str(input('Digite uma frase:')).strip().lower()
print(f'A letra "A" apareceu {frase.count("a")} vezes!')
print(f'Da primeira vez, a letra "A" aparece na posição {frase.find("a")+1}') #o '+1' é só pra compensar o zero do primeiro caractere
print(f'Da última vez, a letra "A" aparece na posição {frase.rfind("a")+1}')
