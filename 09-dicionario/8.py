import math
def polar_para_cartesiano(r, a):
    x = r * math.cos(a)
    y = r * math.sin(a)
    cartesiano = {
        'x': x,
        'y': y
    }

    return cartesiano

r = float(input())
a= float(input())
polar = {
    'r': r,
    'a': a
}
c = polar_para_cartesiano(r, a)
print(polar)
print(c)