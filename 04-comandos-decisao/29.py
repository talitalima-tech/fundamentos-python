def eh_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0:
            return False
        if n % (i + 2) == 0:
            return False
        i += 6

    return True


n = int(input(""))
y = eh_primo(n)
if y == True:
    print("Primo")
else:
    print("Nao primo")