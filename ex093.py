''' Crie um programa que gerencie o aproveitamento de um jogador de futebol
o programa irá ler o nome, partidas jogadas
Depois a quantidade de gols feito em cada partida
no final turo isso será guardado em um dicionario
incluindo o total de gols'''
jogador = dict()
partidas = list()
jogador['nome'] = input('Insira o nome do jogador: ')
tot = int(input('Insira a quantidade de jogos: '))
print('-=-'*20)
for i in range(tot):
  partidas.append(int(input('Insira a quantidade de gols: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(jogador['gols'])
print('-=-'*20)
print(f'O jogador {jogador["nome"]} jogou {len(partidas)} partidas(s)')
print('-=-'*20)
for i, v in enumerate(jogador['gols']):
  print(f'Na partida {i+1}, {jogador["nome"]} fez {v} gol(s)')
print(f'{jogador["nome"]} fez o total de {jogador["total"]} gol(s)')