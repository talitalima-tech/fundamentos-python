# conversão de dólar para real
def conversão(num):
    real = num * 5.27
    return real


# Programa principal
dolar = float(input("numero: "))
dolar = conversão(dolar)
print(f'{dolar:.2f}')