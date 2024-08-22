''' Crie um programa que leia dois valores e mostre um menu
na tela:

1: somar
2: multiplicar
3: maior
4: novos números
5: sair do programa

Seu programa deverá realizar a operação solicitada em cada caso '''

n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))
print(''' -=-=- MENU -=-=-
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
''')
m = int(input('Escolha uma opção: '))
print('-=-'*10)
while m != 5:
  if m == 1:
    print('A soma de {} e {} resulta em {}'.format(n1, n2, n1+n2))
    print('-=-'*10)
    print(''' -=-=- MENU -=-=-
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    ''')
    m = int(input('Escolha uma opção: '))
  elif m == 2:
    print('O resultado da multiplicação de {} e {} é {}'.format(n1, n2, n1*n2))
    print('-=-'*10)
    print(''' -=-=- MENU -=-=-
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    ''')
    m = int(input('Escolha uma opção: '))
  elif m == 3:
    if n1 > n2:
      print('{} é maior que {}'.format(n1, n2))
      print('-=-'*10)
      print(''' -=-=- MENU -=-=-
      [1] Somar
      [2] Multiplicar
      [3] Maior
      [4] Novos números
      [5] Sair do programa
      ''')
      m = int(input('Escolha uma opção: '))
    elif n1 == n2:
      print('Os números são iguais.')
      print('-=-'*10)
      print(''' -=-=- MENU -=-=-
      [1] Somar
      [2] Multiplicar
      [3] Maior
      [4] Novos números
      [5] Sair do programa
      ''')
      m = int(input('Escolha uma opção: '))
    else:
      print('{} é maior que {}'.format(n2, n1))
      print('-=-'*10)
      print(''' -=-=- MENU -=-=-
      [1] Somar
      [2] Multiplicar
      [3] Maior
      [4] Novos números
      [5] Sair do programa
      ''')
      m = int(input('Escolha uma opção: '))
  elif m == 4:
    n1 = int(input('Informe um número: '))
    n2 = int(input('Informe outro número: '))
    print(''' -=-=- MENU -=-=-
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    ''')
    m = int(input('Escolha uma opção: '))
    print('-=-'*10)
print('Programa encerrado!!!')