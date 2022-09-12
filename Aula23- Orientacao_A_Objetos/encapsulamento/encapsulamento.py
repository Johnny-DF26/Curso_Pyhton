"""
public: São métodos e atributos que podem ser acessado dentro e fora da classe
protected: São métodos e atributos que podem ser acessado somente dentro da classe ou das filhas da classe
private: São métodos e atributos só esta disponivel dentro da classe
_ : protected(sutil)
__: private
Objetivo: Proteger sua aplicação
"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


base = BaseDeDados()
base.inserir_cliente(1, 'Otavio')
base.inserir_cliente(2,'Anna')
base.__dados = 'outra coisa'
print(base.__dados)
# base.lista_clientes()