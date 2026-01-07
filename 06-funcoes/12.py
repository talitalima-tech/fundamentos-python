def aumento_salário(salario):
    novo = salario + (salario * 21.37/100)
    return novo


# Programa principal
salario = float(input('Salário: '))
novo = aumento_salário(salario)
print(f'{novo:.2f}')
