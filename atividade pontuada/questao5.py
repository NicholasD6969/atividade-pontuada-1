import os
os.system("clear")

primeiro_numero = int(input("Digite um número: "))
operador = input("Digite a operaçao que deseja (+ - * /): ")
segundo_numero = int(input("Digite um numero: "))

#processamento
match operador:
    case"+":
        resultado = primeiro_numero + segundo_numero
    case"-":
        resultado = primeiro_numero- segundo_numero
    case"*":
        resultado = primeiro_numero * segundo_numero
    case"/":
        resultado = primeiro_numero / segundo_numero 
    case _:
        resultado= "opção inválida"
                 
print(f"primeiro numero: {primeiro_numero}")
print(f"operação: {operador}")  
print(f"segundo numero: {segundo_numero}")
print(f"resultado: {resultado}")
   


