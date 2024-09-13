"""
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista.

No final, mostre:
a. Quantas pessoas foram cadastradas
b. A média de idade do grupo
c. uma lista com todas as mulheres
d. uma lista com todas as pessoas com idade acima da média.
"""

people = dict()
p_people = list()
p_mulher = list()
media = total = 0
acima = list()

while True:
    people['nome'] = input("Insira o nome: ")
    people['sexo'] = input("Insira o sexo [ M ] - Masculino / [ F ] - Feminino: ").upper()
    while people['sexo'] not in "MF":
        print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE")
        people['sexo'] = input("Insira o sexo [ M ] - Masculino / [ F ] - Feminino: ").upper()[0]
    if people['sexo'] in "fF":
        p_mulher.append(people.copy())
    people['idade'] = int(input("Insira a idade: "))
    media += people['idade']
    total += 1
    if people['idade'] > media / total:
        acima.append(p_people.copy())
    p_people.append(people.copy())
    s = int(input("Digite 1 - Para continuar / 999 - Para sair"))
    if s == 999:
        break
print("=-="*30)
print(total)
print(media/total)
print(p_mulher)
print(acima)
