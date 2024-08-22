# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# 0e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado
print("Calcular custo de aluguel de carro")
print("-=-"*15)
k = float(input("Informe a quantidade de quilomêtros percorridos: "))
days = int(input("Informe a quantidade de dias: "))
day_price = days*60
k_price = k*0.15
print("-=-"*15)
print(f"O total de {days} ficará R${day_price:.2f}")
print(f"O total de {k}Kms rodados ficará R${k_price:.2f}")
print(f"O custo do carro ficará R${k_price+day_price:.2f} ")
