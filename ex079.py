# Crie um programa que o usuario digite varios numeros
# Cadastre em uma lista caso o valor já exista nao sera adicionado
# no final serao exibidos todos os valores em ordem crescente

num = []
n = int
print("Para sair digite 999")
while True:
    n = int(input("Insira um número: "))
    if n == 999:
        if len(num) == 0:
            print("Você não digitou nenhum número")
        break
    if n not in num:
        num.append(n)

num.sort()
if len(num) > 0:
    print(f"Esses são todos os números em ordem crescente {num}")