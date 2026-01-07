nota1= float(input(""))
if 0<=nota1<= 10:
    nota2= float(input(""))
    if 0<=nota2<=10:
        nota3= float(input(""))
        if 0<=nota3<=10:
            media= (n1+n2+n3)/3
            print(f"{media:.2f}")
        else:
            print("Nota invalida")
    else:
        print("Nota invalida")
else:
    print("Nota invalida")