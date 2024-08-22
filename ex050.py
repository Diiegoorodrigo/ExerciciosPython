'''
Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares
Se o valor digitado for ímpar, desconsidere-o.'''
s = 0
for i in range(0, 6):
    int(input("Digite um número: "))
    if i % 2 == 0:
        s += i
print(f"A soma dos números fica pares fica {s}")