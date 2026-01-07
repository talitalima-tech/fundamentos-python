def área(largura, comprimento):
    a = largura * comprimento
    return a

def perímetro(largura, comprimento):
    p = (largura * 2) + (comprimento * 2)
    return p


# Programa principal
l = float(input("largura: "))
c = float(input('comprimento: '))
area = área(l, c)
perimetro = perímetro(l, c)
print(f'{area:.2f}')
print(f'{perimetro:.2f}')