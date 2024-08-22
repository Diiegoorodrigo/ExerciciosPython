# Crie um programa que leia varios números
# pergunte se ele deseja inserir mais números
# De a média dos números digitados, o maior e o menor.
n = int(input('Informe um número: '))
m = 1
soma = n
mr = n
mn = n
s = str(input('Quer continuar? [S/N]: ')).upper()
while s not in 'NnSs':
    print('Opção errada! Digite novamente.')
    s = str(input('Quer continuar? [S/N]: ')).upper()
if s == 'N':
    print('PROGRAMA ENCERRADO!!')
    print('Maior número {}'.format(mr))
    print('Menor número {}'.format(mn))

while s == 'S':
    n = int(input('Digite um número: '))
    soma += n
    if n > mr:
        mr = n
    elif n < mn:
        mn = n
    m += 1

    s = str(input('Quer continuar? [S/N]: ')).upper()
    while s not in 'NnSs':
        print('Opção errada! Digite novamente.')
        s = str(input('Quer continuar? [S/N]: ')).upper()
    if s == 'N':
        print('-=-' * 10)
        print('PROGRAMA ENCERRADO!!')
        print('-=-' * 10)
        print('Maior número {}'.format(mr))
        print('-=-' * 10)
        print('Menor número {}'.format(mn))
        print('-=-' * 10)
        print('Media dos números digitados {:.2f}'.format(soma / m))
