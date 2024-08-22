''' Crie um programa que leia o ano de nascimento de sete pessoas
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores'''
from datetime import date
yearAc = date.today().year
count_young = 0
count_adult = 0
for i in range (0,7):
    year = int(input("Insira o ano de nascimento: "))
    if yearAc - year > 18:
        count_adult += 1
    else:
        count_young +=1
print(f"A quantidade de maiores de 18 são {count_adult} pessoas e os menores de 18 são {count_young} pessoas")

