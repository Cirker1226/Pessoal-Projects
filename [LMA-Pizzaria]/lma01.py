import os
os.system('cls' if os.name == 'nt' else 'clear')

# Listas a serem utilizadas.

lista_sabores = ["CALABRESA", "FRANGO", "CATUPIRY", "MARGUERITA", "PORTUGUESA", "QUATRO QUEIJOS", "PEPPERONI", "VEGETARIANA", "MUSSARELA"]
preço_sabores = [15, 20, 30, 30, 25, 25, 20, 30, 25]
lista_tamanhos = ["PEQUENA", "MÉDIA", "GRANDE"]
precos_tamanhos = [5, 8, 10]
lista_refrigerantes = ["COCA-COLA", "GUARANÁ", "FANTA"]
precos_refrigerantes = [7, 6, 5]

# Exibe o cardapio da Pizzaria.

print("_____________________________________________________________")
print("")
print("PIZZARIA LMA - SEJA BEM VINDO".center(60))
print("")
print("_____________________________________________________________")

print("\n", "CARDÁPIO - PREÇOS".center(60))
print("PIZZAS - SABORES".center(60))
print("")

for i, (sabor, preço) in enumerate(zip(lista_sabores, preço_sabores), 1):
    print(f"{i}. {sabor} - R$ {preço},00")

print("")
print("PIZZAS - TAMANHO".center(60), "\n")

for i, (tamanho, preco) in enumerate(zip(lista_tamanhos, precos_tamanhos), 1):
    print(f"{i}. {tamanho} - R$ {preco},00")

print("")
print("REFRIGERANTES \n".center(60))

for i, (refri, preco) in enumerate(zip(lista_refrigerantes, precos_refrigerantes), 1):
    print(f"{i}. {refri}. R$ {preco},00")

print("_____________________________________________________________")

# Escolha do sabor

while True:
    try:
        pedidopizza = int(input("Digite o número do sabor da pizza: "))
        if 1 <= pedidopizza <= len(lista_sabores):
            sabor_escolhido = lista_sabores[pedidopizza-1]
            preço_pizzasabor = preço_sabores[pedidopizza-1]
            break
        else:
            print("Sabor inválido, por favor escolha um sabor listado!")
    except ValueError:
        print("Digite um número válido!")

# Escolha do tamanho

while True:
    try:
        tampizza = int(input("Digite o número do tamanho da pizza: "))
        if 1 <= tampizza <= len(lista_tamanhos):
            tamanho_escolhido = lista_tamanhos[tampizza-1]
            preco_pizzatamanho = precos_tamanhos[tampizza-1]
            break
        else:
            print("Tamanho inválido, por favor escolha um tamanho listado!")
    except ValueError:
        print("Digite um número válido!")

# Escolha do refrigerante

while True:
    try:
        pedidorefri = int(input("Digite o número do refrigerante: "))
        if 1 <= pedidorefri <= len(lista_refrigerantes):
            refri_escolhido = lista_refrigerantes[pedidorefri-1]
            preco_refri = precos_refrigerantes[pedidorefri-1]
            break
        else:
            print("Refrigerante inválido, por favor escolha um refrigerante listado!")
    except ValueError:
        print("Digite um número válido!")

# Exibe o resumo do pedido e o preço total a pagar.

total = preço_pizzasabor + preco_pizzatamanho + preco_refri

print("")
print("_____________________________________________________________", "\n")
print(f"O TOTAL A PAGAR É: R$ {total},00", "\n")
print("_____________________________________________________________", "\n")
print("Resumo do Pedido".center(60))
print("")
print(f"Pizza de {sabor_escolhido} - {tamanho_escolhido}")
print(f"Refrigerante: {refri_escolhido}", "\n")
print("_____________________________________________________________")
print("")
print("Agradecemos a preferência!")
print("")
print("_____________________________________________________________")