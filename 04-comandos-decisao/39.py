def comparar_palavras(palavra1, palavra2):
    comprimento_minimo = min(len(palavra1), len(palavra2))

    for i in range(comprimento_minimo):
        if palavra1[i] < palavra2[i]:
            return f"{palavra1}"
        elif palavra1[i] > palavra2[i]:
            return f"{palavra2}"

    if len(palavra1) < len(palavra2):
        return f"{palavra1}"
    elif len(palavra1) > len(palavra2):
        return f"{palavra2}"
    else:
        return palavra1


palavra1 = input("")
palavra2 = input("")
resultado = comparar_palavras(palavra1, palavra2)
print(resultado)
