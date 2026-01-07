numero = []
for i in range(10):
    num = int(input())
    numero.append(num)
for j in range(len(numero)):
    n = numero[j]
    if n > 1:
        primo = True
        limite = int(n**0.5)+1
        for k in range(2, limite):
            if n%k == 0:
                primo = False
                break
        if primo:
            print(n)
            print(j)
    elif n<0:
        modulo = abs(n)
        if modulo >1:
            primo = True
            limite = int(modulo**0.5)+1
            for k in range(2, limite):
                if modulo % k == 0:
                    primo = False
                    break
            if primo:
                print(n)
                print(j)
