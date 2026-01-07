def limpar_string(s):
    resultado = ''
    for c in s:
        if c.isalnum():
            resultado += c.lower()
    return resultado

def eh_palindromo(x):
    x = limpar_string(x)
    x1 = x[::-1]  # Inverte a string
    if x == x1:  
        return True
    return False


x = input("")
y = eh_palindromo(x)
print(y)
