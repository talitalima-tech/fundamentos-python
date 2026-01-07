def media_aluno(x1, x2, x3, x4):
    if x4 == "A":
        media = (x1 + x2 + x3) / 3
    elif x4 == "P":
        media = ((5 * x1) + (3 * x2) + (2 * x3)) / 10

    return media

x1 = float(input(""))
x2 = float(input(""))
x3 = float(input(""))
x4 = input("")
y = media_aluno(x1, x2, x3, x4)
print(f"{y:.2f}")