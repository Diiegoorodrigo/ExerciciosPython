# Crie um programa que insira 5 números aleatórios na tupla
# mostre o maior número e o menor
from random import randint
n = (randint(1,200), randint(1,100), randint(1,100), randint(1,100), randint(1,100))
nMn = nMr =0

for c in n:
  if nMn == 0:
    nMn = c
  if c < nMn:
    nMn = c
  elif c > nMr:
    nMr = c
print(f'A tupla contem os números {n}')
print(f'O maior número é {nMr}')
print(f'O menor número é {nMn}')