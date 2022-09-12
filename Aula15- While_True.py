
print('')
print('-----------------------LEITOR DE NUMEROS--------------------------')
soma = 0
cont = 0
while True:
    num = int(input('Digite um numero: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Foram digitados {cont} numeros e soma entre eles é: {soma}')




