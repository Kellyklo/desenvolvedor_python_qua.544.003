# tratamento de exceção
try:
    while True:
        nome = input("informe o nome:"). strip().title()
        idade = int(input("informe a idade:"))
        altura = float(input("informe a altura em metros:").replace(",", "."))

        if idade >= 12 and altura >= 1.25:
            print(f"{nome} está liberado")
        else:
            print(f"Entrada de {nome} proíbida")

        print("1 - Passa novo pagante.")
        print("2 - Encerrar programa.")

        opcao = input("Informe a opção desejada:").strip()

        match opcao:
            case "1":
                continue
            case "2":
                print("Programa encerrado.")
                break
            case _: 
                print("Opção inválida.")
                continue        
except:
    print("Não foi possivel registrar a entrada do pagante.")