# Faça um programa que leia a largura e a altura de uma parede em metros
# calcule a sua área e a quantidade de tinta necessária para pintá-la
# sabendo que cada litro de tinta pinta uma área de 2m²
print("Calculo para uso de tinta para pintar parede")
print("-=-"*10)
h = float(input("Insira a largura da parede: "))
a = float(input("Insira a altura da parede: "))
print(f"A área parede contem {h*a}m² e será necessário {(h*a)/2} litros de tinta para pintar a parede")
