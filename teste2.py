expr = str(input('Digite a expressão: '))
pilha = list()

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão correta! ')
else:
    print('Expressão incorreta !')