"""
listaNomes = []

while True:
    nome = str(input('Digite seu nome: '))
    listaNomes.append(nome)
    resp = str(input("Deseja continaur ?[S/N]")).strip().upper()
    if resp == 'N':
        break
print(f'A lista é: {listaNomes}')

minhaLista = [1, "Silva", 4.5]
minhaLista[0] = 2
minhaLista[1] = "João da Silva"
print(minhaLista)
minhaLista.pop()
print(minhaLista)

minhalista = ['Pedro', 'Maria','Anna','Silva',2]
minhalista.remove('Anna')
print(minhalista)


minhaLista3 = ["João", "Maria", "Anna", "Silva"]
try:
    minhaLista3.remove("Maria")
    print(minhaLista3)
except:
    print("O valor não existe na lista")
"""
import math
from math import sqrt
num = int(input('Digite um numero: '))
try:
    raiz = sqrt(num)
    print(f'{raiz:.2f}')
except Exception or TypeError or ValueError:
    print('O número que voce digitou é negativo ou inválido !!\nTransformado em positivo é: ',end='')
    num = -num
    raiz = math.sqrt(num)
    print(f'{raiz:.2f}')
