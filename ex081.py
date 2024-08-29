# Crie um programa que o usuario digite varios numeros
# Mostre quantos números foram digitados
# Mostre os números em forma decrescente
# Mostre se o valor 5 foi digitado ou não

num = []
n = int
count = 0
print("Para sair digite 999")
while True:
  n = int(input("Insira um número: "))
  if n == 999:
    if len(num) == 0:
      print("Você não digitou nenhum número")
    break
  if 5 in num:
    count += 1
  num.append(n)
num.sort(reverse = True)
print(f"Foram digitado {len(num)} número(s)")
if len(num) > 0 :
  print(f"Esses são todos os números em ordem decrescente {num}")
if count >= 1:
  print(f"O número 5 foi digitado {num.count(5)} vez(es)")
else:
  print("O número 5 não foi encontrado na lista.")