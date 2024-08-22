# Faça um programa que leia três números e mostre qual é o maior e qual é o menor
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
menor = a
maior =a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
if c < a and c < b:
    menor = c
if b < a and b < c:
    menor = b
print(f"O número maior é {maior} e o menor é {menor}")
