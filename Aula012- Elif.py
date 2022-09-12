nome = str(input('Qual é seu nome: ')).strip().upper()
if nome == 'JOHNNY':
    print('Que nome bonito!!')
elif nome == 'PEDRO' or nome == 'MARIA' or nome == 'PAULO':
    print('\033[031mSeu nome é bem popular no Brasil !\033[m')
elif nome in ('ANA CLAUDIA JESSICA JULIANA'):
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia \033[36m{}\033[m !!'.format(nome))
