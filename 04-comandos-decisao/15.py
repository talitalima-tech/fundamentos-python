numero = int(input())

soma = 0
for i in range(1, numero):
    if numero % i == 0:
        soma += i #i:divisor
print(soma)