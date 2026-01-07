def fatorial(x):
    fatorial = 1
    for i in range(1, x + 1):
        fatorial *= i
    return fatorial

# Programa Principal
x = int(input(""))
fatorial = fatorial(x)
print(f"{fatorial}")