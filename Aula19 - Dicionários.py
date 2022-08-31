
filme = {'Título':'Star Wars','Ano': 1977,'Diretor':'George Lucas'}

for k,v in filme.items():
    print(f"O {k} é {v}")

pessoas = {'nome': 'Johnny','sexo':'M','idade':29}

print(f"O {pessoas['nome']} tem {pessoas['idade']} anos")
print(pessoas.keys()) # mostra a chaves do dicionario
print(pessoas.values()) # mostra os valores dentro do dicionario
print(pessoas.items()) # mostra todos itens do dicionario

brasil = list()
estado1 = {'uf':'Rio de  Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[1])
print(brasil[0]['sigla'])

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado['sigla'] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())
for e in brasil:
    print(e)
    for k,v in e.items():
        print(f"O campo {k} tem valor {v}")
