s = input("")
resultado = ""

for caractere in s:
    if caractere == "0":
        resultado += "1"
    else:
        resultado += caractere

print(f"{resultado}")