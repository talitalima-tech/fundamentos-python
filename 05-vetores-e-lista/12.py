import math
def media_desvio_padrao(x):
    soma=0
    diferenca=0
    quadrado=0
    for n in x:
        soma += n
    media = soma/len(x)
    for n in x:
        diferenca = n - media
        quadrado += diferenca**2
        dp = math.sqrt(quadrado/len(x))
    return media, dp


x = []
for i in range(15):
    x.append(float(input("")))
y1, y2 = media_desvio_padrao(x)
print(f"{y1:.2f}")
print(f"{y2:.2f}")
