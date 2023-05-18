#Leia nome de uma cidade e diga se ela começa ou nao com o nome 'santo'.
cidade = str(input('Digite o nome da sua cidade:')).strip().lower()
print('Analisando a cidade digitada...')
#inserido como alternativa para nao dar erro na busca pelo nome santo# cidade = cidade.lower()
print(cidade[:6] == 'santo ')
#inserido o espaço no 6º caractere para certificar que nao vai aparecer true de resultado para 'santoS', por exemplo!