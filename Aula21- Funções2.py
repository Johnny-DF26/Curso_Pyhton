#  Interactive Help

'''print(input.__doc__)
help(print)'''

#  Docstrings, argumentos opcionais em funções

'''ef somar(a,b,c=0):  # def somar(a=0,b=0,c=0)
    """ # digita aspas duplas e press enter
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    """
    s = a + b + c
    print(f'A soma vale: {s}')


somar(8,4)'''

'''def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
funcao()
print(f'N1 fora vale {n1}')'''


#  Utilizando 'global':

'''def teste(b):
    #  global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')'''

#  Retornando valores return


'''def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 1)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')'''

'''from math import factorial


def fatorial(num=1):
    f = factorial(num)
    return f


while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    print(fatorial(n))

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')'''


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    if par(num):
        print('É par!')
    else:
        print('Não é par!')
