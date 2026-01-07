def soma(z, w):
    return {
        'real': z['real'] + w['real'],
        'imaginario': z['imaginario'] + w['imaginario']
    }


def subtracao(z, w):
    return {
        'real': z['real'] - w['real'],
        'imaginario': z['imaginario'] - w['imaginario']
    }


def produto(z, w):
    return {
        'real': z['real'] * w['real'] - z['imaginario'] * w['imaginario'],
        'imaginario': z['real'] * w['imaginario'] + z['imaginario'] * w['real']
    }


def modulo(z):
    return (z['real'] ** 2 + z['imaginario'] ** 2) ** 0.5


real_z = float(input())
imaginaria_z = float(input())
real_w = float(input())
imaginaria_w = float(input())

z = {
    'real': real_z,
    'imaginario': imaginaria_z
}

w = {
    'real': real_w,
    'imaginario': imaginaria_w
}

soma_total = soma(z, w)
subtracao_total = subtracao(z, w)
produto_total = produto(z, w)
modulo_z = modulo(z)
modulo_w = modulo(w)

print(f"{soma_total}")
print(f"{subtracao_total}")
print(f"{produto_total}")
print(f"{modulo_z:.2f}")
print(f"{modulo_w:.2f}")


