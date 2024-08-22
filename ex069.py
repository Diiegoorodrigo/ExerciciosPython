# Crie um programa que leia idade e o sexo de varias pessoas
# Pergunte se o usuário deseja continuar e no final mostre:
# quantas pessoas tem mais de 18 anos
# quantos homens foram cadastrados
# quantas mulheres tem menos de 20 anos
pMaior = 0
qtdH = 0
qtdM = 0
while True:

  idade = int(input('Informe a idade: '))
  if idade > 18:
    pMaior += 1
  print('-=-'*30)
  sexo = str(input('Informe o sexo [M/F]: ')).upper()
  print('-=-'*30)
  while sexo not in 'MmFf':
    print('-=-'*30)
    print('OPÇÃO INVÁLIDA! Tente novamente.')
    print('-=-'*30)
    sexo = str(input('Informe o sexo [M/F]')).upper()
    print('-=-'*30)
  if sexo == 'M':
    qtdH += 1
  elif sexo in 'Ff' and idade < 20:
    qtdM += 1
  segue = str(input('Deseja continuar [S/N]? ')).upper()
  while segue not in 'SsNn':
    print('-=-'*30)
    print('OPÇÃO INVÁLIDA! Tente novamente.')
    print('-=-'*30)
    segue = str(input('Deseja continuar [S/N]? ')).upper()
    print('-=-'*30)
  if segue == 'N':
    print('-=-'*30)
    print('PROGRAMA ENCERRADO!')
    break
print(f'Houve {pMaior} cadastradas tem mais de 18 anos!')
print(f'Foram cadastrados {qtdH} homens')
print(f'Foram cadastradas {qtdM} mulheres com menos de 20 anos')