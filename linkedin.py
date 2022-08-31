# from datetime import datetime
#
#
# def formataDataHora():
#     hoje = datetime.now()
#     print(hoje.strftime("O ano é: %y"))
#     print(hoje.strftime('Data e hora local: %c'))
#     print(hoje.strftime("A hora atual é: %I:%M:%S %p"))
#
# formataDataHora()

# print('-------------------------------------- USANDO TIME --------------------------------------------')
# import datetime
#
#
# def deltaTempo():
#     delta = datetime.timedelta(days=86, hours=8532, minutes=7645)
#     print(delta)
#
#     hoje = datetime.datetime.now()
#     print(f'Data no futuro: {hoje + delta}')
#     print(f'Data do passado: {hoje - delta}')
#
#
# deltaTempo()

# print('---------------------------------  MANIPULAÇÃO DE DATAS   --------------------------------')
# from datetime import datetime
#
#
# def quantosDiasFaltam(ano, mes, dia):
#     hoje = datetime.today()
#     dataProcurada = datetime.date(ano, mes, dia)
#     qtdDias = dataProcurada - hoje
#     msgRetorno = "Faltam" + str(qtdDias) + "dias para a data" + dataProcurada.strftime('%d%m%y')
#     print(msgRetorno)
#
#
# quantosDiasFaltam(2019,10,15)

print('-----------------------------------  CALENDÁRIO    ---------------------------------------')
import calendar

calendarioHTML = calendar.HTMLCalendar(calendar.MONDAY)
htmlCalendario = calendarioHTML.formatmonth(2020, 6)
print(htmlCalendario)

