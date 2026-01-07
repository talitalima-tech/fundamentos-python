def eh_perfeito(x):
    soma = 0
    d = None
    for i in range(1, x):
        if x % i == 0:
            soma += i
    if soma == x:
        return True
    else:
        return False


x = int(input(""))
y = eh_perfeito(x)
if y == True:
    print("perfeito")
else:
    print("Nao perfeito")