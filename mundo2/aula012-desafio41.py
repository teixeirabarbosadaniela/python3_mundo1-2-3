#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
#e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM;
#Até 14 anos: INFANTIL;
#Até 19 anos: JUNIOR;
#Até 25 anos: SÊNIOR;
#Acima: MASTER.

birthYear = int(input('What is your year of birth?'))
from datetime import date
age = date.today().year - birthYear

if age <= 9:
    print(f'You have {age} years old, so you belong to JUNIORs group.')
elif age <= 14: #no need to "age >= 10 and"
    print(f'You are {age} years old,so you belong to TEENAGEs group. ')
elif age <= 19: #no need to "age >=15 and"
    print(f'You are {age} years old,so you belong to YOUNGs group.')
elif age <= 25:
    print(f'You are {age} years old,so you belong to SENIORs group.')
else:
    print(f'You are {age} years old,so you belong to MASTERs group.')
