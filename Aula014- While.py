'''for cont in range(1,11):
    print(cont, end=' ')
print('Fim') - Posso usar quando sei o limite

c = 1
while c < 10:
    print(c, end=' ')
    c += 1
print('fim')'''


'''for cont in range(1,6):
    num = int(input('Digite um numero: '))
print('FIM')'''
'''resp = 'S'
while resp == 'S':
    num = int(input('Digite um numero: '))
    resp = str(input('Voce deseja continuar [S/N]: ')).strip().upper()
print('FIM')'''

n = 1
par = 0
sPar = 0
impar = 0
sImpar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            sPar = sPar + n
            par += 1

        else:
            sImpar = sImpar + n
            impar += 1


print(f'Voce digitou {par} numeros pares e {impar} numeros impares')
print(f'A soma dos numeros pares é {sPar} e a soma dos ímpares é {sImpar}')
