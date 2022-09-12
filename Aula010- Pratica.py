nome = int(input('Qual a senha: '))

if nome == 2612:
    print('Senha correta !')
else:
    print('Senha Inválida, tente novamente !')
print('----------------------------------------------------------------------')

n1 = float(input('Digite sua nota: '))
n2 = float(input('Digite outr nota: '))

media = (n1 + n2) / 2


if media >= 6.0:
    print('Sua média foi {:2.f}.VOCE ESTA APROVADO !'.format(media))
else:
    print('Sua média foi {:.2f}.VOCE ESTA REPROVADO !'.format(media))



