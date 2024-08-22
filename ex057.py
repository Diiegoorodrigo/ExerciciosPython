'''
Faça um programa que leia o sexo de uma pessoa
mas só aceite os valores "M" ou "F".
Caso esteja errado, peça a digitação novamente
até ter um valor correto.
'''

sex = input("Digite o sexo F ou M: ").upper()
while sex not in "MmFf":
    print("OPÇÃO INVÁVLIDA, TENTE NOVAMENTE")
    sex = input("Digite o sexo F ou M: ").upper()