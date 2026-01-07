def vogais(s):
    vogais = 'aeiouAEIOU'
    resultado = ''
    for c in s:
        if c != 'a' and c != 'e' and c != 'i' and c != 'o' and c != 'u' and \
           c != 'A' and c != 'E' and c != 'I' and c != 'O' and c != 'U':
            resultado += c
    return resultado

s = input("")
resultado = vogais(s)
print(resultado)