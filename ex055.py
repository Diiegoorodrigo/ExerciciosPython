''' Faça um programa que leia o peso de cinco pessoas
No final, mostre qual foi o maior e o menor peso lidos'''
large = 0
small = 1000
for i in range(0, 5):
    p = float(input("Informe o peso: "))
    if p > large:
        large = p
    elif p < small:
        small = p
print(f"O maior peso é {large:.2f} quilos e o menor peso é {small:.2f} quilos")