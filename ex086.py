'''
Crie um programa que crie uma matriz 3.3
e preencha com valores lidos pelo teclado.

No final, mostre a matriz na tela com a formatação correta
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for c in range(0, 3):
        matriz[i][c] = int(input(f"Insira um numéro na matriz {[i]}{[c]}: "))
print("=-="*30)
for i in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[i][c]:^5}]", end='')
    print()
