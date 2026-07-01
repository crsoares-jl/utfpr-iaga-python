a = int(input())
b = int(input())
c = int(input())

if ((a <= b) and (b <= c)):
    print(f"meio = {b}")
elif ((c <= b) and (b <= a)):
    print(f"meio = {b}")
elif ((b <= a) and (a <= c)):
    print(f"meio = {a}")
elif ((c <= a) and (a <= b)):
    print(f"meio = {a}")
elif ((a <= c) and (c <= b)):
    print(f"meio = {c}")
else:
    print(f"meio = {c}")


a=7
b=9
c=-1
numeros=[a,b,c]
numeros=sorted(numeros)
print(f'1º: {numeros[0]}')
print(f'Meio: {numeros[1]}')
print(f'3º: {numeros[2]}')
