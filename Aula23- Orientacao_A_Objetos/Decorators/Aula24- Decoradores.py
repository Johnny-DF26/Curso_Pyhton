import requests
import time

# decorator calcular tempo
def calcular_tempo(funcao):
    def wrapper():
        tempo_inic = time.time()
        funcao()
        temp_final = time.time()
        print(f'Duração foi de {temp_final - tempo_inic:.2f} segundos')
    return wrapper


@calcular_tempo
def pegar_dolar():
    link = f'https://economia.awesomeapi.com.br/last/USD-BRL'
    requisicao = requests.get(link)
    requisicao = requisicao.json()
    print(requisicao['USDBRL']['bid'])

pegar_dolar()