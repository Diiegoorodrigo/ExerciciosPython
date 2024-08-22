# Crie um programa que tenha uma tupla totalmente preenchida
# Obtenha uma contagem por extenso de zero até vinte
# Seu programa deverá ler o núermo pelo teclado e mostralo por extenso
n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
  i = int(input('Informe um número entre 0 e 20: '))
  print(n[i])
  s = str(input('Deseja continuar? [S/N]')).upper()
  if s == 'N':
    print('Programa encerrado')
    break
