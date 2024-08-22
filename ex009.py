# Faça um programa que leia um número inteiro qualquer
# e mostre na tela a sua tabuada
c = int(input("Insira um número: "))

for n in range(0, 11):
    print(f"{c} x {n} = {n*c}")
