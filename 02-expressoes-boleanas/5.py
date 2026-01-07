def eh_triangulo(x1, x2, x3):
    if (x1 + x2 > x3) and (x1 + x3 > x2) and (x2 + x3 > x1):
        return True
    return False


def tipo_triangulo(x1, x2, x3):
    y = eh_triangulo(x1, x2, x3)
    if y == True:
        if (x1 == x2) and (x2 == x3):
            return "Triangulo equilatero"
        if (x1 != x2) and (x1 != x3) and (x2 != x3):
            return "Triangulo escaleno"
        else:
            return "Triangulo isosceles"
    else:
        return "Nao triangulo"


x1 = int(input(""))
x2 = int(input(""))
x3 = int(input(""))
t = tipo_triangulo(x1, x2, x3)
print(t)