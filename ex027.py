# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
name = input("Digite seu nome: ").strip().split()
print(f"O primeiro nome é {name[0]} e o último nome é {name[len(name)-1]}")
