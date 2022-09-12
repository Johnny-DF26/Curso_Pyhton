from random import randint

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):       # metodo de instancia, precisa receber o "self"
        print(f'{self.ano_atual - self.idade}')

    @classmethod                         # não é referente a instacia mais em si a classe
    def por_ano_nascimento(clas, nome, ano_nascimento):
        idade = clas.ano_atual - ano_nascimento
        return clas(nome, idade)


p1 = Pessoa('Anna', 23)
