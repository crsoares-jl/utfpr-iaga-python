def matriz_I(n):
    i = 0
    while (i < n):
        j = 0
        while (j < n):
            print(f"{i}{j}", end=" ")
            j = j + 1
        print()
        i = i + 1
    print()

def matriz_II(n):
    for i in range(n):
        for j in range(n):
            print(f"{i}{j}", end=" ")
        print()

# módulo principal
n = int(input("Tamanho da matriz?" ))

print()
matriz_I(n)
matriz_II(n)