#S = 1/1 + 3/2 + 5/3 + 7/4 + … + 99/50
soma = 0
denominador = 1
for numerador in range(1, 100, 2):
    soma += numerador / denominador
    denominador += 1
print(f'{soma:.10f}')


