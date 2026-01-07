numero = int(input())
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f'{milhar}')
print(f'{centena}')
print(f'{dezena}')
print(f'{unidade}')