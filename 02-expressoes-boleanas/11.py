def separar_data(x):
    dia = mes = ano = 0

    if len(x) != 10:
        return dia, mes, ano

    if x[2] != '/' or x[5] != '/':
        return dia, mes, ano

    dia_str = x[0:2]
    mes_str = x[3:5]
    ano_str = x[6:10]

    if (dia_str.isdigit() and mes_str.isdigit() and ano_str.isdigit() and
            len(dia_str) == 2 and len(mes_str) == 2 and len(ano_str) == 4):

        dia = int(dia_str)
        mes = int(mes_str)
        ano = int(ano_str)

    else:
        return 0, 0, 0

    return dia, mes, ano

x = input("")
y1, y2, y3 = separar_data(x)
print(f"{y1}")
print(f"{y2}")
print(f"{y3}")
