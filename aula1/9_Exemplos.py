from math import sqrt, pow
from random import randint

n = int(input("n: ", ))

print()
print(f"Raiz quadrada = {sqrt(n):.4f}")
print(f"O cubo de {n} = {pow(n, 3)}")

print()
a = []
for i in range(10):
    a.append(randint(1, 100))

print(a)
