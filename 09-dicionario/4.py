from datetime import datetime


def informacao_aula(dia, mes, ano, hora, minuto, segundo, descricao):
    return {
        'data': {'dia': dia, 'mes': mes, 'ano': ano},
        'horario': {'hora': hora, 'minuto': minuto, 'segundo': segundo},
        'descricao': descricao
    }


dados = []

n = int(input())
for i in range(n):
    dia = int(input("Dia: "))
    mes = int(input("Mes: "))
    ano = int(input("Ano: "))
    hora = int(input("Hora: "))
    minuto = int(input("Minuto: "))
    segundo = int(input("Segundo: "))
    descricao = input("Descricao: ")

    compromisso = informacao_aula(dia, mes, ano, hora, minuto, segundo, descricao)
    dados.append(compromisso)

dados.sort(key=lambda c: (
    c['data']['ano'], c['data']['mes'], c['data']['dia'],
    c['horario']['hora'], c['horario']['minuto'], c['horario']['segundo']
))

for compromisso in dados:
    print(compromisso)
