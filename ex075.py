# Desenvolva um programa que leia quatro valores no teclado e insira na tupla
# Mostre quantas vezes o 9 aparece
# mostre o indice do 3
# quais foram os números pares digitados.
n = (int(input('Insira um número: ')), int(input('Insira um número: ')), int(input('Insira um número: ')), int(input('Insira um número: ')))
print('='*30)
print(f'O número 9 foi digitado {n.count(9)} vez(es)')
if 3 in n:
  print(f'A posição que o 3 foi digitado é {n.index(3)}')
for i in n:
  if i % 2 == 0:
    print(i,'',end='')