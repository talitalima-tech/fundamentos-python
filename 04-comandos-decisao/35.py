def funcao(n):
    a = n // 100
    b = n % 100
    s = a + b
    return s * s == n


for n in range(1000, 10000):
    if funcao(n):
        print(n)