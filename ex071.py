# Crie um programa que simule m caixa eletrônico.
# Pergunte ao usuário o valor sacado
# O programa irá informar a quantidade de cédulas de cada valor
# Considere cedulas de 50, 20, 10 e 1
print('-=-'*30)
print('          BANCO TESTE')
print('-=-'*30)
c1 = 0
c2 = 0
c3 = 0
c4 = 0
while True:
  valor = int(input('Informe o valor para saque: '))
  while valor >= 50:
    valor -= 50
    c1 += 1
  while valor >= 20:
    valor -= 20
    c2 += 1
  while valor >= 10:
    valor -= 10
    c3 += 1
  while valor >= 1:
    valor -= 1
    c4 += 1
  if valor == 0:
    break

if c1 > 0:
  print(f'Total de {c1} cédulas de R$50')
if c2 > 0:
  print(f'Total de {c2} cédulas de R$20')
if c3 > 0:
  print(f'Total de {c3} cédulas de R$10')
if c4 > 0:
  print(f'Total de {c4} cédulas de R$1')
print('==='*20)
print('VOLTE SEMPRE AO BANCO TESTE! Tenha um bom dia!')