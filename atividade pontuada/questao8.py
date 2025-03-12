import os
os.system("clear")

cd = float(input("Digite a cor do cd: "))

match cd:
    case "verde":
        print("R$10,00")
    case "azul":
        print("20,00")
    case "amarelo":
        print("30,00")
    case "amarelo":
        print("40,00") 
    case _:
        print ("opção invalída")              