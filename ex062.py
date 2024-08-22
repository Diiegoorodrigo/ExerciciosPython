# Crie um programa que leia o primeiro termo  e a razão de uma PA
# Mostre apenas os 10 primeiros termos
r = int(input('Informe a razão da PA: '))
pt = int(input('Informe o primeiro termo da PA: '))
c = 0
pa = [pt]
while c < 9:
  pt += r
  pa.append(pt)
  c += 1
print(pa)
m = str(input('DESEJA VER MAIS TERMOS? [S/N]: ')).upper()
while m not in 'SsNn':
  print('OPÇÃO INCORRETA!')
  m = str(input('DESEJA VER MAIS TERMOS? [S/N]: ')).upper()
if m == 'N':
  print('PROGRAMA ENCERRADO')
while m == 'S':
  x = int(input('Informe quantos termos deseja ver: '))
  c = 0
  while c < x:
    pt += r
    pa.append(pt)
    c += 1
  print(pa)
  m = str(input('DESEJA VER MAIS TERMOS? [S/N]: ')).upper()
  while m not in 'SsNn':
    print('OPÇÃO INCORRETA!')
    m = str(input('DESEJA VER MAIS TERMOS? [S/N]: ')).upper()
  if m == 'N':
    print('PROGRAMA ENCERRADO')