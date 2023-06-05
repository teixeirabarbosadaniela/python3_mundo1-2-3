#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a idade:
#Se ele ainda vai se alistar para o serviço militar;
#Se é a hora de se alistar;
#Se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

anoNascimento = int(input('Qual seu ano de nascimento?'))

from datetime import date
idade = date.today().year - anoNascimento

if idade > 18:
    print(f'Já passou o tempo para seu alistamento, você tem {idade} anos, deveria ter se alistado há {idade-18} anos.')
    print(f'Seu ano de alistamento foi {anoNascimento+18}.')
elif idade == 18:
    print(f'Você tem {idade}, deve se alistar imediatamente.')
elif idade < 18:    #ou else:
    print(f'Não é hora de se alistar! Você tem apenas {idade}, ainda faltam {18-idade} anos.')
    print(f'Seu alistamento será em {anoNascimento+18}.')