# Faça um programa que ajude um jogador da MEGA SENA criar palpites
# Pergunte quantos jogos serão e serão sorteados 6 números
# Sendo eles de entre 1 e 60 para cada jogo
# Cadastrando em uma lista composta
from random import randint
from time import sleep

m = int(input("Quantidade de palpites: "))
new_game = list()
palpites = list()
for c in range(m):
    for i in range(0, 6):
        n = randint(1, 60)
        if n not in new_game:
            new_game.append(n)
        else:
            new_game.append(randint(1, 60))

    new_game.sort()
    palpites.append(new_game[:])
    new_game.clear()
for i, l in enumerate(palpites):
    print(f"Jogo {i + 1}: {l}")
    sleep(1)