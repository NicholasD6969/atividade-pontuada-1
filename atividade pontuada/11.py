import os
os.system("cls || clear")

kg_morangos = float(input("Digite a quantiade de morangos: "))
Kg_Macas = float(input("Digite a quantidade de Maças: "))

if kg_morangos > 5:
    preço_morango = 2.20
else:
    preço_morango = 2.50  
if Kg_Macas >5:
    preço_macas = 1.50
else:
    preço_macas = 1.80

if preço_morango >= 15.0:
    