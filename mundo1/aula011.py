#Aula de padrão ANSI
'''
#ESTILO/STYLE
0 = NULO
1 = NEGRITO
4 = UNDERLINE
7 = INVERTE/NEGATIVO

#TEXTO                        #FUNDO/BACK
30 = BRANCO                    40
31 = VERMELHO                  41
32 = VERDE                     42
33 = AMARELO                   43
34 = AZUL                      44
35 = LILAS/MAGENTA             45
36 = CIANO                     46
37 = CINZA                     47

ENCERRA CONFIGURAÇÃO: '\033[m'

#outra maneira

cores = {'limpa' :'\033[m', 'azul':'\033[34m', 'vermelho':'\033[31m'} #e, assim, sucessivamente!


print('Olá \033[1;36;43mmundo\033[m!')
print('Olá \033[1;33;41mmundo\033[m!')
'''

cores = {'limpa' :'\033[m', 'azul':'\033[34m', 'vermelho':'\033[31m'}
print(cores['azul'] Dani )