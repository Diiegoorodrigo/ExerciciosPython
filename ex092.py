''' Crie um programa que leia
    nome, ano de nascimento, e carteira de trabalho
    e cadastre os com idade em um dicionário
    se caso a CTPS for diferente de zero
    o dicionário recebera também o ano de contratação e salario
    calcule e acrescente com quanto anos irá se aposentar'''
from datetime import datetime
ano_atual = datetime.now().year
pessoa = dict()
pessoa['nome'] = input("Insira seu nome: ")
pessoa['nascimento'] = int(input('Insira seu ano de nascimento: '))
pessoa['CPTS'] = int(input('Insira Nº CPTS, digite [0] se não possuir:  '))
if pessoa['CPTS'] != 0:
  pessoa['contratação'] = int(input('Insira o ano de contratação: '))
  pessoa['salario'] = float(input('Insira o salario: '))
  pessoa['idade'] = ano_atual - pessoa['nascimento']
  pessoa['aposentadoria'] = (pessoa['contratação']+35) - pessoa['nascimento']
for i,v in pessoa.items():
  print(f'{i} é {v}')