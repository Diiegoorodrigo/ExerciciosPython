# Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela
students = dict()
students["name"] = input("Insira o nome: ")
n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Insira a segunda nota: "))
students["avgr"] = (n1 + n2) / 2
if students["avgr"] > 6:
  print(f"O aluno {students['name']} tem a média {students['avgr']} e está aprovado")
else:
  print(f"O aluno {students['name']} tem a média {students['avgr']} e está reprovado.")