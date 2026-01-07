def multiplo(x1, x2):
    multiplo = []
    for n in x1:
        if n % x2 == 0:
            multiplo.append(n)

    return multiplo

x1 = []
for i in range(10):
    x1.append(int(input("")))
x2 = int(input(""))
y = multiplo(x1, x2)
print(y)