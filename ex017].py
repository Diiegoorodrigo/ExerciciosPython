#Faça um programa que leia o cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

from math import hypot

co = float(input("Cateto oposto: "))
# co = math.pow(co, 2)  # co = 9
ca = float(input("Cateto adjacente: "))
# ca = math.pow(ca, 2)  # ca = 16

hipo = hypot(co, ca)

print(f"A hipotenusa de Cateto oposto: {co} e Cateto adjacente: {ca} é {hipo}")

