import random

semente = float(input())
random.seed(semente)
numeros = [random.uniform(-10, 10) for _ in range(12)]

cont_negativo = 0
soma = 0
for n in numeros:
    if n < 0:
        cont_negativo += 1
    else:
        soma += n

print(cont_negativo)
print(f"{soma:.2f}")