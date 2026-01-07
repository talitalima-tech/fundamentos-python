def string_iguais(string1, string2):
    if string1 == string2:
        return True
    return False

string1 = input("")
string2 = input("")
y = string_iguais(string1, string2)
print(f"{y}")