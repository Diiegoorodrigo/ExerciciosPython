# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "Santo"
nome = input("Digite seu nome: ").strip().upper().split()
if nome[0] == "SANTO":
    print("O nome começa com Santo")
else:
   print("O nome não começa com Santo")