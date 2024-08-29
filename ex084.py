# Faça um programa que leia nome e peso de pessoas
# Guarde tudo em uma lista e no final mostre
# Quantas pessoas foram cadastradas
# Lista dos mais pesados
# Lista do mais leves
galera = list()
pessoa = list()
pp = list()
pl = list()
pf = 0
while True:
    pessoa.append(input("Insira o nome: "))
    pessoa.append(float(input("Insira o peso: ")))
    galera.append(pessoa[:])
    pessoa.clear()
    opt = input("Para continuar digite [S] - Sim ou [N]: ").upper()
    while opt not in "SN":
        print("Digite apenas S ou N")
        opt = input("Para continuar digite [S] - Sim ou [N]: ").upper()
    if opt == "N":
        print("Programa encerrado!")
        break
    elif opt == "S":
        print("Continuado!")
        print("-=-"*30)
print(f"Foram cadastrados {len(galera)} pessoa(s)")
for c in galera:
    if c[1] > 80:
       pp.append(c)
    else:
        pl.append(c)
print("-=-"*30)
print("Pessoas acima do peso comum")
print("-=-"*30)
for i in pp:
    print(f"{i[0]} está com {i[1]} kg")
print("-=-" * 30)
print("Pessoas abaixo do peso comum")
print("-=-"*30)
for i in pl:
    print(f"{i[0]} está com {i[1]} kg")
