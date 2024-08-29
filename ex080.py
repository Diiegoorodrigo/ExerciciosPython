'''
Crie um programa onde o usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista, já na posição correta de inserção
(sem usar o sort()).

No final, mostre a lista ordenada na tela.
'''
num = []
for c in range(0, 5):
    n = int(input("Insira um número: "))
    if c == 0 or n > num[-1]:
        num.append(n)
        print("O número foi inserio no final da lista")
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos, n)
                print(f"O número foi inserido na posição {pos} da lista")
                break
            pos += 1
print(num)