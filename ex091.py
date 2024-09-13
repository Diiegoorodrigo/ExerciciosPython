# Crie um programa onde 4 jogadores joguem um dado
# e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário.

  # No final, coloque esse dicionário em ordem,
  # sabendo que o vencedor tirou o maior número no dado
from random import randint
from time import sleep

player = {'Jogador1': randint(1, 6),
              'Jogador2': randint(1, 6),
              'Jogador3': randint(1, 6),
              'Jogador4': randint(1, 6),}

ranking = list()
ranking = sorted(
    list(zip(player.values(), player.keys())), reverse=True)
for i, v in enumerate(ranking):
    print(f"{i+1}º lugar para {v[1]} tirou {v[0]} ")
    sleep(1)