#Manipulando textos - cadeia de caracteres = strings

frase = 'Curso em Video Python'

#FATIAMENTO
print(frase [9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

#ANALISE
print(len(frase))
print(frase.count('o'))
print(frase.find('deo'))
print(frase.find('androide'))
print('Curso' in frase)
print('curso' in frase) #resultado difere se maiuscula

#TRANSFORMAÇÃO
print(frase.replace('Python', 'Androide'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())
print(frase.split())

dividido = frase.split()
print(dividido[0])

dividido = frase.split()
print(dividido[2][3]) #do divivido '2' = video; me mostre a letra '3' = e

print(frase.join()) #?




