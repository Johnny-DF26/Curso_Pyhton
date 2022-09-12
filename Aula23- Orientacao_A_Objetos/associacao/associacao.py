from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Joao')
caneta = Caneta('BIC')
maquina = MaquinaDeEscrever()
escritor.ferramenta = maquina
escritor.ferramenta.escrever()