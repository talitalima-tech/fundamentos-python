import math
def media_desvio_padrao_qtd_aluno(x):
    soma = 0
    diferenca = 0
    quadrado = 0
    cont = 0
    for n in x:
        soma += n
    media = soma / len(x)
    for n in x:
        diferenca = n - media
        quadrado += diferenca ** 2
        dp = math.sqrt(quadrado / len(x))
    for n in x:
        if n < 7:
            cont += 1

    return media, dp, cont


x = []
for i in range(15):
    x.append(float(input("")))
y1, y2, y3 = media_desvio_padrao_qtd_aluno(x)
print(f"{y1:.2f}")
print(f"{y2:.2f}")
print(f"{y3}")