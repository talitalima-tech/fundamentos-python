import math
def quociente_divisao(x1, x2):
    if x1 > x2:
        divisao = x1 * x2 ** (-1)
        divisao2 = math.floor(divisao)
        return divisao2
    else:
        divisao = x2 * x1 ** (-1)
        divisao2 = math.floor(divisao)
        return divisao2


x1 = int(input(""))
x2 = int(input(""))
y = quociente_divisao(x1, x2)
print(y)