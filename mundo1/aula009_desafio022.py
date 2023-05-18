#Crie um programa que leia o nome completo de uma pessoa e mostre:
#nome com todos caracteres em letra maiuscula
#todas minusculas
#conte quantas letras tem ao todo (desconsiderando espaços)
#quantas letras tem o primeiro nome


'''
#meus errinhos <3

nome = str(input('Digite seu nome completo:').strip())
print(nome.upper())
print(nome.lower())
dividido = nome.split()
juntado = ''.join(dividido)
print(f'O nome completo possui {len(juntado)} letras!')
print(f'O primeiro nome é {dividido[0]} e ele possui {len(dividido[0])} letras!')


#############
nome = str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome...')
print(f'Seu nome em letras maiúsculas é {nome.upper()}.')
print(f'Seu nome em letras minusculas é {nome.lower()}.')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras.')
#print(f'Seu primeiro nome tem {nome.find(" ")} letras.')
dividido = nome.split()
print(f'Seu primeiro nome é {dividido[0]} e ele tem {len(dividido[0])} letras!')
'''
'''
#NOMES PARA TESTAR
Lohane Vêkanandre Sthephany Smith Bueno de HA HA HA de Raio Laser bala de Icekiss
#OUUUU
Nati Natini Natili Lohana Savic de Albuquerque Pampic de La Tustuane de Bolda, Danusa Deise Medly Leona Meiry Cibele de Bolda de Gasparri. A mulher jamais falada. A menina jamais igualada.
Conhecidíssima como a noite de Paris. Eu sou apertada como uma bacia. Eu sou enxuta como uma melancia.
Tenho dois filhosinho, um zolhudinho, outro barrigudinho. Casei com o dono da Parmalat. Virei mamífera. Só mamo. Pertenço à família imperial brasileira Orleans Bragança. Penetração difícil.

'''

nome = str(input('Digite seu nome completo:')).strip()
'''
print('Vamos analisar o nome digitado...')
print(f'Em letras maiúsculas, seu nome fica {nome.upper()};')
print(f'Em minúsculas, fica {nome.lower()};')
'''
separado = nome.split()
'''
print(f'Sem contar os espaços, seu nome completo contém {len(nome) - nome.count(" ")} letras;')
print(f'Seu primeiro nome é {separado[0]} e ele tem {len(separado[0])} letras!')
'''
print(separado)
juntado = ''.join(separado)
print(juntado)

print(f'Sem espaços, seu nome completo contem {len(juntado)} letras')























