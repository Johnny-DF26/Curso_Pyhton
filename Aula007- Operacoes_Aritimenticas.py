
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

soma = n1 + n2
Sub = n1 - n2
mult = n1 * n2
div = n1 / n2
divInt = n1 // n2
pot = n1 ** n2
ResDiv = n1 % n2

print(' A soma é {} \n A subtracao é {} \n A multiplicação é {} '
      '\n A Divisão é {} \n A potencia é {} \n '
      'A divisão inteira é {} \n O resto da divisão é {} '
      .format(soma,Sub,mult,div,pot,ResDiv,ResDiv))
