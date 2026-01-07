numero = []

for i in range(100):
    num = float(input())
    numero.append(num)
while True:
    n = int(input())
    if n == 0:
        break
    if n == 1:
        for j in numero:
            print(j)
    if n == 2:
        inverso = numero[::-1]
        for j in inverso:
            print(j)
    if (n != 1) and (n != 2):
        print("Codigo invalido")
