# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
n = float(input("Informe o valor do seu salário: "))
print(f"O seu salário atual é R${n:.2f} com aumento de 15% ficará R${n+(n*0.15):.2f}")
