#Faça pograma que leia um número de zero a 9999 e mostra na tela cada um dos digitos separadamente.
#Exemplo: digitado foi 1834...unidade:4; dezena:3; centena:8; milhar:1.
# tentar fazer como string e matematicamente

num = int(input('Informe um número de zero a 9999:'))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Analisando o número {num}, temos que:')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')

#dica: se não entendeu a lógica da divisão pela didática do guanabara,
# faz a conta na mão que o insight provavelmente vem :)!