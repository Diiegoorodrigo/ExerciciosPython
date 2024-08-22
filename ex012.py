# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
n = float(input("Informe o valor do produto: "))
print(f"O valor R$ {n:.2f} com desconto de 5% ficará R${n-(n*0.05):.2f}")
