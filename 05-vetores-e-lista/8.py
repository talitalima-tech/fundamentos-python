vetor = []
impares = []
soma = 0

for i in range(15):
    num = int(input())
    vetor.append(num)

for n in vetor:
    if n % 2 != 0:
        soma += n
        impares.append(n)
print(soma)

for i in impares:
    print(i)

