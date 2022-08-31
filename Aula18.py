"""
galera = [['maria', 25], ['joao', 13], ['kleber',28],['ana',25]]

print(galera[2][0])
pessoas = list(galera[:])
animais = list(galera[:])
galera.append(['Julia',28])
print(galera)
print(pessoas)
print(animais)


galera = [['Joao',19], ['ana',33], ['Joaquim',13], ['Maria',45]]
for p in galera:
    print(f"{p[0]} tem {p[1]} anos")
"""

galera = list()
dado = list()
tot = 0
totMenor = 0
for c in range(0,3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()
print("=="*30)
for c in galera:
    print(f"Nome: {c[0]} - Idade: {c[1]}")
print("=="*30)
for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior e idade")
        tot += 1
    else:
        print(f"{p[0]} é menor de idade")
        totMenor += 1
print("=="*30)
print(f"{tot} pessoas são maiores de idade")
print(f"{totMenor} pessoas são menores de idade")
