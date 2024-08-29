# Escreva um programa que cria uma lista e leia números
# Crie mais duas listas de número impares e pares
# Mostre o conteúdo das três listas.
num = []
n_par = []
n_impar = []
n = int
count = 0
print("Para sair digite 999")
while True:
  n = int(input("Insira um número: "))
  if n == 999:
    if len(num) == 0:
      print("Você não digitou nenhum número")
    break
  num.append(n)  
  if n % 2 == 0:
    n_par.append(n)
  else:
    n_impar.append(n)
if len(num) > 0:  
  print(f"Os números digitados foram {num}")
  print(f"Os números pares digitados foram {n_par}")
  print(f"Os números impares digitados foram {n_impar}")
