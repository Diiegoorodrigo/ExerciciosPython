'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''
from random import randint
from time import sleep
cpu = randint(0, 2)
option = ("PEDRA", "PAPEL", "TESOURA")
player = int(input('''
    OPÇÕES
    
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA
    
    ESCOLHA SUA OPÇÃO: '''))

print("JO")
sleep(0.50)
print("KEN")
sleep(0.5)
print("PÔ!!!")

while player not in (0, 1, 2):
    print("ERRO, OPÇÃO INVALIDA TENTE NOVAMENTE!!!!")
    player = int(input('''
    OPÇÕES

    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA

    ESCOLHA SUA OPÇÃO: '''))

    print("JO")
    sleep(0.50)
    print("KEN")
    sleep(0.5)
    print("PÔ!!!")

if cpu == player:
    print(f"COMPUTADOR ESCOLHEU {option[cpu]} E JOGADOR ESCOLHEU {option[player]}")
    sleep(0.5)
    print("O JOGO EMPATOU.")

elif cpu == 0 and player == 1:
    print(f"COMPUTADOR ESCOLHEU {option[cpu]} E JOGADOR ESCOLHEU {option[player]}")
    sleep(0.5)
    print("PARABENS O JOGADOR GANHOU")
elif cpu == 0 and player == 2:
    print(f"COMPUTADOR ESCOLHEU {option[cpu]} E JOGADOR ESCOLHEU {option[player]}")
    sleep(0.5)
    print("O COMPUTADOR GANHOU!! TENTE NOVAMENTE.")


elif cpu == 1 and player == 2:
    print(f"COMPUTADOR ESCOLHEU {option[cpu]} E JOGADOR ESCOLHEU {option[player]}")
    sleep(0.5)
    print("PARABENS O JOGADOR GANHOU")
elif cpu == 1 and player == 0:
    print(f"COMPUTADOR ESCOLHEU {option[cpu]} E JOGADOR ESCOLHEU {option[player]}")
    sleep(0.5)
    print("O COMPUTADOR GANHOU!! TENTE NOVAMENTE.")

elif cpu == 2 and player == 0:
    print(f"COMPUTADOR ESCOLHEU {option[cpu]} E JOGADOR ESCOLHEU {option[player]}")
    sleep(0.5)
    print("PARABENS O JOGADOR GANHOU")
elif cpu == 2 and player == 1:
    print(f"COMPUTADOR ESCOLHEU {option[cpu]} E JOGADOR ESCOLHEU {option[player]}")
    sleep(0.5)
    print("O COMPUTADOR GANHOU!! TENTE NOVAMENTE.")
