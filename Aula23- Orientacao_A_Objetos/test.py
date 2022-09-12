class Teste:
    def __init__(self, valor):
        self.x = valor

    '''Método gettter para retornar o valor do atributo x:'''
    def get_valor(self):
        return self.x

    '''Método setter para atribuir um novo valor ao atributo x:'''
    def set_valor(self, valor):
        self.x = valor


teste = Teste(10)
print(f'Valor do objeto: {teste.get_valor()}')

val = int(input('Digite um valor numererico: '))
print(f'O valor alterado é {teste.x}')
