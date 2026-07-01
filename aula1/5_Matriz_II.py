def matriz_I(nl, nc):
    i = 0
    while (i < nl):
        j = 0
        while (j < nc):
            print(f"{i}{j}", end=" ")
            j = j + 1
        print()
        i = i + 1
    print()

def matriz_II(nl, nc):
    for i in range(nl):
        for j in range(nc):
            print(f"{i}{j}", end=" ")
        print()

# módulo principal
nl = int(input("Quantas linhas na matriz?" ))
nc = int(input("Quantas colunas na matriz?" ))

print()
matriz_I(nl, nc)
print()
matriz_II(nl, nc)
print()