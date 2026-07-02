# entrada de dados
x = float(input("Informo o valor de X:").replace (",","."))
y = float(input("Informo o valor de y:").replace (",","."))

#menu
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

opcao = input("Informe a opção desejada: ").strip()

match opcao: 
    case "1":
        print(f"a soma é {x+y}.")
    case "2":
        print(f"a subtração é {x-y}.")
    case "3":
        print(f"a multiplicação é {x*y}.")
    case "4":
        print(f"a divisão é {x/y}.")
    case _:
        print("Opção invalida.")
        
