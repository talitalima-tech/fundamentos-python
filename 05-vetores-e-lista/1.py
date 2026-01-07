def data_extenso(x):
    dia, mes, ano = x.split("/")
    dia = int(dia)
    mes = int(mes)
    mes_extenso = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro",
                   "novembro", "dezembro"]
    extenso = f"{dia} de {mes_extenso[mes - 1]} de {ano}"
    return extenso

x = input("")
y = data_extenso(x)
print(f"{y}")
