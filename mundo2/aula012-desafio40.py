#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem
#no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO;
#Média entre 5.0 e 6.9: RECUPERAÇÃO;
#Média 7.0 ou superior: APROVADO.

firstGrade = float(input('Enter your first grade:'))
secondGrade = float(input('Enter your second grade:'))

average = (firstGrade + secondGrade)/2

if average < 5.0:
    print(f'Your average grade is {average}, so you FAILED.')
elif average > 5.0 < 6.9:  #or average > 5.0 and average < 6.9:
    print(f'Your average grade is {average}, so you go to RECOVERY class.')
elif average >= 7.0:
    print(f'Your average grade is {average}, so you are APPROVED.')