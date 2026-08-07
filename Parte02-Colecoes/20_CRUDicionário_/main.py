import os

# criar a lista
usuarios = []

# limpa a tela
os.system("cls" if os.name == "nt" else "clear")

while True:
    #menu
    print(f"{'-'*20}CRUDicionário {'-'*20}")
    print("1 - Cadastra novo usuário")
    print("2 - Listar todos usuário")
    print("3 - Alterardados novo usuário")
    print("4 - Deletar usuário")
    print("1 - sair do programa")
    opcao = input("Informe a opção desejada: ").strip()

    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        case "1": 
            # criar novo dicionário
            usuario = {}
            usuario ['nome'] = input("Informe o nome: ").strip().title()
            usuario ['cpf'] = input("Informe o CPF: ").strip()
            usuario ['email'] = input("Informe o e-mail: ").strip().lower()

            # adiciona dicionário na lista
            usuarios.append(usuario)
            os.system("cls" if os.name == "nt" else "clear")
            continue
        case "2":
            for usuario in usuarios:
                for chave, valor in usuario.items():
                    print(f"{chave.capitalize()}: {valor}")
                print(f"{'-'*40}")
            continue
        case "3":
            #TODO: fazer alterar usuário
            pass
        case "4":
             #TODO: excluir usuário
            pass
        case "5":
            breack 
        case _:   
            print("Opção inválida.")
            continue


