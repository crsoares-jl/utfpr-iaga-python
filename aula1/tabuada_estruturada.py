def tabuada(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

# módulo principal (main)
tabuada(5)
tabuada(7)
tabuada(9)

for i in range(1, 11):
    tabuada(i)
