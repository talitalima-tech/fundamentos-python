def numero_maior(x1, x2):
    if x1 >= x2:
        return x1
    elif x2 > x1:
        return x2

x1 = float(input(""))
x2 = float(input(""))
y = numero_maior(x1, x2)
print(f"{y:.2f}")