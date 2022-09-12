"""def mostraLinha():
    print('--' * 20)


mostraLinha()
print('          SITEMAS DE ALUNOS      ')
mostraLinha()
print('          PRENDA PYTHON          ')
mostraLinha()"""

"""def mensagem(msg):
    print('-' * 20)
    print(msg)
    print('-' * 20)


mensagem(' Sistema de alunos')
mensagem(' Aprendendo funcoes')"""


"""def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


soma(b=4, a=5)
soma(7,2)"""


"""def contador(*num):
    print(num)


contador(5,7,3,1,4)
contador(8,4,7)"""


"""def contador(*num):
    for valor in num:
        print(valor,end=' ')
    print('FIM')


contador(5,7,3,1,4)
contador(8,9)
contador(4,4,7,6,2)"""


"""def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')


contador(5,7,3,1,4)
contador(8,9)
contador(4,4,7,6,2)"""


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6,3,9,1,0,2]
dobra(valores)
print(valores)
