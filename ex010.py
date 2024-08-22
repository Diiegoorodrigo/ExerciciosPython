# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar
# Considere o valor do dolar R$ 5,45
n = float(input("Informe o valor em sua carteira: "))
d = 5.45
print(f"O valor R${n:.2f} em dolares são ${(n/d):.2f}")
