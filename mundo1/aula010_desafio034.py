#Pergunte o salário de um funcionario e calcule o valor do seu aumento.
#Para salarios superiores a R$1.250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.

salario_atual = float(input('Qual o valor do seu salário, trabalhador?'))
salario_reajustado15 = ((salario_atual) * 15 / 100) + salario_atual
salario_reajustado10 = ((salario_atual) * 10 / 100) + salario_atual
if salario_atual <= 1250:
    print(f'Seu salário, considerando o reajuste de 15%, passará a ser R$ {salario_reajustado15:.0f}.')
else:
    print(f'O reajuste pra sua faixa salarial é de 10%, portanto seu salário passará a ser R$ {salario_reajustado10:.0f}.')


