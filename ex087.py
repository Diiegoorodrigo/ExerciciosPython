'''
Aprimore o desafio anterior, mostrando no final:

a: a soma de todos os valores pares digitados
b: a soma dos valores da terceira coluna
c: o maior valor da segunda linha
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = soma_col = maior_l = 0
for i in range(0, 3):
    for c in range(0, 3):
        matriz[i][c] = int(input(f"Insira um numéro na matriz {[i]}{[c]}: "))
        if matriz[i][c] % 2 == 0:
            pares += matriz[i][c]
for i in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[i][c]:^5}]", end='')
    print()
print("=-="*30)
for i in range(0, 3):
    soma_col += matriz[i][2]
    if matriz[1][i] > maior_l:
        maior_l = matriz[1][i]
print("=-="*30)
print(f"A soma dos números pares é {pares}")
print(f"A soma dos valores da terceira coluna é {soma_col}")
print(f"O maior da segunda linha é {maior_l}")