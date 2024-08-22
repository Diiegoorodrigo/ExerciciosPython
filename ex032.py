'''
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
'''
year = int(input("Informe o ano: "))
if year % 4 == 0:
    print("Esse ano é bissexto!")
else:
    print("Esse ano não é bissexto!")