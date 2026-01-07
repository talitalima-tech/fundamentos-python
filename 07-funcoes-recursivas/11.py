def mdc(x1, x2):
    if x2 == 0:
        return x1
    else:
        return mdc(x2, x1 % x2)


x1 = int(input(""))
x2 = int(input(""))
y = mdc(x1, x2)
print(f"{y}")