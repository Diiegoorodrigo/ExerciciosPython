# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
nome = input("Digite seu nome: ").upper().strip()
if "SILVA" in nome:
    print("Ele tem Silva no nome")
else:
    print("Ele não tem Silva no nome")
