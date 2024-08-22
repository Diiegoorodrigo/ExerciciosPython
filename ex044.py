'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal, e condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- em 3x ou mais no cartão: 20% de juros
'''

price = float(input("Insira o valor do produto: "))
pay = int(input('''
    FORMAS DE PAGAMENTO
    [ 0 ] A VISTA DINHEIRO OU CHEQUE
    [ 1 ] A VISTA CARTÃO
    [ 2 ] PARCELADO EM ATÉ 2x
    [ 3 ] PARCELADO ACIMA DE 3x
    
    ESCOLHA A FORMA DE PAGAMENTO: '''))

while pay not in (0, 1, 2, 3):
    print("ERRO FORMA DE PAGAMENTO INVALIDA!! TENTE NOVAMENTE")
    pay = int(input('''
        FORMAS DE PAGAMENTO
        [ 0 ] A VISTA DINHEIRO OU CHEQUE
        [ 1 ] A VISTA CARTÃO
        [ 2 ] PARCELADO EM ATÉ 2x
        [ 3 ] PARCELADO ACIMA DE 3x

        ESCOLHA A FORMA DE PAGAMENTO: '''))
if pay == 0:
    print(f"O valor do item é {price:.2f}, você recebeu um desconto de 10% e valor total ficou {price - (price * 0.1):.2f}")
elif pay == 1:
    print(f"O valor do item é {price:.2f}, você recebeu um desconto de 10% e valor total ficou {price - (price * 0.05):.2f}")
elif pay == 2:
    print(f"O valor do item a ser pago é {price:.2f} em 2 parcelas de {price/2:.2f}")
else:
    parc = int(input("Parcelar em quantas vezes: "))
    print(f"O valor do item é {price:.2f}, receberá juros de 20% ficando o total de {price + (price * 0.2):.2f} e será pago em {parc} parcelas de {(price + (price * 0.2))/parc:.2f}")
