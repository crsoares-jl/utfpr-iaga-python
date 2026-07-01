def matriz_String(s):
    n = len(s)
    for i in range(n):
        for j in range(i + 1):
            print(s[j], end=" ")
        print()

def matriz_String(s):
    n = len(s)
    for i in range(n):
        for j in range(i + 1):
            print(s[i], end=" ")
        print()

# módulo principal

s = input("Informe uma string:\n")

print()
matriz_String(s)

