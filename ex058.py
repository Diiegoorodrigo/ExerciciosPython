''' Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer
'''
from random import randint
from time import sleep
cpu = randint(0, 10)
count = 0
player = int(input("Insira um número de 0 a 10 para tentar adivinhar o número que a CPU pensou: "))
while player != cpu:
    count += 1
    if player < 0 or player > 10:
        print("Opção inválida, digite outro número!")
        player = int(input("Insira um número de 0 a 10 para tentar adivinhar o número que a CPU pensou: "))
    else:
        print("Número errado, tente novamente!")
        player = int(input("Insira um número de 0 a 10 para tentar adivinhar o número que a CPU pensou: "))

print(f"Parabens você acertou o número é {cpu} e você acertou em {count+1} tentaviva(s)")
