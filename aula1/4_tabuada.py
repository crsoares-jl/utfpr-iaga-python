def tabuada_I(n):
    i = 1
    while (i <= 10):
        print(f"{n} x {i} = {n * i}")
        i = i + 1

    print()

    
def tabuada_II(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


# módulo principal

n = int(input("n: "))

tabuada_I(n)
tabuada_II(n)