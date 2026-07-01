from random import randint
from statistics import mean

jogo = []

i = 1
while (i <= 6):
    nr = randint(1, 60)
    if (nr not in jogo):
        jogo.append(nr)
        i = i + 1

print(jogo)
jogo.sort()
print(jogo)

print(mean(jogo)) # média dos 6 números

# obtendo ascii

for i in range(48, 84):
    print(i, chr(i))

print('9' < 'A' < 'a')
