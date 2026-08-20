import funcao f:


def menu():
    while True:
        f.limpar_terminal()
        print("========== MENU DE FUNÇÕES ==========")
        print("1 - Calcular Potência")
        print("2 - Calcular Raiz Quadrada")
        print("3 - Calcular Volume Paralelepípedo")
        print("4 - Calcular Volume Cilíndrico")
        print("5 - Limpar Terminal")
        print("0 - Sair")
        print("=====================================")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            f.potencia()
        elif opcao == '2':
            f.raiz_quadrada()
        elif opcao == '3':
            f.volume_paralelepipedo()
        elif opcao == '4':
            f.volume_cilindro()
        elif opcao == '5':
            f.limpar_terminal()
            print("Terminal limpo!")
        elif opcao == '0':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida!")
        
        input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    menu()