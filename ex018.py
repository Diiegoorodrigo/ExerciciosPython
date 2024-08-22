# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
ang = float(input("Informe um ângulo entre 0º e 360º: "))
print(f"O ângulo de {ang} tem o seno de {sin(ang):.2f}.")
print(f"O ângulo de {ang} tem o cosseno de {cos(ang):.2f}.")
print(f"O ângulo de {ang} tem a tangente de {tan(ang):.2f}.")
