vetor = []

for i in range(8):
    num = float(input())
    vetor.append(num)

x = int(input())
y = int(input())

posicao1 = vetor[x]
posicao2 = vetor[y]
soma = posicao1 + posicao2
print(f"{soma:.2f}")