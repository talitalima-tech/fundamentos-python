def maior_fator_primo(x):
    if x == 1:
        y = 1

    while x % 2 == 0:
        y = 2
        x //= 2

    fator = 3
    while fator * fator <= x:
        while x % fator == 0:
            y = fator
            x //= fator
        fator += 2

    if x > 1:
        y = x

    return y

x = int(input(""))
y = maior_fator_primo(x)
print(f"{y}")