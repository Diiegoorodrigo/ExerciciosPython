# Crie um programa que tenha um tupla com varias palavras
# Depois você mostra para cada palavra onde estão as vogais
words = ("Pedro", "Casa", "Chao")
vogal = ("a", "e", "i", "o", "u")
for i in words:
    i = i.lower()
    lista = []
    for letra in i:
        if letra in vogal:
            lista.append(letra)
    print(f"A palavra {i.capitalize()} contem as vogais {lista}")
