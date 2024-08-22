# Crie um programa que leia o nome e o preço de varios produtos
# Pergunte se o usuário deseja continuar e no final mostre:
# Total gasto na compra
# Quantos produtos custaram mais que R$ 1000.
# Qual é o nome do produto mais barato
soma = 0
valorAcima = 0
maisBarato = 10000000000000
pBarato = ''
while True:
  produto = str(input('Informe o nome do produto: ')).upper()
  print('-=-'*15)
  valor = float(input('Informe o valor do produto: '))
  print('-=-'*15)
  soma += valor
  if valor > 1000:
    valorAcima += 1
  if valor < maisBarato:
    maisBarato = valor
    pBarato = produto
  segue = str(input('Deseja continuar? [S/N]: ')).upper()
  print('-=-'*15)
  while segue not in 'NnSs':
    print('ESCOLHA INVÁLIDA!')
    print('-=-'*15)
    segue = str(input('Deseja continuar? [S/N]: ')).upper()
    print('-=-'*15)
  if segue == 'N':
    print('PROGRAMA ENCERRADO!')
    print('-=-'*15)
    break
print(f'O valor total da compra deu {soma:.2f}')
print('-=-'*15)
print(f'Foram {valorAcima} produtos com o valor acima de R$ 1000,00')
print('-=-'*15)
print(f' {pBarato} foi o produto mais barato, custando R${maisBarato:.2f}')