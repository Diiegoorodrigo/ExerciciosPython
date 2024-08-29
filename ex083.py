'''
Crie um programa onde o usuário digite uma expressão qualquer
que use parênteses.
Seu aplicativo deverá analisar se a expressão passada
está com os parênteses abertos e fechados na ordem correta.
'''

simb = []
expres = input("Digite uma expressão: ")
for c in expres:
    if c == "(":
        simb.append("(")
    elif c == ")":
        if len(simb) > 0:
            simb.pop()
        else:
            simb.append(")")
            break
if len(simb) == 0:
    print("Valido!")
else:
    print("Inválido!")
print(simb)
