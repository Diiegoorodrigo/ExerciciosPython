# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
cpu = randint(0, 5)
player = int(input("Adivinhe o número que o CPU está pensando entre 0 e 5: "))
if player == cpu:
    print("PARABENS VOCÊ ACERTOU!!")
else:
    print("VOCÊ ERROU, TENTE NOVAMENTE!!")
