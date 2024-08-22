'''
Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
- o primeiro valor é maior
- o segundo valor é maior
- não existe valor maior; os dois são iguais
'''
n = int(input("Insira o primeiro número: "))
ns = int(input("Insira o segundo número: "))
if n > ns:
    print(f"O primeiro valor é maior que o segundo.")
elif n < ns:
    print(f"O segundo número é maior.")
else:
    print(f"Os números são iguais.")