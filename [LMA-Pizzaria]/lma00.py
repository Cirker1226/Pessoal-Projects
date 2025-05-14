print("====================================================================")
print("                    PIZZARIA LMA - SEJA BEM VINDO                   ")
print("====================================================================")
print("")
print("                        CARDÁPIO - PREÇOS                           ")
print("                        PIZZAS - SABORES                            ")
print("")
print("1. CALABRESA      - R$ 15,00")
print("2. FRANGO         - R$ 20,00")
print("3. CATUPIRY       - R$ 30,00")
print("4. MARGUERITA     - R$ 30,00")
print("5. PORTUGUESA     - R$ 25,00")
print("6. QUATRO QUEIJOS - R$ 25,00")
print("7. PEPPERONI      - R$ 25,00")
print("8. VEGETARIANA    - R$ 30,00")
print("9. MUSSARELA      - R$ 25,00")
print("")
print("                        PIZZAS - TAMANHO                            ")
print("1. PEQUENA  - R$ 5,00")
print("2. MÉDIA    - R$ 8,00")
print("3. GRANDE   - R$ 10,00")
print("")
print("                        REFRIGERANTES                               ")
print("1. COCA-COLA. R$ 7,00")
print("2. GUARANÁ   . R$ 6,00")
print("3. FANTA     . R$ 5,00")
print("====================================================================")
print("")
print("Digite o número do sabor da pizza:")

#Lê a escolha da pizza do usuário e converte para inteiro
pedidopizza = int(input())

print("DIGITE O TAMANHO DA PIZZA:")
print("P - PEQUENA")
print("M - MÉDIA")
print( "G - GRANDE")
print("______________________________________")
#Lê a escolha do tamanho da pizza do usuário e converte para maiúsculo
tampizza = input().upper()

print("FAÇA O SEU PEDIDO PARA REFRIGERANTE:")
print("1 - COCA-COLA")
print("2 - GUARANÁ")
print("3 - FANTA")
print("_________________________________________")
# Lê a escolha do refrigerante do usuário e converte para inteiro
pedidorefri = int (input())




#Calcule opreço total e descreve o pedido utilizando elif com parênteses
if(pedidopizza == 1) and (tampizza == "P") and (pedidorefri == 1):
    precopagar = 10.00 + 7.00 
    pedidos = "CALABRESA, PEQUENA, COCA-COLA"

elif(pedidopizza == 1) and (tampizza == "P") and (pedidorefri == 2):
    precopagar = 10,00 + 6,000 
    pedidos = "CALABRESA, PEQUENA, GUARANÁ"

elif(pedidopizza == 1) and (tampizza == "P") and (pedidorefri == 3):
    precopagar = 10,00 + 5,00 
    pedidos = "CALABREZA, PEQUENA, FANTA"

elif (pedidopizza == 2) and (tampizza == "P") and (pedidorefri == 1):
    precopagar =10,00 + 7,0 
    pedidos = "FRANGO, PEQUENA, COCA-COLA"

elif(pedidopizza == 2) and (tampizza == "P") and (pedidorefri == 3):
    precopagar = 10.00 + 5.00 
    pedidos = "FRANGO, PEQUENA, FANTA"

elif(pedidopizza == 2) and (tampizza == "P") and (pedidorefri == 2):
    precopagar = 10. + 6.00 
    pedidos = "FRANGO, PEQUENA, GUARANÁ"

elif(pedidopizza == 3) and (tampizza == "P") and (pedidorefri == 1):
    precopagar = 10.00 + 7.00 
    pedidos = "CATUPIRY, PEQUENA, COCA-COLA"

elif(pedidopizza == 3) and (tampizza == "P") and (pedidorefri == 3):
    precopagar = 10.00 + 5.00 
    pedidos = "CATUPIRY, PEQUENA, FANTA"

elif(pedidopizza == 3) and (tampizza == "P") and (pedidorefri == 2):
    precopagar = 10.00 + 6.00 
    pedidos = "CATUPIRY, PEQUENA, GUARANÁ"
#Variação com tamanho médio
elif(pedidopizza == 1) and (tampizza == "M") and (pedidorefri == 1):
    precopagar = 15.00 + 7.00 
    pedidos = "CALABREZA, MÉDIA, COCA-COLA"

elif(pedidopizza == 1) and (tampizza == "M") and (pedidorefri == 2):
    precopagar = 15.00 + 6.00 
    pedidos = "CALABRESA, MÉDIA, GUARANÁ"

elif(pedidopizza == 1) and (tampizza == "M") and (pedidorefri == 3):
    precopagar = 15.00 + 5.00 
    pedidos = "CALABRESA, MÉDIA, FANTA"

elif(pedidopizza == 2) and (tampizza == "M") and (pedidorefri == 1):
    precopagar = 15.00 + 7.00 
    pedidos = "FRANGO, MÉDIA, COCA-COLA"

elif(pedidopizza == 2) and (tampizza == "M") and (pedidorefri == 3):
    precopagar = 15.00 + 5.00 
    pedidos = "FRANGO, MÉDIA, FANTA"

elif(pedidopizza == 2) and (tampizza == "M") and (pedidorefri == 2):
    precopagar = 15.00 + 6.00 
    pedidos = "FRANGO, MÉDIA, GUARANÁ"

elif(pedidopizza == 3) and (tampizza == "M") and (pedidorefri == 1):
    precopagar = 15.00 + 7.00 
    pedidos = "CATUPIRY, MÉDIA, COCA-COLA"

elif(pedidopizza == 3) and (tampizza == "M") and (pedidorefri == 3):
    precopagar = 15.00 + 5.00 
    pedidos = "CATUPIRY, MÉDIA, FANTA"

elif(pedidopizza == 3) and (tampizza == "M") and (pedidorefri == 2):
    precopagar =15.00 + 6.00 
    pedidos = "CATUPIRY, MÉDIA, GUARANÁ"

#variação de tamanho grande

elif(pedidopizza == 1) and (tampizza == "G") and (pedidorefri == 1):
    precopagar = 20.00 + 7.00 
    pedidos = "CALABREZA, GRANDE, COCA-COLA"

elif(pedidopizza == 1) and (tampizza == "G") and (pedidorefri == 2):
    precopagar = 20.00 + 6.00 
    pedidos = "CALABRESA, GRANDE, GUARANÁ"

elif(pedidopizza == 1) and (tampizza == "G") and (pedidorefri == 3):
    precopagar = 20.00 + 5.00 
    pedidos = "CALABRESA, GRANDE, FANTA"

elif(pedidopizza == 2) and (tampizza == "G") and (pedidorefri == 1):
    precopagar = 20.00 + 7.00 
    pedidos = "FRANGO, GRANDE, COCA-COLA"

elif(pedidopizza == 2) and (tampizza == "G") and (pedidorefri == 3):
    precopagar = 20.00 + 5.00 
    pedidos = "FRANGO, GRANDE, FANTA"

elif(pedidopizza == 2) and (tampizza == "G") and (pedidorefri == 2):
    precopagar = 20.00 + 6.00 
    pedidos = "FRANGO, GRANDE, GUARANÁ"

elif(pedidopizza == 3) and (tampizza == "G") and (pedidorefri == 1):
    precopagar = 20.00 + 7.00 
    pedidos = "CATUPIRY, GRANDE, COCA-COLA"

elif(pedidopizza == 3) and (tampizza == "G") and (pedidorefri == 3):
    precopagar = 20.00 + 5.00 
    pedidos = "CATUPIRY, GRANDE, FANTA"

elif(pedidopizza == 3) and (tampizza == "G") and (pedidorefri ==2):
    precopagar = 20.00 + 6.00 
    pedidos = "CATUPIRY, GRANDE, GUARANÁ"
else:
    procopagar = 0.0
    pedidos = "PEDIDO INVÁLIDO"

#Exibe o resumo do pedido e o  preço total a pagar.
print("_____________________________________________________________")
print(f"O TOTAL A PAGAR É: R$ {precopagar:.2f}")
print ("_____________________________________________________________")
print(f"OS PEDIDOS fORAM {pedidos}")
print ("_____________________________________________________________")
print(f"bom apetite e seja bem vindo")


