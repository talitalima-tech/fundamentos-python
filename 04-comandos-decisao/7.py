salario= float(input(""))
prestaçao = float(input(""))

if prestaçao > salario * 0.20:
    print("Emprestimo nao concedido")
else:
    print("Emprestimo concedido")