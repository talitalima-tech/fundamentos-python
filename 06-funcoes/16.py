def conversão_tempo(numero):
    horas = numero // 3600
    resto = numero % 3600
    minutos = resto // 60
    segundos = resto % 60
    return horas, minutos, segundos


# Programa principal
tempo = int(input('tempo: '))
horas, minutos, segundos = conversão_tempo(tempo)
print(f'{horas}:{minutos}:{segundos}')
