print('===================CORES===================')

print('\033[1;31mOlá Mundo')
print('\033[4;30m Olá Mundo !\033[m')
print('\033[0;30;41mOlá Mundo!\033[m')
print('\033[1;35mOlá Mundo!\033[m')
print('\033[4;33;44mOlá Mundo!\033[m')

a = 3
b = 4

print('Os valores são \033[1;34m{}\033[m e \033[1;31m{}\033[m!!!!'.format(a,b))

nome = 'Johnny'
print('Muito prazer {}{}{}!!'.format('\033[4;34m', nome, '\033[m'))

cores = {'limpa':'\033[n', 'azul'
        :'\033[33m', 'amarelo':'\033[33m'}

print('Ola muit prazer em te conhecer, {}{}{}'.format(cores['amarelo'],nome,cores['limpa']))