numero = int(input())
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
novo = unidade * 100 + dezena * 10 + centena * 1
print(novo)