'''
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

- média abaixo de 5.0: reprovado
- média entre 5.0 e 6,9: recuperação
- média 7.0 ou superior: aprovado
'''

n1 = float(input("Insira a primeira nota: "))
n2 = float(input("Insira a segunda nota: "))
media = (n1 + n2)/2
if media >= 7:
    print(f"Sua média é {media}, parabens está aprovado.")
elif media < 5:
    print(f"Sua média é {media}, você está reprovado!")
else:
    print(f"Sua média é {media}, você ficou de recuperação.")