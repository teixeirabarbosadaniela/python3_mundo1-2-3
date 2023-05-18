#Leia o nome completo de uma pessoa, mostrando o primeiro e o último nome separadamente.
#EX.: Ana Maria de Souza
# primeiro = Ana
# ultimo = Souza

nome = str(input('Digite um nome completo:')).strip().split()
print(f'Primeiro nome = {nome[0]}')
print(f'Último nome = {nome[-1]}')

'''
Sugestões de nome:
Virgulino Ferreira da Silva
Chica da Silva
Luiz Inácio da Silva
Marielle Francisco da Silva
Carolina Maria de Jesus
Conceição Evaristo
Djamila Ribeiro
Noémia de Sousa
Alice Walker
Maya Angelou
Bell Hooks
Chimamanda Adichie
Lélia González
Sueli Carneiro
Carla Akotirene
Maria Beatriz Nascimento
Abdias do Nascimento
Silvio Almeida

'''
