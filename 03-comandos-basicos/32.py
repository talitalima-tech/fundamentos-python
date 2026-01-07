string = input("")
string_nova = ""
for letra in string:
    soma_ascii = ord(letra) + 1 #transforma para numero e soma
    string_nova += chr(soma_ascii) #transforma para texto
print(string_nova)