s = input("")
x = len(s)
c = len(s) - 1
invetida = ""
while True:
    if c < 0:
        break

    if s[c].lower() == "a":
        invetida += "*"
    else:
        invetida += s[c]

    c -= 1

print(invetida)

