# Crie um programa que tenha uma tupla
# Nela deve conter nome dos produtos e respecitivamente o preço
# Mostre uma lista de preos organizados em forma tabualr
products = ("Pão", 2.50, "Leite", 4.50, "Batata", 7.50)
for i in range(0, len(products)):
    if i % 2 == 0:
        print(f"{products[i]:.<30}", end=" ")
    else:
        print(f"R${products[i]:>5.2f}")
