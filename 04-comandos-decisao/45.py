def codigo_cesar(x1, x2):
    resultado = ""
    for char in x1:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            novo_char = chr((ord(char) - base + x2) % 26 + base)
            resultado += novo_char
        else:
            resultado += char
    return resultado

x1 = input("")
x2 = int(input(""))
y = codigo_cesar(x1, x2)
print(f"{y}")