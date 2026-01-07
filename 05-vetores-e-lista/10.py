vetor = []
negativo = 0

for i in range(20):
    num = int(input())
    vetor.append(num)

for n in vetor:
    if n >= 0:
        print(n)
    else:
        print(negativo)