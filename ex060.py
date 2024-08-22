# Faça um programa que leia um número qualquer e mostre seu fatorial
n = int(input('Informe o número a ser fatorado: '))
c = 1
n2 = n
while c < n:
  n2 = n2*(n-c)
  c += 1
print('O {} fatorado resulta em {}'.format(n, n2))