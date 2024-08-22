''' Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
2 para hexadecimal
'''

n = int(input("Insira um número: "))
print("-=-"*30)
b = int(input('''

    [ 0 ] Binário
    [ 1 ] Octal
    [ 2 ] Hexadecimal
    
Escolha a base de conversão: '''))
print("-=-"*30)

while b not in (0, 1, 2):
    print("Opção errada tente novamente.")
    b = int(input('''

        [ 0 ] Binário
        [ 1 ] Octal
        [ 2 ] Hexadecimal

    Escolha a base de conversão: '''))
if b == 0:
    print(f"O número {n} em binário fica {bin(n)[2:]}")
if b == 1:
    print(f"O número {n} em octal fica {oct(n)[2:]}")
else:
    print(f"O número {n} em hexadecimal fica {hex(n)[2:]}")
