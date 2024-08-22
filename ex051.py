''' Desenvolva um programa que leia o primeiro termo e a razão
de uma PA (Progressão Aritmética).
No final, mostre os 10 primeiros termos dessa progressão.'''
pt = int(input("Insira o primeiro termo: "))
r = int(input("Insira a razão da progressão aritimética: "))
dec = (pt + 10) * r
for i in range(pt, dec, r):
    print(f"{i}", end=",")
print("Fim")