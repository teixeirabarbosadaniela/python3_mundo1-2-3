#Desenvolva uma lógica que leia o peso e altura de uma pessoa. Calcule seu IMC e mostre
#seu status, de acordo com a tabela abaixo:
#Abaixo de 18.5: ABAIXO DO PESO;
#Entre 18.5 e 25: PESO IDEAL;
#De 25.1 até 30: SOBREPESO;
#De 30.1 até 40: OBESIDADE;
#Acima de 40.1: OBESIDADE MÓRBIDA.

print('Lets calculate your Body mass index (BMI)!')
w = float(input('How much do you weigh (Kg)?'))
h = float(input('What is your height? (m)'))

bmi = w/(h**2)

if bmi <= 18.5:
    print(f'Your BMI is about {bmi:.1f}, and you are UNDER WEIGHT.')
elif bmi <= 25:
    print(f'Your BMI is about {bmi:.1f}, and you have the IDEAL WEIGHT.')
elif bmi <= 30:
    print(f'Your BMI is about {bmi:.1f}, and you are OVERWEIGHT.')
elif bmi <= 40:
    print(f'Your BMI is about {bmi:.1f}, and you have OBESITY.')
else:
    print(f'Your BMI is about {bmi:.1f}, and you have MORBID OBESITY.')


