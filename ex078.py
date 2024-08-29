# Faça um programa que leia 5 valores e os guarde em uma lista
# No final mostre o maior e o menor
num = []
mr = 0
mn = 100000000000
for c in range(0,5):
  c = int(input("Insira um número: "))
  if c > mr:
    mr = c
  elif c < mn:
   mn = c
  num.append(c)
print(f"O maior número da lista é {mr} e o menor é {mn}")
print(f"A lista completa é {num}")