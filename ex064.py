# Crie um programa que leia varios números inteiros e se digitar 999 saiará
# mostre a soma dos números digitados e quantos números foram digitados
n = int(input('Digite um valor: '))
s = 0
qtn = 0
while n != 999:
  s += n
  qtn += 1
  n = int(input('Digite um valor: '))
print('A soma de todos os números é {}'.format(s))
print('Quantidade de números digitados {}'.format(qtn))