# Crie um programa que leia nome e duas notas de varios alunos
# Guarde em uma lista composta
# No final mostre o boletim contendo a média
# Mostre a oção de consulta individual para as notas dos alunos.
ficha = list()
while True:
  nome = input("Insira o nome: ")
  n1 = float(input("Insira a nota 1: "))
  n2 = float(input("Insira a nota 2: "))
  media = (n1 + n2) / 2
  ficha.append([nome, [n1, n2], media])
  opt = input("Deseja continuar? [S] ou [N]: ").upper()
  while opt not in "SN":
    print("Opção inválida, tente novamente!")
    opt = input("Deseja continuar? [S] ou [N]: ").upper()
  if opt == "N":
    print("OBRIGADO, FINALIZANDO")
    print("-=-"*20)
    break
  print("Continuando..")
  print("-=-"*20)
print(f"{'No.':<4}{'NOME':<10}{'MEDIA':>8}")
for i, a in enumerate(ficha):
  print(f"{i:<4}{a[0]:<10}{a[2]:>8}")
print("-=-"*20)
while True:
  n = int(input("Qual aluno deseja ver a ficha ou digite 999 para sair: "))
  if n == 999:
    print("Finalizando!")
    break
  if n <= len(ficha) -1:
    print(f"O Aluno {ficha[n][0]} tem as notas {ficha[n][1]}")
    print("-=-"*20)
print("OBRIGADO VOLTE SEMPRE")