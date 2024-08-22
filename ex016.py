# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import trunc
n = float(input("Insira um número quebrado: "))
print(f"{(trunc(n))}")
print(f"{int(n)}")