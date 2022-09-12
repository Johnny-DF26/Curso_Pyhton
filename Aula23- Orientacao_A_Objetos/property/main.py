class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, perc):
        self.preco = self.preco - (self.preco * (perc / 100))

    def aumento(self, perc):
        self.preco = self.preco + (self.preco * (perc / 100))

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, value):
        if isinstance(value, str):
            value = float(value.replace('R$',''))
        self._preco = value


produto1 = Produto('calca', '10')
produto1.desconto(10)
print(produto1.preco)

produto2 = Produto('caneca', 10)
produto2.aumento(5)
print(produto2.preco)
