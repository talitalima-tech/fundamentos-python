def MDC(x1, x2):
    # para limitar a busca encontra o menor
    menor = min(x1, x2)

    for i in range(1, menor + 1):
        # Se i divide ambos, logo é um divisor comum
        if x1 % i == 0 and x2 % i == 0:
            mdc = i

    return mdc

x1 = int(input(""))
x2 = int(input(""))
y = MDC(x1, x2)
print(f"{y}")