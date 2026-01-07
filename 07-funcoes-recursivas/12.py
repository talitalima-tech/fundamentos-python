def h(x1, x2):
    if x2 == 1:
        return x1 + 1
    if x1 == 1:
        return x2 + 1
    if x1 > 1 and x2 > 1:
        return h(x1, x2 - 1) + h(x1 - 1, x2)


x1 = int(input(""))
x2 = int(input(""))
y = h(x1, x2)
print(f"{y}")