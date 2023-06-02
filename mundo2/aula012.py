#Condições aninhadas

name = str(input('Em quem você votou?')).lower().strip()
if name == 'lula':                         #condição simples
    print('Bacana, ele foi eleito na tentativa de encerrar a ascenção fascista!')
    print('Agora, continue politicamente ativo e cobrando o governo!')
    print('Porque o captalismo ainda é selvagem,\no apaziguamento da classe trabalhadora tá fungando no seu cangote \ne o fascismo continua entranhado em 50% da população!')
elif name == 'bolsonaro' or name == 'mito':  #aninhada
    print('Vagabunde ordinário, vai procurar o parachoque de um caminhão pra dar uma volta!')
elif name in 'o voto é secreto' or 'terceira via':
    print('Tenha um dia miserável!')
else:                                      #condição composta
    print('Onde você esteve nos últimos anos, vida?')
print('A classe trabalhadora tudo produz, à ela tudo pertence!')


