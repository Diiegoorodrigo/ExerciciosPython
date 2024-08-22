'''
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa
O programa vai perguntar o valor da casa, o salário do comprador e em quantos
anos ele vai pagar

Calcule o valor da prestação mensal,
sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado
'''

print('-=-'*20)
print("Simulação de emprestimo")
print('-=-'*20)
sal = float(input("Informe o valor do seu salário: "))
empres = float(input("Informe o valor desejado: "))
anos = int(input("Informe em quantos anos pretende quitar: "))*12
par = empres / anos
if par > sal*0.3:
    print('-=-' * 20)
    print("EMPRESTIMO NEGADO")
else:
    print('-=-' * 20)
    print("PARABENS EMRPESTIMO APROVADO!")
