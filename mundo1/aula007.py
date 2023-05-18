n1 = (int(input('Digite um número:')))
n2 = (int(input('Digite outro número:')))
s = n1+n2
sub = n1-n2
d = n1/n2
di = n1//n2
rd = n1%n2
m = n1*n2
p = n1**n2
print(f'A soma dos dois números resulta em {s};')
print(f'A subtração dos dois números resulta em {sub};')
print(f'A divisão dos dois números resulta em {d};')
print(f'A divisão inteira dos dois números resulta em {di};')
print(f'O resto da divisão é {rd:.3f};')
print(f'A multiplicação dos dois números resulta em {m}')
print(f'O primeiro numero elevado ao segundo número resulta em {p}')
#########################
print(f'A soma resulta em {s} e subtração em {sub}. Já a divisão resultou em {d}, enquanto em números inteiros deu {di} com resto de {rd}. Multiplicação resultou em {m} e a potencia do primeiro número pelo segundo é {p}.')
########################
print(f'A soma resulta em {s} e subtração em {sub}.', end=' ')
print(f'Já a divisão resultou em {d}, enquanto em números inteiros deu {di} com resto de {rd}.', end=' ')
print(f'Multiplicação resultou em {m} e a potencia do primeiro número pelo segundo é {p}.')
########################
print(f'A soma resulta em {s} e subtração em {sub}.\nJá a divisão resultou em {d}, enquanto em números inteiros deu {di} com resto de {rd}.\nMultiplicação resultou em {m} e a potencia do primeiro número pelo segundo é {p}.')