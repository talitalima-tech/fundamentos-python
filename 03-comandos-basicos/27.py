def fatorial_exponencial(n):
    resposta= 1
    modulo = (int)(1000000007)
    for i in range(2, n + 1):
        resposta = pow(i, resposta, modulo)
    return resposta
n= int(input())
y= fatorial_exponencial(n)
print(y)