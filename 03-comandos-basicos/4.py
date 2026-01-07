soma = 0
media = 0
for _ in range(10):
    n = int(input('Digite um numero: '))
    soma += n
    media = soma / 10
print(f'{media:.2f}')