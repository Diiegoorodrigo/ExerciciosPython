# Crie um programa que leia sete números
# Mantenha separados os impares e pares
# Mostre ambos em ordem crescente
par = list()
impar = list()
for i in range(0, 7):
    n = int(input(f"Digite o {i+1}º número: "))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

par.sort()
impar.sort()
print(f"Os números pares são {par}")
print(f"Os números impares são {impar}")