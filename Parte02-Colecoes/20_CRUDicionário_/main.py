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
    print("3 - Alterar dados novo usuário")
    print("4 - Deletar usuário")
    print("1 - sair do programa")
    opcao = input("Informe a opção desejada: ").strip()

    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        case "1": 
            # criar nov o dicionário
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
            nome = input("Informe o nome a ser pesquisado:").strip().title()
            for usuario in usuarios:
                if nome in usuario['nome']:
                    #2º menu
                    print("nome")
                    print("CPF")
                    print("email")
                    print("cancelar")
                    alterar = input("Qual chave deseja alterar?").strip().lower()
                    if alterar in usuario:
                        usuario[alterar] = input("Informe o novo valor:").strip()
                        print("alterado com sucesso.")
                else: 
                    #Review: mensagem bugada
                    print("Usuario não encontrado.")
            continue
        case "4":
            nome = input("Informe o nome a ser deletado:").strip().title()
            for usuario in usuario:
                if nome in usuario['nome']:
                    indice = usuarios.index(usuario)
                    del(usuario)
                    print("Usuário deletado com sucesso!")
                else:
                    print("Usuaário não encontrado.")
            continue
        case "5":
            break 
        case _:   
            print("Opção inválida.")
            continue
