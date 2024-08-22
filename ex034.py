'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento

Para salários superiores a R$ 1.250,00, calcule um aumento de 10%

Para os inferiores ou iguais, o aumento é de R$ 15%.
'''
sal = float(input("Informe seu salário: "))
if sal > 1250:
    print(f"Você receberá 10% de aumento e seu salário será R${sal+(sal*0.1):.2f}")
else:
    print(f"Você receberá 15% de aumento e seu salário será R${sal+(sal*0.15):.2f}")
    