resposta = 0
print("1: Média entre os números digitados")
print("2: Diferença do maior pelo menor")
print("3: Produto entre os números digitados")
print("4: Divisão do primeiro pelo segundo")
n1 = float(input(""))
n2 = float(input(""))
n3 = int(input(""))


if n3==1:
    resposta = (n1+n2)/2
    print(f"{resposta:.2f}")
elif n3==2:
    if n1 > n2:
        resposta=n1-n2
        print(f"{resposta:.2f}")
    else:
        resposta=n2-n1
        print(f"{resposta:.2f}")
elif n3==3:
    resposta = n1*n2
    print(f"{resposta:.2f}")
elif n3==4:
    if n2 != 0:
        resposta=n1/n2
        print(f"{resposta:.2f}")
    else:
        print("Erro")
else:
    print("Erro")