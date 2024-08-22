'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200km
e R$ 0,45 para viagens mais longas
'''

n = int(input("Informe a distância da viagem: "))
if n <= 200:
    print(f"O valor da viagem será R${n*0.5:.2f}")
else:
    print(f"O valor da viagem será R${n*0.45:.2f}")
