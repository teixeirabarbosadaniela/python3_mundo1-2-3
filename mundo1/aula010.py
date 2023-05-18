n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1+n2)/2
print(f'Sua média foi: {m:.1f}')
if m >= 5.0:
    print('Não fez mais que a sua obrigação!')
else:
    print('Tá com nota negativa, mô! Te vejo semestre que vem, melhore!')

########################## condicao
# simplificada:
'''print('PARABENS pelo esforço'if m>5.0 else 'LASCOU-SE, melhore')'''


