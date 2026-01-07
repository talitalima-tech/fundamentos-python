def soma(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s
def soma_fatorial(n):
    y = 1
    for i in range(n, 0, -1):
        y *= i
    return soma(y)

n = int(input())
y = soma_fatorial(n)
print(y)

