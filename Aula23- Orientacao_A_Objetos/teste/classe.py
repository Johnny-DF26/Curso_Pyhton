class Conta:
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo Insuficiente')
            return

        self.saldo -= valor
        print(f'Saldo Atual: R${self.saldo}')

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.ver_saldo()

    def ver_saldo(self):
        print('__' * 20)
        print(f'Agencia: {self.agencia}\nConta: {self.conta}\nSaldo: R${self.saldo}')
        print('__' * 20)

    def cabecalho(self,txt):
        print('__' * 20)
        print(f'\033[35m{txt}\033[m'.center(45))
        print('__' * 20)
