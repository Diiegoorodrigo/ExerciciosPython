''' Desenvolva um programa que leia nome, idade e sexo de 4 pessoas
No final do programa, mostre:
 - A média de idade do grupo
 - Qual é o nome do homem mais velho
 - Quantas mulheres têm menos de 20 anos
 '''
manOld = 0
woman_count = 0
man = []
age = 0
count = 0
for i in range (0,4):
    name = input("Insira o nome: ")
    idade = int(input("Insira a idade: "))
    sex = input("Insira o sexo: ").upper()
    while sex not in ("M","F"):
        print("SEXO INVALIDO, TENTE NOVAMENTE!")
        sex = input("Insira o sexo: ").upper()
    print("-=-"*30)
    age += idade
    count += 1
    if sex == "M" and idade > manOld:
        manOld = idade
        man = name
    elif sex == "F" and idade < 20:
        woman_count += 1
print(f"O homem mais velho é o {man} com {manOld} anos.")
print(f"O grupo contem {woman_count} mulher(es) com menos de 20 anos")
print(f"A média de idade do grupo é {age/count} anos")




