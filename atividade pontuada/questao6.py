import os
os.system("clear") 

primeira_nota = float(input("Digite sua primeira nota: "))
segunda_nota = float(input("Digite sua segunda nota"))

soma = primeira_nota + segunda_nota
media = soma

print(f"media: (media)")

if media >=6 :
    print("aprovado")
elif media >4:
    print("recuperação")
else:
    print("reprovado")
    