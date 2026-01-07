numero1 = float(input(""))
numero2 = float(input(""))
numero3 = float(input(""))
if numero1>numero2:
    if numero1>numero3:
        print(f"{numero1}")
    else:
        print(f"{numero3}")
else:
    if numero2>=numero3:
        print(f"{numero2}")
    else:
        print(f"{numero3}")
