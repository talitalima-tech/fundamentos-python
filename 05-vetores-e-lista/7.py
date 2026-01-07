vetor = []
cont = 0
for i in range(15):
    num = int(input())
    vetor.append(num)

for n in vetor:
    if n % 2 == 0:
        cont += 1
print(cont)
for n in vetor:
    if n % 2 == 0:
        print(n)
